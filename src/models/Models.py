from flask_login import UserMixin
from settings import db


class UserModel(UserMixin, db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
	email = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(20))
	name = db.Column(db.String(20))
	role = db.Column(db.Integer)


class VaccinesModel(db.Model):
    __tablename__ = 'vaccines'
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(20))
    status = db.Column(db.Integer)
    created = db.Column(db.Integer)


class VaccineCentresModel(db.Model):
    __tablename__ = 'vaccine_centres'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    status = db.Column(db.Integer)
    created = db.Column(db.Integer)
    address = db.Column(db.String(100))
    postcode = db.Column(db.String(10))


class VaccineAvailabilityModel(db.Model):
    __tablename__ = 'vaccine_availability'
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    vaccine_centre_id = db.Column(db.Integer, db.ForeignKey(VaccineCentresModel.id), nullable=False)
    vaccine_id = db.Column(db.Integer, db.ForeignKey(VaccinesModel.id), nullable=False)
    count = db.Column(db.Integer)


class VaccineBookingModel(db.Model):
    __tablename__ = 'vaccine_booking'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id), nullable=False)
    vaccine_id = db.Column(db.Integer, db.ForeignKey(VaccinesModel.id), nullable=False)
    vaccine_centre_id = db.Column(db.Integer, db.ForeignKey(VaccineCentresModel.id), nullable=False)
    status = db.Column(db.Integer)
    created = db.Column(db.Integer)
