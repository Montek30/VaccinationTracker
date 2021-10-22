import requests
from flask_login import UserMixin, login_user, logout_user, login_required
from flask import render_template, redirect, url_for, flash
from settings import db

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))

    def login(self, request_data):
        user = User.query.filter_by(email=request_data['email']).first()

        if not user or user.password != request_data['password']:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth_bp.login')) # if the user doesn't exist or password is wrong, reload the page

        login_user(user, remember=request_data['remember'])
        return redirect(url_for('main_bp.profile'))

    def signup(self, request_data):
        user = User.query.filter_by(email=request_data['email']).first()

        if user:
            flash("Email already exists!")
            return redirect(url_for('auth_bp.signup'))

        new_user = User(email=request_data['email'], name=request_data['name'], password=request_data['password'])

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth_bp.login'))

    @login_required
    def logout(self):
        logout_user()  
        return redirect(url_for('main_bp.home'))