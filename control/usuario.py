from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

usuario_bp = Blueprint('usuario', __name__, url_prefix = '/usuario')

#registri-se com email e senha
@usuario_bp.route("/login", methods=['POST'])
def senha():
    senha = request.form.get('senha')
    email = request.form.get('email')

    sql = text (""" SELECT email, senha FROM usuarios WHERE email = :email """)
    result = db.session.execute(sql, {"email": email})
    usuario = result.fetchone()

    if usuario is None:
        return jsonify({"msg": " email não encontrado"}), 404

    if email == usuario.email and senha == usuario.senha:
        return jsonify ({"msg": "acesso concedido"}), 200
    else:
        return jsonify ({"msg": "senha incoreto"}), 401

    """precisa de hash, mas faz o simples. 
    faz funcionar primeiro"""
    
@usuario_bp.route("/teste", methods=["GET"])
def teste_sevidor():
    return "login funcionando"
