from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# from app import mail
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
mail = Mail()