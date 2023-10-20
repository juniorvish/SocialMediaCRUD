from flask import request, jsonify
from app import app
from app.models import User, Post, Comment

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user:
        data = request.get_json()
        user.update(**data)
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        user.delete()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# Similar routes can be created for Post and Comment models.