from flask import render_template, request, redirect,flash,session,url_for
from models import Stadium,User, Reviews
from werkzeug.security import check_password_hash
from utilities import db

def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            if password == user.password:
                session['username'] = username
                session['is_admin'] = user.is_admin == 1
                return redirect(url_for('home'))
            else:
                flash("You've entered incorrect password")
                return redirect(url_for('login'))
        else:
            flash("Username does not exist. Try Signing Up First...")
            return redirect(url_for('login'))



def register():
    if request.method == 'POST':

        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if password != re_password:
            flash("Passwords must match!")
        else:
            username = request.form.get('username')
            user = User.query.filter_by(username=username).first()
            print(user)
            if user:
                flash("Username already Exists!")
            else:
                new_user = User(
                    first_name=request.form.get('firstname'),
                    last_name=request.form.get('lastname'),
                    username=username,
                    password=password,
                    #is_admin=1
                )
                db.session.add(new_user)
                db.session.commit()
                flash("User Successfully Signed Up")
                return redirect(url_for('login'))

    return render_template('register.html')


def add_stadium():
    if request.method == 'POST':
        new_stadium = Stadium(
            name=request.form.get('name'),
            image_url=request.form.get('image_url'),
            capacity=request.form.get('capacity'),
            general_info=request.form.get('general_info'),
            year_established=request.form.get('year_established'),
            maintenance_company=request.form.get('maintenance_company'),
            dimensions = request.form.get('dimensions')
        )
        db.session.add(new_stadium)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_stadium.html')


def home():
    # db.session.query(User).delete()  # Delete all entries in User table
    # db.session.commit()
    stadiums = Stadium.query.all()
    return render_template("home.html", stadiums=stadiums)


def stadium_details(stadium_id):
    username = session["username"] if "username" in session else None

    if request.method == 'GET':
        stadium = Stadium.query.get_or_404(stadium_id)
        print(stadium)
        reviews = get_reviews_for_stadium(stadium_id)
        print(reviews)
        return render_template('stadium_details.html', stadium=stadium,reviews=reviews,user_logged=username)
    else:
        review_text = request.form.get("review-text")
        rating = request.form.get("rating")
        print(rating)
        if rating:
            new_review = Reviews(
                stadium_id=int(stadium_id),
                user_submitted=username,
                review_text=review_text,
                review_stars=int(rating)
            )
            print(stadium_id,username,review_text,rating)
            print(type(stadium_id),type(username),type(review_text),type(rating))

            db.session.add(new_review)
            db.session.commit()
        else:
            flash("You Must Specify Stars Number")
        
        return redirect(url_for('stadium_details', stadium_id=stadium_id))

        
def get_reviews_for_stadium(stadium_id):
    reviews = Reviews.query.filter_by(stadium_id=stadium_id).all()
    return reviews

def logout():
    session.clear()
    return redirect(url_for('login'))