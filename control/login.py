from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy


#senha_bp = Blueprint('senha', __name__, url_prefix = '/senha')
#registri-se com email e senha
@senha_bp.route("/senha", methods=['POST'])
def senha():
    senha = request.form.get('senha')
    email = request.form.get('email')

     if 
    
