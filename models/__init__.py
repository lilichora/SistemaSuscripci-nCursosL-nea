
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User Model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'admin', 'creator', 'consumer'

    # Relationship: A creator can have many courses
    courses = db.relationship('Course', backref='creator', lazy=True)

# Course Model
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    state = db.Column(db.String(20), nullable=False, default='en_construccion')  # 'en_construccion', 'activo', 'inactivo'
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    subscriptions = db.relationship('Subscription', backref='course', lazy=True)

# Subscription Model
class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)  # Foreign key to Course
    subscription_date = db.Column(db.DateTime, nullable=False)
