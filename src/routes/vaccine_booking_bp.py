from flask import Blueprint
from controllers.VaccineBookingController import detail

vaccine_booking_bp = Blueprint('vaccine_booking_bp', __name__)

vaccine_booking_bp.route('/detail', methods=['GET'])(detail)