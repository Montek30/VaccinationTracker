import requests
from flask_login import UserMixin, login_user, logout_user, login_required
from flask import render_template, redirect, url_for, flash
from flask_mail import Message
from settings import db, mail
from constants import USER_ROLE
from models.Models import UserModel

class User():

    # id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    # email = db.Column(db.String(20), unique=True)
    # password = db.Column(db.String(20))
    # name = db.Column(db.String(20))
    # role = db.Column(db.Integer)

    def login(self, request_data):
        user = UserModel.query.filter_by(email=request_data['email']).first()

        if not user or user.password != request_data['password']:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth_bp.login')) # if the user doesn't exist or password is wrong, reload the page

        login_user(user, remember=request_data['remember'])
        return redirect(url_for('main_bp.profile'))

    def signup(self, request_data):
        user = UserModel.query.filter_by(email=request_data['email']).first()

        if user:
            flash("Email already exists!")
            return redirect(url_for('auth_bp.signup'))


        if request_data.get('role',0) == 0:
            request_data['role'] = USER_ROLE

        new_user = UserModel(email=request_data['email'], name=request_data['name'], password=request_data['password'], role=request_data['role'])

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth_bp.login'))

    @login_required
    def logout(self):
        logout_user()  
        return redirect(url_for('main_bp.home'))

    def send_mail(self, request_data):
        msg = Message(request_data['subject'], sender = request_data['from'], recipients = [request_data['to']])
        msg.body = request_data['body']
        mail.send(msg)