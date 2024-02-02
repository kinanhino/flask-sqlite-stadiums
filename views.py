from flask import render_template, request, redirect, flash, session, url_for
from models import Stadium, User, Reviews
from utilities import db
import hashlib


def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            if verify_password(user.password, password):
                session['username'] = username
                session['is_admin'] = user.is_admin == 1
                return redirect(url_for('home'))
            else:
                flash("You've entered incorrect password", "error")
                return redirect(url_for('login'))
        else:
            flash("Username does not exist. Try Signing Up First...", "error")
            return redirect(url_for('login'))


def register():
    if request.method == 'POST':

        password = request.form.get('password')
        re_password = request.form.get('re-password')
        if check_password(password):

            if password != re_password:
                flash("Passwords must match!", "error")

            else:
                username = request.form.get('username')
                if check_username(username):
                    user = User.query.filter_by(username=username).first()
                    print(user)
                    if user:
                        flash("Username already Exists!", "error")
                    else:
                        new_user = User(
                            first_name=request.form.get('firstname'),
                            last_name=request.form.get('lastname'),
                            username=username,
                            password=hash_password(password),
                            # is_admin=1
                        )
                        db.session.add(new_user)
                        db.session.commit()
                        flash("User Successfully Signed Up", "info")
                        return redirect(url_for('login'))
                else:
                    flash("Username must be Alphanumeric only with atleast 3 chars!", "error")
        else:
            flash("Password Must Have", "error")
            flash("At least 8 characters long", "error")
            flash("Contains at least one digit", "error")
            flash("Contains at least one special character", "error")

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
            dimensions=request.form.get('dimensions')
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
        return render_template('stadium_details.html', stadium=stadium, reviews=reviews, user_logged=username)
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
            print(stadium_id, username, review_text, rating)
            print(type(stadium_id), type(username), type(review_text), type(rating))

            db.session.add(new_review)
            db.session.commit()
        else:
            flash("You Must Specify Stars Number", "error")

        return redirect(url_for('stadium_details', stadium_id=stadium_id))


def get_reviews_for_stadium(stadium_id):
    reviews = Reviews.query.filter_by(stadium_id=stadium_id).all()
    return reviews


def logout():
    session.clear()
    return redirect(url_for('login'))


def delete_stadium(stadium_id):
    if request.method == 'POST':
        stadium = Stadium.query.filter(Stadium.id == int(stadium_id)).first()
        if stadium:
            db.session.delete(stadium)
            db.session.commit()
    else:
        flash('trying to access with the wrong method!', 'error')
    return redirect(url_for('home'))

def edit_stadium(stadium_id):
    if request.method == 'POST':
        stadium = Stadium.query.get_or_404(stadium_id)
        stadium.name = request.form.get('name')
        stadium.image_url=request.form.get('image_url')
        stadium.capacity=request.form.get('capacity')
        stadium.general_info=request.form.get('general_info')
        stadium.year_established=request.form.get('year_established')
        stadium.maintenance_company=request.form.get('maintenance_company')
        stadium.dimensions=request.form.get('dimensions')
        
        db.session.commit()
        return redirect(url_for('home'))
    else:
        stadium = Stadium.query.filter(Stadium.id == int(stadium_id)).first()

        stadium.capacity = make_int(stadium.capacity)
        stadium.year_established = make_int(stadium.year_established)
        return render_template('edit_stadium.html', stadium=stadium)

def make_int(text):
    if isinstance(text, str):
        if ',' in text:
            return int(text.replace(',', ''))
        else:
            return int(text)
    else:
        return text

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(stored_password_hash, user_password):
    return stored_password_hash == hash_password(user_password)


def check_username(username):
    return len(username) >= 3 and username.isalnum()


def check_password(password):
    return (len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(not char.isalnum() for char in password))


