import os
from pymongo import MongoClient
from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserInfoSchema(BaseModel):
    full_name: str = Field(..., title="Full Name", description="User's full name")
    phone_number: str = Field(..., pattern="^\+?1?\d{9,15}$", title="Phone Number", description="User's phone number in international format")
    email_address: EmailStr = Field(..., title="Email Address", description="User's email address")
    residents: int = Field(..., title="Residents", description="Number of people living in the house", ge=1)
    has_children: bool = Field(..., title="Children at Home", description="Are there any children staying with you?")
    property_type: str = Field(..., pattern="^(rent|sale)$", title="Rent or Sale", description="Is the property for rent or sale?")
    budget: float = Field(..., title="Budget", description="User's budget", gt=0)
    city: str = Field(..., title="City", description="City where the user is looking for a property")

# MongoDB connection setup
MONGO_URI = "mongodb+srv://oktaronder:oktaronder123@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1"  # Replace with your actual MongoDB URI
client = MongoClient(MONGO_URI)
db = client['user_database']  # Adjust 'user_database' to your actual database name
collection = db['user_info']  # Adjust 'user_info' to your actual collection name

def custom_json_schema(model):
    schema = model.schema()
    properties_formatted = {
        k: {
            "title": v.get("title"),
            "type": v.get("type"),
            "description": v.get("description")
        } for k, v in schema["properties"].items()
    }
    return {
        "type": "object",
        "default": {},
        "properties": properties_formatted,
        "required": schema.get("required", [])
    }

def collect_and_save_user_info(full_name: str, phone_number: str, email_address: str, residents: int, has_children: bool, property_type: str, budget: float, city: str):
    try:
        # Create an instance of UserInfoSchema to validate the data
        user_info = UserInfoSchema(
            full_name=full_name,
            phone_number=phone_number,
            email_address=email_address,
            residents=residents,
            has_children=has_children,
            property_type=property_type,
            budget=budget,
            city=city
        )
        # Convert validated data to dictionary and insert into MongoDB
        collection.insert_one(user_info.dict())
        return "User info successfully saved to MongoDB."
    except ValidationError as e:
        return {"error": str(e)}

# Example of defining the tool registration (for systems supporting tool plugins)
tools = [
    {
        "name": "user_info_collector",
        "description": "Collects and validates user's personal information and stores it in MongoDB.",
        "parameters": custom_json_schema(UserInfoSchema),
        "runCmd": collect_and_save_user_info,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    }
]

