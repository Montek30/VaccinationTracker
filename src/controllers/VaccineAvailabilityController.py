from models.VaccineAvailability import VaccineAvailability
from flask import request

def get_data_by_pincode():
	request_data = {}
	request_data['pincode'] = request.args.get('pincode', -1)

	obj = VaccineAvailability()
	data = obj.get_data_by_pincode(request_data)
	return data