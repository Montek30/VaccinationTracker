from models.Models import VaccinesModel, VaccineCentresModel, VaccineBookingModel, UserModel
from settings import db


class VaccineBooking():

    def detail(self, request_data):
        return_data = {}
        return_data['status'] = 1
        return_data['message'] = ''
        return_data['data'] = {}

        if int(request_data.get("booking_id", -1)) == -1:
            return_data['status'] = 0
            return_data['message'] = 'Empty Booking Id'
            return return_data

        li = VaccineBookingModel.query\
                    .join(VaccinesModel, VaccinesModel.id==VaccineBookingModel.vaccine_id)\
                    .join(VaccineCentresModel, VaccineCentresModel.id==VaccineBookingModel.vaccine_centre_id)\
                    .join(UserModel, UserModel.id==VaccineBookingModel.user_id)\
                    .add_columns(VaccinesModel.name.label('vaccine_name')
                        , VaccineCentresModel.name.label('vaccine_centre_name')
                        , VaccineCentresModel.address.label('address')
                        , VaccineCentresModel.postcode
                        , UserModel.name.label('user_name')
                        , UserModel.email.label('user_email'))\
                    .filter(VaccineBookingModel.id == request_data['booking_id']).first()

        if li is None:
            return_data['status'] = 0
            return_data['message'] = 'Invalid Booking Id!!!'
            return return_data

        return_data['data']['user_name'] = li.user_name
        return_data['data']['user_email'] = li.user_email
        return_data['data']['vaccine_name'] = li.vaccine_name
        return_data['data']['vaccine_centre_name'] = li.vaccine_centre_name
        return_data['data']['address'] = li.address
        return_data['data']['postcode'] = li.postcode

        return return_data