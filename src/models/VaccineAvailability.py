from flask import render_template, redirect, url_for, flash
from models.Models import VaccinesModel, VaccineCentresModel, VaccineAvailabilityModel
# from models.VaccineCentres import VaccineCentres
from settings import db


class VaccineAvailability():
    # id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    # vaccine_centre_id = db.Column(db.Integer, db.ForeignKey('VaccineCentres.id'), nullable=False)
    # vaccine_id = db.Column(db.Integer, db.ForeignKey('Vaccines.id'), nullable=False)
    # count = db.Column(db.Integer)

    def get_data_by_pincode(self, request_data):
        return_data = {}
        return_data['status'] = 1
        return_data['message'] = ''
        return_data['data'] = []

        if request_data.get("pincode", "") == "":
            return_data['status'] = 0
            return_data['message'] = 'Enter Pincode'
            return return_data

        li = VaccineAvailabilityModel.query\
                    .join(VaccinesModel, VaccinesModel.id==VaccineAvailabilityModel.vaccine_id)\
                    .join(VaccineCentresModel, VaccineCentresModel.id==VaccineAvailabilityModel.vaccine_centre_id)\
                    .add_columns(VaccinesModel.id.label('vaccine_id'), VaccinesModel.name.label('vaccine_name')
                        , VaccineCentresModel.id.label('vaccine_centre_id'), VaccineCentresModel.name.label('vaccine_centre_name')
                        , VaccineCentresModel.address.label('address'), VaccineCentresModel.postcode, VaccineAvailabilityModel.count)\
                    .filter(VaccineAvailabilityModel.count > 0)\
                    .filter(VaccinesModel.status == 1)\
                    .filter(VaccineCentresModel.status == 1)\
                    .filter(VaccineCentresModel.postcode == request_data['pincode']).all()

        for item in li:
            data = {}
            data['vaccine_id'] = item.vaccine_id
            data['vaccine_name'] = item.vaccine_name
            data['vaccine_centre_id'] = item.vaccine_centre_id
            data['vaccine_centre_name'] = item.vaccine_centre_name
            data['address'] = item.address
            data['postcode'] = item.postcode
            data['count'] = item.count
            return_data['data'].append(data)
        
        return return_data