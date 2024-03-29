from flask import Flask
from flask_migrate import Migrate
from utilities import db, configure_routes

app = Flask(__name__)
app.secret_key = 'fjlhfewfhewkjfhwefewfkjbvdcsakdlwkjwodcvckxk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stadiums.db'

db.init_app(app)
migrate = Migrate(app, db)


configure_routes(app)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
