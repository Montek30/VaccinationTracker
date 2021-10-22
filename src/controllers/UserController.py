import sys
from flask import render_template, redirect, url_for, request, abort

from models.User import User

def login():
	if request.method == "GET":
		return render_template('login.html')
	elif  request.method == "POST":
		request_data = {}
		request_data['email'] = request.form.get('email')
		request_data['password'] = request.form.get('password')
		request_data['remember'] = True if request.form.get('remember') else False
		obj = User()
		data = obj.login(request_data)
		return data

def signup():
	if request.method == "GET":
		return render_template('signup.html')
	elif  request.method == "POST":
		request_data = {}
		request_data['email'] = request.form.get('email')
		request_data['name'] = request.form.get('name')
		request_data['password'] = request.form.get('password')
		obj = User()
		data = obj.signup(request_data)
		return data

def logout():
	obj = User()
	data = obj.logout()
	return data
