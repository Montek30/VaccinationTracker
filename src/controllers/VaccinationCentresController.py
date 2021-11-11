import sys
from flask import render_template, redirect, url_for, request, abort

from models.VaccineCentres import VaccineCentres

def search():
	request_data = {}
	request_data['search_method'] = request.args.get('search_method', '')
	request_data['search_value'] = request.args.get('search_value', '')
	request_data['version'] = int(request.args.get('version', 1))
	
	obj = VaccineCentres()
	
	if request_data['version'] == 1:
		request_data['date'] = request.args.get('date', '')
		data = obj.search(request_data)
	else:
		data = obj.search_v2(request_data)

	return data
