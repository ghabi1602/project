from flask import Blueprint, render_template
from flask_login import login_required
from ..models.student_model import STUDENT
from ..models.prof_model import PROFESSOR


# Initialize a blueprint
bp = Blueprint('routes', __name__)


@bp.route('/', strict_slashes=False)
def home():
    """route to the Landing page"""
    return render_template('home.html')


@bp.route('/about')
def about():
    """route to the about page"""
    return render_template('about.html')


@bp.route('/prof_dash')
@login_required
def prof_dash():
    """route to the professor dashboard"""
    return render_template('prof_dash.html')


@bp.route('/std_dash')
@login_required
def std_dash():
    """route to the student dashboard"""
    return render_template('std_dash.html')


@bp.route('/std_dash/profs')
@login_required
def profs():
    """retrieves a list of professors"""
    professors = PROFESSOR.query.with_entities(PROFESSOR.fullname).all()
    return render_template('professors.html', professors=professors)


@bp.route('/prof_dash/stds')
@login_required
def stds():
    """retrieves a list of students"""
    students = STUDENT.query.with_entities(STUDENT.fullname).all()
    return render_template('students.html', students=students)


@