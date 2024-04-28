from flask import Flask
import logging
from twilio.rest import Client
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb+srv://kaanacar:kaanacar123@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1")
db = client['house_info']
collection_names = db.list_collection_names()

# Send SMS function revised with improved error handling
def send_sms(v_id=None, receiver_number=None):
    if not v_id or not receiver_number:
        logging.error("Receiver number or v_id is missing.")
        return {"error": "Receiver number and id are required."}, 400

    # Search for document in MongoDB
    document = None
    for collection_name in collection_names:
        collection = db[collection_name]
        document = collection.find_one({'v_id': {'$regex': v_id, '$options': 'i'}})
        if document:
            break

    if not document:
        logging.error("Document not found for title: %s", v_id)
        return {"error": "Document not found"}, 404

    # Twilio client setup and message construction
    twilio_client = Client('AC683dd1233d20210e8ced64ec278a3e41', 'be3e11044b1a47d5e6b7818c979e5bb3')
    message_body = (
        f"{document['title']}\n\n"
        f"Area: {document['closed_area']}\n"
        f"Price: {document['price']}\n"
        f"Bedrooms: {document['bedrooms']}\n"
        f"Bath: {document['bath_wc']}\n"
        f"Status: {document['item_status']}\n"
        f"City: {document['city']}\n"
        f"Description: {document['short_description']}"
    )

    # Send message using Twilio
    try:
        message = twilio_client.messages.create(
            from_='+15012155802',
            body=message_body,
            to=receiver_number
        )
        logging.info("SMS sent successfully: %s", message.sid)
        return {"message_sid": message.sid}
    except Exception as e:
        logging.error("Failed to send SMS: %s", str(e))
        return {"error": str(e)}, 500




tools = [
    {
    "name": "send_sms",
    "description": "Sends a message to a specified phone number based on a property v_id from MongoDB. The function searches through all collections in a specified MongoDB database for a document matching the v_id and sends relevant details via SMS.",
    "parameters": {
        "type": "object",
        "properties": {
            "v_id": {
                "type": "string",
                "description": "The v_id of the property to find in the MongoDB database. The API will search MongoDB to find a matching document based on this v_id, searching across all collections."
            },
            "receiver_number": {
                "type": "string",
                "description": "The phone number to which the message will be sent via Twilio. This must be a valid phone number formatted according to Twilio's requirements."
            }
        },
        "required": ["v_id", "receiver_number"]
    },
    "runCmd": send_sms,
    "isDangerous": False,
    "functionType": "backend",
    "isLongRunningTool": False,
    "rerun": True,
    "rerunWithDifferentParameters": True
    }

]