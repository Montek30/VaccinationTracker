from flask import Flask, render_template
from flask_login import LoginManager
from routes.auth_bp import auth_bp
from routes.vaccination_centre_bp import vaccination_centre_bp
from routes.main_bp import main_bp
from routes.vaccine_availability_bp import vaccine_availability_bp
from settings import db


app = Flask(__name__)

app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(vaccination_centre_bp, url_prefix='/vaccine_centre')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(vaccine_availability_bp, url_prefix='/vaccine_availability')

app.config['SECRET_KEY'] = '!@#amam@@!!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/vaccine_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)


from models.User import User
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.debug = True
    app.run()
