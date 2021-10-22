from flask import Blueprint
from controllers.UserController import login, logout, signup

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['GET','POST'])(login)
auth_bp.route('/signup', methods=['GET','POST'])(signup)
auth_bp.route('/logout', methods=['GET','POST'])(logout)