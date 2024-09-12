from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.student_model import STUDENT
from ..models.prof_model import PROFESSOR
from ..models.course import CLASSES
from ..models.enrollment import ENROLLMENT


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
    if not professors:
        return "No professors found yet", 404
    return render_template('professors.html', professors=professors)


@bp.route('/prof_dash/stds')
@login_required
def stds():
    """retrieves a list of students"""
    students = STUDENT.query.with_entities(STUDENT.fullname).all()
    if not students:
        return "No students found yet", 404
    return render_template('students.html', students=students)


@bp.route('/prof_profile')
@login_required
def prof_profile():
    """route to professor profile"""
    professor = PROFESSOR.query.get_or_404(current_user.id)
    prof_class = CLASSES.query.filter_by(id=professor.id).all()
    return render_template('prof_profile.html', professor=professor, prof_class=prof_class)


@bp.route('/std_profile')
@login_required
def std_profile():
    """route to std profile"""
    student = STUDENT.query.get_or_404(current_user.id)
    enrollments = ENROLLMENT.query.filter_by(student_id=student.id)
    data = {}
    if enrollments:
        class_ids = [enrollment.class_id for enrollment in enrollments]
        classes = CLASSES.query.filter(CLASSES.id.in_(class_ids)).all()
        class_names = {cls.id: cls.name for cls in classes}
        enrolled_classes = [class_names.get(enrollment.class_id) for enrollment in enrollments]
        data['classes'] = enrolled_classes
    return render_template('std_profile.html', student=student, data=data)