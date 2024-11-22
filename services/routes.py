from flask import Blueprint, request, jsonify
from models import db, User, Course, Subscription
from dtos.dtos import UserDTO, CourseDTO, SubscriptionDTO
from datetime import datetime

app = Blueprint('routes', __name__)

# User Management Endpoints
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password'],
        user_type=data['user_type']
    )
    db.session.add(new_user)
    db.session.commit()

    user_dto = UserDTO(new_user)
    return jsonify(user_dto.to_dict()), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.user_type = data.get('user_type', user.user_type)
    db.session.commit()

    user_dto = UserDTO(user)
    return jsonify(user_dto.to_dict()), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_dto = UserDTO(user)
    return jsonify(user_dto.to_dict()), 200


# Course Management Endpoints
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    new_course = Course(
        name=data['name'],
        description=data['description'],
        state=data.get('state', 'en_construccion'),
        creator_id=data['creator_id']
    )
    db.session.add(new_course)
    db.session.commit()

    course_dto = CourseDTO(new_course)
    return jsonify(course_dto.to_dict()), 201


@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.json
    course.name = data.get('name', course.name)
    course.description = data.get('description', course.description)
    course.state = data.get('state', course.state)
    db.session.commit()

    course_dto = CourseDTO(course)
    return jsonify(course_dto.to_dict()), 200


@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully"}), 200


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    course_dto = CourseDTO(course)
    return jsonify(course_dto.to_dict()), 200


# Subscription Management Endpoints
@app.route('/subscriptions', methods=['POST'])
def subscribe():
    data = request.json
    new_subscription = Subscription(
        user_id=data['user_id'],
        course_id=data['course_id'],
        subscription_date=datetime.utcnow()
    )
    db.session.add(new_subscription)
    db.session.commit()

    subscription_dto = SubscriptionDTO(new_subscription)
    return jsonify(subscription_dto.to_dict()), 201


@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def cancel_subscription(subscription_id):
    subscription = Subscription.query.get_or_404(subscription_id)
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({"message": "Subscription canceled successfully"}), 200


@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    subscription = Subscription.query.get_or_404(subscription_id)
    subscription_dto = SubscriptionDTO(subscription)
    return jsonify(subscription_dto.to_dict()), 200


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API"}), 200
