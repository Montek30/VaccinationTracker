from flask import Blueprint
from controllers.VaccineAvailabilityController import get_data_by_pincode

vaccine_availability_bp = Blueprint('vaccine_availability_bp', __name__)

vaccine_availability_bp.route('/get_data_by_pincode', methods=['GET'])(get_data_by_pincode)