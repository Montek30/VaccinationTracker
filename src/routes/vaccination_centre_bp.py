from flask import Blueprint
from controllers.VaccinationCentresController import search

vaccination_centre_bp = Blueprint('vaccination_centre_bp', __name__)

vaccination_centre_bp.route('/search', methods=['GET'])(search)