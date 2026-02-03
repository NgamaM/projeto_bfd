from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

cor_bp = Blueprint('cor', __name__, url_prefix = '/cor')

#CRUD CORES
@cor_bp.route("/criar", methods=["POST"])
def create():
    #dados que vieram do postman
    nome = request.form.get("nome")
    


    #SQL
    sql = text("INSERT INTO cores (nome_cor) VALUES (:nome) RETURNING id")
    dados = {"nome": nome} #os dados do que veio lá da var sql


    #executar consulta
    result = db.session.execute(sql, dados)
    db.session.commit()


    #pega o id
    id = result.fetchone()[0] #lá do RETURNING id
    dados['id'] = id


    return dados

#ver
@cor_bp.route("/all", methods=["GET"])
def get_cor():
    sql_query = text("SELECT * FROM cores ") #filtro para no max 100 pg
    
    try:
        #result sem dados
        result = db.session.execute(sql_query)
                
        relatorio = result.mappings().all()
        json = [dict(row) for row in relatorio] #Gambi pq cada linha é um objeto


        print(json)


        return json
    except Exception as e:
        
        #salvar log da aplicação 
        #Mandar email programador
        return e
    
#alterar pelo id
@cor_bp.route("/<id>", methods=["PUT"])
def atualizar(id):
    nome = request.form.get("nome")


    sql = text("UPDATE cores SET nome_cor = :nome WHERE id = :id")
    dados = {"nome": nome, "id": id} #os dados que veio do bd sql


    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"cores com o ID foram {id} atualizadas"
    else:
        db.session.rollback()
        return f"problemas ao atualizar dados"

#deletar
@cor_bp.route("/<id>", methods=["DELETE"])
def deletar(id):
    sql = text("DELETE FROM marcas WHERE id = :id")
    dados = {"id": id}
    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"marcas com o ID {id} foi removida"
    else:
        db.session.rollback()
        return f"erro ao deletar dados"
#deletei item 4 do teste criar e put

