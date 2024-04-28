from pydantic import BaseModel
from pymongo import MongoClient
from bson.json_util import dumps

# MongoDB connection setup
MONGO_URI = "mongodb+srv://oktaronder:oktaronder123@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1"
client = MongoClient(MONGO_URI)
db = client['user_database']
collectionUser = db['user_info']

class FetchUsersSchema(BaseModel):
    # No filtering parameters needed
    pass

def fetch_all_users():
    """
    Fetches all user information from the MongoDB database without any filters.
    """
    users_cursor = collectionUser.find()
    users_list = []
    for user in users_cursor:
        user_data = {
            'full_name': user.get('full_name', ''),
            'phone_number': user.get('phone_number', ''),
            'email_address': user.get('email_address', ''),
            'residents': user.get('residents', ''),
            'has_children': user.get('has_children', False),
            'property_type': user.get('property_type', ''),
            'budget': user.get('budget', 0),
            'city': user.get('city', '')
        }
        users_list.append(user_data)

    return dumps(users_list) if users_list else "No users found"

# Tool registration example
tools = [
    {
        "name": "fetch_all_users",
        "description": "Fetches all user information from MongoDB without any filters.",
        "parameters": FetchUsersSchema.schema(),
        "runCmd": fetch_all_users,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    }
]
