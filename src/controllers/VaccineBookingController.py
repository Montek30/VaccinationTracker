from flask import request
from models.VaccineBooking import VaccineBooking

def detail():
	request_data = {}
	request_data['booking_id'] = int(request.args.get('booking_id', -1))
	
	obj = VaccineBooking()
	data = obj.detail(request_data)
	return data