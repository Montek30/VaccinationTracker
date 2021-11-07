from flask import render_template, request
from flask_login import login_required, current_user

def home():
	return render_template('index.html')

@login_required
def profile():
	return render_template('profile.html', name=current_user.name)

def faq():
	return render_template('faq.html')