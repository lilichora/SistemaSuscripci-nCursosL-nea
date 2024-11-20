from flask import Blueprint, request, jsonify
from models import db, User, Course, Subscription
from dtos import UserDTO, CourseDTO, SubscriptionDTO
from builders import UserBuilder, CourseBuilder, SubscriptionBuilder

app = Blueprint('services', __name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_builder = UserBuilder().set_first_name(data['first_name']).set_last_name(data['last_name']).set_email(data['email']).set_password(data['password']).set_user_type(data['user_type'])
    user = user_builder.build()
    db.session.add(user)
    db.session.commit()
    return UserDTO().jsonify(user), 201

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    course_builder = CourseBuilder().set_name(data['name']).set_description(data['description']).set_status(data['status']).set_creator_id(data['creator_id'])
    course = course_builder.build()
    db.session.add(course)
    db.session.commit()
    return CourseDTO().jsonify(course), 201

@app.route('/subscriptions', methods=['POST'])
def subscribe_course():
    data = request.get_json()
    subscription_builder = SubscriptionBuilder().set_user_id(data['user_id']).set_course_id(data['course_id'])
    subscription = subscription_builder.build()
    db.session.add(subscription)
    db.session.commit()
    return SubscriptionDTO().jsonify(subscription), 201


