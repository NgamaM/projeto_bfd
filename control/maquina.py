from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

maquina_bp = Blueprint('maquina', __name__, url_prefix = '/maquina')

#CRUD
#relacao entre maquinas e marcas, categorias, cores

@maquina_bp.route("/criar", methods=["POST"])
def post_criar():
    nome = request.form.get("nome")
    potencia = request.form.get("potencia")
    ano = request.form.get("ano")
    peso = request.form.get("peso")
    id_marca = request.form.get("id_marca")
    id_categoria = request.form.get("id_categoria")
    id_cor = request.form.get("id_cor")

    sql = text("INSERT INTO maquinas (nome_modelo, potencia_cv, ano_modelo, peso_kg, id_marca, id_categoria, id_cor) VALUES (:nome, :potencia, :ano, :peso, :id_marca, :id_categoria, :id_cor) RETURNING id")
    dados = {"nome": nome, "potencia": potencia, "ano": ano, "peso": peso, "id_marca": id_marca, "id_categoria": id_categoria, "id_cor": id_cor}

    result = db.session.execute(sql, dados)
    db.session.commit()

    id = result.fetchone()[0]
    dados['id'] = id

    return dados

@maquina_bp.route("/ver", methods=["GET"])
def get_ver():
    sql_query = text("SELECT * FROM maquinas ") 
    
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

@maquina_bp.route("/relatorio", methods=["GET"])
def get_relatorio():
    sql_query = text("select * from maquinas m inner join marcas mc on mc.id = m.id_marca  ") 
    
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

@maquina_bp.route("/<id>", methods=["PUT"])
def atualizar(id):
    #dados que vieram postman
    nome = request.form.get("nome")
    potencia = request.form.get("potencia")
    ano = request.form.get("ano")
    peso = request.form.get("peso")
    id_marca = request.form.get("id_marca")
    id_categoria = request.form.get("id_categoria")
    id_cor = request.form.get("id_cor")


    sql = text("UPDATE maquinas SET nome_modelo = :nome WHERE id = :id")
    dados = {"nome": nome, "id": id} #os dados que veio do bd sql


    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"informações de maquinas com o ID foram {id} atualizadas"
    else:
        db.session.rollback()
        return f"problemas ao atualizar dados"
