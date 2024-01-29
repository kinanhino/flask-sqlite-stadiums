from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///stadiums.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():

    return render_template("home.html", stadiums=[])

if __name__ == "__main__":
    app.run(Debug=True, port=5005)