from flask import Blueprint
from controllers.VaccineController import booking, check_booking

vaccine_bp = Blueprint('vaccine_bp', __name__)

vaccine_bp.route('/booking', methods=['POST'])(booking)
vaccine_bp.route('/check_booking', methods=['GET'])(check_booking)