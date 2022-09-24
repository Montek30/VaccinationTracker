from flask import Flask, render_template
from flask_login import LoginManager
from routes.auth_bp import auth_bp
from routes.vaccination_centre_bp import vaccination_centre_bp
from routes.main_bp import main_bp
from routes.vaccine_availability_bp import vaccine_availability_bp
from routes.vaccine_bp import vaccine_bp
from routes.vaccine_booking_bp import vaccine_booking_bp
from settings import db, mail
from models.Models import UserModel


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'monteksingh30@gmail.com'
app.config['MAIL_PASSWORD'] = '*_(#)Mon#(*)_123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(vaccination_centre_bp, url_prefix='/vaccine_centre')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(vaccine_availability_bp, url_prefix='/vaccine_availability')
app.register_blueprint(vaccine_bp, url_prefix='/vaccine')
app.register_blueprint(vaccine_booking_bp, url_prefix='/vaccine_booking')

app.config['SECRET_KEY'] = '!@#montek@@!!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/vaccine_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
mail.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return UserModel.query.get(int(user_id))

if __name__ == '__main__':
    app.debug = True
    app.run()
