```python
from flask import jsonify, request
from app.api import bp
from app.models import User, Post, Comment

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    user = User()
    user.from_dict(data)
    user.save()
    response = jsonify(user.to_dict())
    response.status_code = 201
    return response

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    user.from_dict(data)
    user.save()
    return jsonify(user.to_dict())

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    user.delete()
    return '', 204

@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json() or {}
    post = Post()
    post.from_dict(data)
    post.save()
    response = jsonify(post.to_dict())
    response.status_code = 201
    return response

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())

@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json() or {}
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict())

@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    post.delete()
    return '', 204

@bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json() or {}
    comment = Comment()
    comment.from_dict(data)
    comment.save()
    response = jsonify(comment.to_dict())
    response.status_code = 201
    return response

@bp.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    return jsonify(Comment.query.get_or_404(id).to_dict())

@bp.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get_or_404(id)
    data = request.get_json() or {}
    comment.from_dict(data)
    comment.save()
    return jsonify(comment.to_dict())

@bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    comment.delete()
    return '', 204
```