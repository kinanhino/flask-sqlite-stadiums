from utilities import db

class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    general_info = db.Column(db.Text, nullable=False)
    year_established = db.Column(db.Integer, nullable=False)
    maintenance_company = db.Column(db.String(50), nullable=True)
    dimensions = db.Column(db.String(50), nullable=False)


class User(db.Model):
    username = db.Column(db.String(50), primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_logged = db.Column(db.Integer, nullable=False, default=0)
    is_admin = db.Column(db.Integer, nullable=False, default=0)


class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stadium_id = db.Column(db.Integer,nullable=False)
    user_submitted = db.Column(db.String(50), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    review_stars = db.Column(db.Integer,nullable=False, default=1)

