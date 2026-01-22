from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

marca_bp = Blueprint('categoria', __name__, url_prefix = '/categoria')

# crud categorias

@categoria_bp.route("/", methods=["POST"])
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

    @categoria_bp.route('/all', methods=['GET'])
def get_categoria():
    sql_query = text("SELECT * FROM ategorias ") #filtro para no max 100 pg
    
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
        #nao ta funcionando ainda
        return e