
from app import app
from models import db, User, Course

# Insert initial data
with app.app_context():
    admin = User(
        first_name="Admin",
        last_name="User",
        email="admin@admin.com",
        password="12345678",
        user_type="admin"
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created.")
