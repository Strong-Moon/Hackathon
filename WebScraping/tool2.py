from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

# Initialize MongoDB connection
client = MongoClient('mongodb+srv://lagnarokthor:berkaypehlivan2001@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1')
db = client['user_database']
collectionUser = db['user_info']  # Collection name for user information

@app.route('/get-users', methods=['GET'])
def get_users():
    try:
        # Query user data from MongoDB collection
        users_data = collectionUser.find()

        # Convert MongoDB cursor to JSON using bson.json_util.dumps
        json_users_data = dumps(users_data)

        # Return the JSON data as a response
        return jsonify({'users': json_users_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
