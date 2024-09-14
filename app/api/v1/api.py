from app.models.prof_model import PROFESSOR
from app.models.student_model import STUDENT
from app.models.course import CLASSES
from flask import request, Blueprint, jsonify, session, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user
from app.db_storage import db


bp = Blueprint('apis', __name__)


@bp.route('/api/v1.0/professor/update', methods=["PUT"])
@login_required
def update_prof():
    """api that updates the profile of a professor"""
    professor = PROFESSOR.query.get_or_404(current_user.id)
    data = request.get_json()
    if data:
        if 'fullname' in data:
            professor.fullname = data['fullname']
        if 'username' in data:
            professor.username = data['username']
        if 'email' in data:
            professor.email = data['email']
        if 'age' in data:
            if not isinstance(data['age'], int):
                return jsonify({'message': 'Age must be a number'}), 400
            professor.age = data['age']
        if 'specialization' in data:
            professor.Specialization = data['Specialization']
        if 'expert_at' in data:
            professor.expert_at = data['expert_at']
        if 'years_of_experience' in data:
            professor.years_of_experience = data['years_of_experience']

        try:
            db.session.commit()
            return jsonify({'message': 'Profile updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error updating profile', 'error': str(e)}), 500
    return jsonify({'message': 'No data provided'}), 400


@bp.route('/api/v1.0/professor/delete', methods=['DELETE'])
@login_required
def delete_prof():
    """api that deletes a professor"""
    professor = PROFESSOR.query.filter_by(id=current_user.id).first_or_404()
    try:
        db.session.delete(professor)
        db.session.commit()
        logout_user()
        flash('Your account has been deleted successfully.', 'success')
        return redirect(url_for('routes.home'))
    except Exception as e:
        db.session.rollback()
        flash('Error deleting account', 'error')
        return jsonify({'message': 'Error deleting professor', 'error': str(e)}), 500


@bp.route('/api/v1.0/student/update', methods=["PUT"])
@login_required
def update_std():
    """api that updates the profile of a student"""
    student = STUDENT.query.get_or_404(current_user.id)
    data = request.get_json()
    if data:
        if 'fullname' in data:
            student.fullname = data['fullname']
        if 'username' in data:
            student.username = data['username']
        if 'email' in data:
            student.email = data['email']
        if 'age' in data:
            if not isinstance(data['age'], int):
                return jsonify({'message': 'Age must be a number'}), 400
            student.age = data['age']
        if 'highest_school_level' in data:
            student.highest_school_level = data['highest_school_level']
        if 'field_of_studies' in data:
            student.field_of_studies = data['field_of_studies']
        if 'interested_at' in data:
            student.interested_at = data['interested_at']

        try:
            db.session.commit()
            return jsonify({'message': 'Profile updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error updating profile', 'error': str(e)}), 500
    return jsonify({'message': 'No data provided'}), 400


@bp.route('/api/v1.0/student/delete', methods=['DELETE'])
@login_required
def delete_std():
    """api that deletes a student"""
    student = STUDENT.query.filter_by(id=current_user.id).first_or_404()
    try:
        db.session.delete(student)
        db.session.commit()
        logout_user()
        flash('Your account has been deleted successfully.', 'success')
        return redirect(url_for('routes.home'))
    except Exception as e:
        db.session.rollback()
        flash('Error deleting account', 'error')
        return jsonify({'message': 'Error deleting student', 'error': str(e)}), 500


@bp.route('/api/professor/class', methods=['POST', 'GET'])
@login_required
def create_class():
    """API to create a new class"""
    data = request.get_json()  # Retrieve JSON data from the request body

    if not data or not all(key in data for key in ('name', 'field', 'maximum_number_of_students')):
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        new_class = CLASSES(
            name=data['name'],
            field=data['field'],
            maximum_number_of_students=data['maximum_number_of_students'],
            professor_id=current_user.id
        )

        db.session.add(new_class)
        db.session.commit()

        return jsonify({'message': 'Class created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating class', 'error': str(e)}), 500


@bp.route('/classes/<int:class_id>', methods=["DELETE"])
@login_required
def delete_class(class_id):
    """api that deletes a class"""
    cls = CLASSES.query.filter_by(id=class_id)
    try:
        db.session.delete(cls)
        db.session.commit()
        return jsonify({'message': 'class deleted successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        flash('error class deletion', 'error')
        return jsonify({'message': 'error class deletion', 'error': str(e)}), 500
