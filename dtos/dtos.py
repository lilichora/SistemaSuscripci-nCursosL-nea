class UserDTO:
    def __init__(self, user):
        self.id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.user_type = user.user_type

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "user_type": self.user_type
        }


class CourseDTO:
    def __init__(self, course):
        self.id = course.id
        self.name = course.name
        self.description = course.description
        self.state = course.state
        self.creator_id = course.creator_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "state": self.state,
            "creator_id": self.creator_id
        }


class SubscriptionDTO:
    def __init__(self, subscription):
        self.id = subscription.id
        self.user_id = subscription.user_id
        self.course_id = subscription.course_id
        self.subscription_date = subscription.subscription_date.isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "course_id": self.course_id,
            "subscription_date": self.subscription_date
        }
