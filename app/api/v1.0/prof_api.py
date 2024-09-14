from app.models.prof_model import PROFESSOR
from flask import request, Blueprint
from flask_login import login_required


bp = Blueprint('prof_apis', __name__)


@bp.route('tvs/professor/v1.0/<int:prof_id>')
@login_required
def update_prof(prof_id):
    """api that updates the profile of a professor"""
