from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB connection
mongodb_uri = "mongodb+srv://lagnarokthor:berkaypehlivan2001@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1"
client = MongoClient(mongodb_uri)
db = client['house_info']
collection_sale = db['for_sale']
collection_rent = db['for_rent']  # New collection for rentals

@app.route('/get-sale', methods=['GET'])
def get_sale_data():
    try:
        # Querying data from MongoDB collection for sale
        data = collection_sale.find()

        # Convert MongoDB cursor to JSON
        json_data = dumps(data)

        return jsonify({'data': json_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-rent', methods=['GET'])
def get_rental_data():
    try:
        # Querying data from MongoDB collection for rent
        data = collection_rent.find()

        # Convert MongoDB cursor to JSON
        json_data = dumps(data)

        return jsonify({'data': json_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
