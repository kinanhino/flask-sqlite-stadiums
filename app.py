from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stadiums.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    club_owner = db.Column(db.String(80), nullable=False)
    general_info = db.Column(db.Text, nullable=False)
    year_established = db.Column(db.Integer, nullable=False)
    maintenance_company = db.Column(db.String(80), nullable=True)



@app.route('/add_stadium', methods=['POST', 'GET'])
def add_stadium():
    if request.method == 'POST':
        new_stadium = Stadium(
            name=request.form.get('name'),
            image_url=request.form.get('image_url'),
            club_owner=request.form.get('club_owner'),
            general_info=request.form.get('general_info'),
            year_established=request.form.get('year_established'),
            maintenance_company=request.form.get('maintenance_company')
        )
        db.session.add(new_stadium)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_stadium.html')


@app.route('/')
def home():
    stadiums = Stadium.query.all()
    return render_template("home.html", stadiums=stadiums)


@app.route('/stadium/<stadium_id>')
def stadium_details(stadium_id):
    stadium = Stadium.query.get_or_404(stadium_id)
    return render_template('stadium_details.html', stadium=stadium)



if __name__ == "__main__":
    app.run(debug=True, port=5005)
