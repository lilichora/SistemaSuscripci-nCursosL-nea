from flask import Flask
from flask_migrate import Migrate
from models import db
from services import app as services_app

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)  # Enable Flask-Migrate

app.register_blueprint(services_app)

if __name__ == '__main__':
    app.run(debug=True)
