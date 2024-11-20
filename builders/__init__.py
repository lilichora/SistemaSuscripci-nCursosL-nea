from models import User, Course, Subscription

class UserBuilder:
    def __init__(self):
        self.user = User()

    def set_first_name(self, first_name):
        self.user.first_name = first_name
        return self

    def set_last_name(self, last_name):
        self.user.last_name = last_name
        return self

    def set_email(self, email):
        self.user.email = email
        return self

    def set_password(self, password):
        self.user.password = password
        return self

    def set_user_type(self, user_type):
        self.user.user_type = user_type
        return self

    def build(self):
        return self.user

class CourseBuilder:
    def __init__(self):
        self.course = Course()

    def set_name(self, name):
        self.course.name = name
        return self

    def set_description(self, description):
        self.course.description = description
        return self

    def set_status(self, status):
        self.course.status = status
        return self

    def set_creator_id(self, creator_id):
        self.course.creator_id = creator_id
        return self

    def build(self):
        return self.course

class SubscriptionBuilder:
    def __init__(self):
        self.subscription = Subscription()

    def set_user_id(self, user_id):
        self.subscription.user_id = user_id
        return self

    def set_course_id(self, course_id):
        self.subscription.course_id = course_id
        return self

    def build(self):
        return self.subscription