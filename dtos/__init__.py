from marshmallow import Schema, fields

class UserDTO(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    user_type = fields.Str(required=True)

class CourseDTO(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)
    creator_id = fields.Int(required=True)

class SubscriptionDTO(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    course_id = fields.Int(required=True)