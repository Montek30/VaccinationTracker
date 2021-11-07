import sys
from flask import render_template, redirect, url_for, request, abort

from models.VaccineCentres import VaccineCentres

def search():
	request_data = {}
	request_data['search_method'] = request.args.get('search_method', '')
	request_data['search_value'] = request.args.get('search_value', '')
	request_data['date'] = request.args.get('date', '')

	obj = VaccineCentres()
	data = obj.search(request_data)
	return data
