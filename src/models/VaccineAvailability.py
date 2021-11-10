from flask import render_template, redirect, url_for, flash
from settings import db

class VaccineAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    vaccine_centre_id = db.Column(db.Integer)
    vaccine_id = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def get_data_by_pincode(self, request_data):
        return_data = {}
        
        return request_data