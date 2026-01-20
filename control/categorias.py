from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

marca_bp = Blueprint('categoria', __name__, url_prefix = '/categoria')

# crud categorias

@marca_bp.route("/", methods=["POST"])
def criar():
    #dados novos
    nome = request.form.get("nome")
    


    #SQL
    sql = text("INSERT INTO categorias (nome_categoria) VALUES (:nome) RETURNING id")
    dados = {"nome": nome} #para criar nova cateoria


    #executar consulta
    result = db.session.execute(sql, dados)
    db.session.commit()


    #pega o id
    id = result.fetchone()[0] #lá do RETURNING id
    dados['id'] = id


    return dados