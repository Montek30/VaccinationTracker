import requests
import time
from flask_mail import Message
from flask import render_template, redirect, url_for, flash
from models.Models import VaccineBookingModel, VaccinesModel, UserModel, VaccineCentresModel, VaccineAvailabilityModel
from settings import db, mail
from models.User import User
from models.VaccineBooking import VaccineBooking
# from app import mail

class Vaccine():

    def booking(self, request_data):
        return_data = {}
        return_data['status'] = 1
        return_data['message'] = ''
        return_data['data'] = {'booking_id':-1}
        
        if request_data.get("user_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter User ID'
            return return_data
        
        if request_data.get("vaccine_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter Vaccine ID'
            return return_data

        if request_data.get("vaccine_centre_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter Vaccine Centre ID'
            return return_data

        result_1 = self.check_booking(request_data)
        if result_1['status'] == 0:
            return_data['status'] = 0
            return_data['message'] = result_1['message']
            return return_data
        elif result_1['exists'] == 1:
            return_data['status'] = 0
            return_data['message'] = "Booking Already Exists"
            return return_data


        u_obj = UserModel.query.filter_by(id=request_data['user_id']).first()
        v_obj = VaccinesModel.query.filter_by(id=request_data['vaccine_id']).first()
        vc_obj = VaccineCentresModel.query.filter_by(id=request_data['vaccine_centre_id']).first()
        va_obj = VaccineAvailabilityModel.query.filter_by(vaccine_centre_id=request_data['vaccine_centre_id'], vaccine_id=request_data['vaccine_id']).first()
        
        if u_obj is None or v_obj is None or vc_obj is None or va_obj is None:
            return_data['status'] = 0
            return_data['message'] = "Invalid Input"
            return return_data

        new_booking = VaccineBookingModel(user_id=request_data['user_id'], vaccine_id=request_data['vaccine_id']
            , vaccine_centre_id=request_data['vaccine_centre_id'], status=1, created=int(time.time()))

        db.session.add(new_booking)
        db.session.commit()
        

        va_obj.count -= 1
        db.session.commit()
        
        vcb_obj = VaccineBooking()
        vcb_detail = vcb_obj.detail({"booking_id":int(new_booking.id)})

        mail_data = {}
        mail_data['subject'] = "Vaccine Booking Confirmation"
        mail_data['body'] = "Congratulations "+vcb_detail['data']['user_name']+", you have successfully booked the "+vcb_detail['data']['vaccine_name']+" Vaccine at "+vcb_detail['data']['vaccine_centre_name']+". The address is "+vcb_detail['data']['address']
        mail_data['to'] = vcb_detail['data']['user_email']
        mail_data['from'] = "monteksingh30@gmail.com"

        user_obj = User()
        user_obj.send_mail(mail_data)
        
        return_data['data']['booking_id'] = new_booking.id
        return return_data


    def check_booking(self, request_data):
        return_data = {}
        return_data['status'] = 1
        return_data['message'] = ''
        return_data['exists'] = 0
        
        if request_data.get("user_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter User ID'
            return return_data
        
        if request_data.get("vaccine_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter Vaccine ID'
            return return_data

        if request_data.get("vaccine_centre_id", 0) == 0:
            return_data['status'] = 0
            return_data['message'] = 'Enter Vaccine Centre ID'
            return return_data

        res = VaccineBookingModel.query\
                    .add_columns(VaccineBookingModel.id.label('id'))\
                    .filter(VaccineBookingModel.user_id == request_data['user_id'])\
                    .filter(VaccineBookingModel.vaccine_id == request_data['vaccine_id'])\
                    .filter(VaccineBookingModel.vaccine_centre_id == request_data['vaccine_centre_id']).all()
        
        if len(res) > 0:
            return_data['exists'] = 1

        return return_data