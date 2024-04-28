import os
from pymongo import MongoClient
from bson.json_util import dumps
from pydantic import BaseModel, Field

# Doğrudan URI'yi kullanarak MongoDB bağlantısı kurma
MONGO_URI = "mongodb+srv://oktaronder:oktaronder123@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1"
client = MongoClient(MONGO_URI)
db = client['house_info']
collection_sale = db['for_sale']
collection_rent = db['for_rent']

class PropertyQuerySchema(BaseModel):
    property_type: str = Field(..., pattern="^(rent|sale)$", title="Property Type", description="Specify 'rent' for rental properties or 'sale' for properties for sale.")

def fetch_properties(property_type: str):
    """
    Fetches properties from the MongoDB database based on the specified type.
    """
    if property_type == 'sale':
        data = list(collection_sale.find())
    elif property_type == 'rent':
        data = list(collection_rent.find())
    else:
        return {"error": "Invalid property type specified"}

    return dumps(data) if data else "No properties found matching the criteria"

# Example of defining the tool registration (for systems supporting tool plugins)
tools = [
    {
        "name": "fetch_properties",
        "description": "Fetches properties for sale or rent from MongoDB.",
        "parameters": PropertyQuerySchema.schema(),
        "runCmd": fetch_properties,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    }
]

