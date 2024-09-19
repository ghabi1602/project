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
    all_classes = CLASSES.query.all()
    data = []
    expertise = []
    if all_classes:
        for class_ in all_classes:
            class_data = {}
            name = class_.name
            field = class_.field
            max_std = class_.maximum_number_of_students
            professor = PROFESSOR.query.get(class_.professor_id)
            prof_name = professor.fullname if professor else "unknown"
            num_std = len(class_.students)
            class_data.update({
                'name': name,
                'prof_name': prof_name,
                'field': field,
                'number_of_students': num_std,
                'max_std': max_std
            })
            data.append(class_data)
        expertise = professor.expert_at.split()
    return render_template('prof_dash.html', professor=professor, data=data, expertise=expertise)


@bp.route('/std_dash')
@login_required
def std_dash():
    """route to the student dashboard"""
    student = STUDENT.query.get_or_404(current_user.id)
    all_classes = CLASSES.query.all()
    data = []
    if all_classes:
        for class_ in all_classes:
            class_data = {}
            name = class_.name
            field = class_.field
            max_std = class_.maximum_number_of_students
            professor = PROFESSOR.query.get(class_.professor_id)
            prof_name = professor.fullname if professor else "unknown"
            num_std = len(class_.students)
            class_data.update({
                'name': name,
                'prof_name': prof_name,
                'field': field,
                'number_of_students': num_std,
                'max_std': max_std,
                'id': class_.id
            })
            data.append(class_data)
        interest = student.interested_at.split()
        classes = [cls.name for cls in student.classes]
    return render_template('std_dash.html', student=student, data=data, interest=interest, classes=classes)


@bp.route('/std_dash/profs')
@login_required
def profs():
    """retrieves a list of professors"""
    professors = PROFESSOR.query.all()
    if not professors:
        return "No professors found yet", 404
    return render_template('profs.html', professors=professors)


@bp.route('/prof_dash/stds')
@login_required
def stds():
    """retrieves a list of students"""
    students = STUDENT.query.all()
    if not students:
        return "No students found yet", 404
    return render_template('stds.html', students=students)


"""@bp.route('/classes')
@login_required
def classes():
    route that retrieves a list of available classes
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
"""


@bp.route('/signup')
def signup():
    """renders to the signup page"""
    return render_template('signup.html')


@bp.route('/professor/create_class')
@login_required
def create_class():
    return render_template('addClass.html')