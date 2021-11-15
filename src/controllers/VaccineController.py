from flask import render_template, request
from models.Vaccine import Vaccine

def booking():
	request_data = {}
	request_data['user_id'] = int(request.form.get('user_id',0))
	request_data['vaccine_id'] = int(request.form.get('vaccine_id',0))
	request_data['vaccine_centre_id'] = int(request.form.get('vaccine_centre_id',0))
	
	obj = Vaccine()
	data = obj.booking(request_data)
	return data

def check_booking():
	request_data = {}
	request_data['user_id'] = int(request.form.get('user_id',0))
	request_data['vaccine_id'] = int(request.form.get('vaccine_id',0))
	request_data['vaccine_centre_id'] = int(request.form.get('vaccine_centre_id',0))
	
	obj = Vaccine()
	data = obj.check_booking(request_data)
	return data