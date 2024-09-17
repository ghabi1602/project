from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.student_model import STUDENT
from app.models.prof_model import PROFESSOR
from app.models.course import CLASSES
from app.models.association import enrollment


# Initialize a blueprint
bp = Blueprint('routes', __name__, template_folder="templates", static_folder="static")


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
    professor = PROFESSOR.query.get_or_404(current_user.id)
    prof_classes = professor.classes
    return render_template('prof_dash.html', professor=professor, prof_classes=prof_classes)


@bp.route('/std_dash')
@login_required
def std_dash():
    """route to the student dashboard"""
    student = STUDENT.query.get_or_404(current_user.id)
    std_classes = student.classes
    return render_template('std_dash.html', student=student, std_classes=std_classes)


@bp.route('/std_dash/profs')
@login_required
def profs():
    """retrieves a list of professors"""
    professors = PROFESSOR.query.all()
    if not professors:
        return "No professors found yet", 404
    return render_template('professors.html', professors=professors)


@bp.route('/prof_dash/stds')
@login_required
def stds():
    """retrieves a list of students"""
    students = STUDENT.query.all()
    if not students:
        return "No students found yet", 404
    data = []
    for student in students:
        std = {}
        fullname = student.fullname
        email = student.email
        cls = student.classes
        std.update({
            'fullname': fullname,
            'email': email,
            'cls': cls
        })
        data.append(std)
    return render_template('students.html', data=data)


@bp.route('/classes')
@login_required
def classes():
    """route that retrieves a list of available classes"""
    user_type = "professor"
    students = STUDENT.query(STUDENT.id).all()
    if current_user.id in students:
        user_type = "student"

    all_classes = CLASSES.query.all()
    if all_classes:
        data = []
        for class_ in all_classes:
            class_data = {}
            name = class_.name
            professor = PROFESSOR.query.get(class_.professor_id)
            prof_name = professor.fullname if professor else "unknown"
            num_std = enrollment.query.filter_by(class_id=class_.id).count()
            class_data.update({
                'name': name,
                'prof_name': prof_name,
                'number_of_students': num_std
            })
            data.append(class_data)

        return render_template('classes.html', data=data, user_type=user_type)
    return render_template('No_class.html')


@bp.route('/signup')
def signup():
    """renders to the signup page"""
    return render_template('signup.html')