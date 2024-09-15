from app.db_storage import db
from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from app.models.prof_model import PROFESSOR
from app.models.student_model import STUDENT
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

bp = Blueprint('auth', __name__, template_folder="templates", static_folder="static")

#function that handles professor registration
@bp.route('/register/prof', methods=["GET", "POST"])
def register_prof():
    """prof registration function"""
    if request.method == "POST":
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        age = request.form.get('age')
        specialization = request.form.get('specialization')
        expert_at = request.form.get('expert_at')
        yoe = request.form.get('years_of_experience')

        if PROFESSOR.query.filter_by(email=email).first():
            flash('Email address already in use :(')
            return redirect(url_for('register_prof'))

        hashed_password = generate_password_hash(password)

        new_prof = PROFESSOR(fullname=fullname,
                             username=username,
                             email=email,
                             password=hashed_password,
                             gender=gender,
                             age=age,
                             specialization=specialization,
                             expert_at=expert_at,
                             years_of_experience=yoe)


        db.session.add(new_prof)
        db.session.commit()
        flash('Successful Registration :)')
        return redirect(url_for('login.prof'))

    return render_template('register_prof.html')


# function that handles student registration
@bp.route('/register/student', methods=["GET", "POST"])
def register_std():
    """student registration function"""
    if request.method == "POST":
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        age = request.form.get('age')
        highest_school_level = request.form.get('highest_school_level')
        field_of_studies = request.form.get('field_of_studies')
        interested_at = request.form.get('interested_at')

        if STUDENT.query.filter_by(email=email).first():
            flash('Email address already in use :(')
            return redirect(url_for('register_std'))

        hashed_password = generate_password_hash(password)

        new_student = STUDENT(fullname=fullname,
                              username=username,
                              email=email,
                              password=hashed_password,
                              age=age,
                              highest_school_level=highest_school_level,
                              field_of_studies=field_of_studies,
                              interested_at=interested_at)


        db.session.add(new_student)
        db.session.commit()
        flash('Successful Registration :)')
        return redirect(url_for('login_std'))

    return render_template('register_std.html')


# function that handles the login
@bp.route('/login', methods=["GET", "POST"])
def login():
    """a function that handles the login procedure"""
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        std = STUDENT.query.filter_by(email=email).first()
        if std:
            if check_password_hash(std.password, password):
                login_user(std)
                flash('Login successful :)')
                current_user.is_online = True
                db.session.commit()
                session['user_type'] = 'std'
                return redirect(url_for('routes.std_dash'))
            else:
                flash('Password is incorrect :(')
                return redirect(url_for('login'))

        prof = PROFESSOR.query.filter_by(email=email).first()
        if prof:
            if check_password_hash(prof.password, password):
                login_user(prof)
                flash('Login successful :)')
                current_user.is_online = True
                db.session.commit()
                session['user_type'] = 'prof'
                return redirect(url_for('routes.prof_dash'))
            else:
                flash('Password is incorrect :(')
                return redirect(url_for('login'))

        flash('Wrong Email :(')
        return redirect(url_for('login'))

    return render_template('login.html')


@bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    """a route that handles a user logout"""
    current_user.is_online = False
    db.session.commit()
    logout_user()
    flash('Logout successful')
    return redirect(url_for('routes.home'))