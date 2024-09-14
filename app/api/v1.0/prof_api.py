from app.models.prof_model import PROFESSOR
from flask import request, Blueprint, jsonify, session, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user
from app.db_storage import db


bp = Blueprint('prof_apis', __name__)


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


