from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

marca_bp = Blueprint('marca', __name__, url_prefix = '/marca')


#altere para outra area se necessário
#CRUD
@marca_bp.route("/", methods=["POST"])
def criar():
    #dados que vieram
    nome = request.form.get("nome")
    


    #SQL
    sql = text("INSERT INTO marcas (nome_marca) VALUES (:nome) RETURNING id")
    dados = {"nome": nome} #os dados do que veio lá da var sql


    #executar consulta
    result = db.session.execute(sql, dados)
    db.session.commit()


    #pega o id
    id = result.fetchone()[0] #lá do RETURNING id
    dados['id'] = id


    return dados