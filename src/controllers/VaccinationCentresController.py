import sys
from flask import render_template, redirect, url_for, request, abort

from models.VaccineCentres import VaccineCentres

def search():
	request_data = request.get_json()
	obj = VaccineCentres()
	data = obj.search(request_data)
	return data
