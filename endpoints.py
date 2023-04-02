from flask_pymongo import pymongo
from flask import jsonify, request

conn_string = "mongodb+srv://afsalbaaqir:afsalbaaqir@kaar-training.fw4uwem.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_string)

db = client.get_database('firstdb')

user_collection = pymongo.collection.Collection(db, 'users')
print("MongoDB connected Successfully")


def api_endpoints(app):
    # hello world
    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({'message': 'Hello World!'})

    # get
    @app.route('/users', methods=['GET'])
    def get_users():
        try:
            users = user_collection.find({})
            users = list(users)
            data = [{'username': user['username'], 'email': user['email']}
                    for user in users]
            status = {
                "status": "200",
                "message": "Users fetched successfully"
            }
            return jsonify({'data': data, 'status': status})
        except Exception as e:
            status = {
                "status": "400",
                "message": str(e)
            }
            return jsonify({'data': [], 'status': status})

    # post
    @app.route('/users', methods=['POST'])
    def add_user():
        try:
            data = request.json
            print(data)
            res = user_collection.insert_one(data)
            print(res.inserted_id)
            status = {
                "status": "200",
                "message": "User added successfully"
            }
            return jsonify({'data': [], 'status': status})
        except Exception as e:
            status = {
                "status": "400",
                "message": str(e)
            }
            return jsonify({'data': [], 'status': status})

    # delete
    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        try:
            id = int(user_id)
            res = user_collection.delete_one({'user_id': id})
            print(res.deleted_count)
            status = {
                "status": "200",
                "message": "User deleted successfully"
            }
            return jsonify({'data': [], 'status': status})
        except Exception as e:
            status = {
                "status": "400",
                "message": str(e)
            }
            return jsonify({'data': [], 'status': status})

    # put
    @app.route('/update_user/<user_id>', methods=['PUT'])
    def update_user(user_id):
        try:
            update_user = request.json
            print(update_user)
            id = int(user_id)
            res = user_collection.update_one({"user_id": id}, {
                                             "$set": update_user['content']})
            print(res.modified_count)
            status = {
                "status": "200",
                "message": "User updated successfully"
            }
            return jsonify({'data': [], 'status': status})
        except Exception as e:
            status = {
                "status": "400",
                "message": str(e)
            }
            return jsonify({'data': [], 'status': status})
