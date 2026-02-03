from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

categoria_bp = Blueprint('categoria', __name__, url_prefix = '/categoria')

# crud categorias

@categoria_bp.route("/", methods=["POST"])
def criar():
    #dados novos
    nome = request.form.get("nome")
    descricao = request.form.get("descrição")
    


    #SQL
    sql = text("INSERT INTO categorias (nome_categoria, descricao) VALUES (:nome, :descricao) RETURNING id")
    dados = {"nome": nome, "descricao": descricao} #para criar nova cateoria


    #executar consulta
    result = db.session.execute(sql, dados)
    db.session.commit()


    #pega o id
    id = result.fetchone()[0] #lá do RETURNING id
    dados['id'] = id


    return dados

@categoria_bp.route('/all', methods=['GET'])
def get_categoria():
    sql_query = text("SELECT * FROM categorias ") #filtro para no max 100 pg
    
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
#atualizar
@categoria_bp.route("/<id>", methods=["PUT"])
def atualizar(id):
    #dados que vieram postman
    nome = request.form.get("nome")
    descricao = request.form.get("descrição")


    sql = text("UPDATE categorias SET nome_categoria = :nome, descricao= :descricao WHERE id = :id")
    dados = {"nome": nome, "descricao": descricao, "id": id} #os dados que veio do bd sql


    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"categorias com o ID foram {id} atualizadas"
    else:
        db.session.rollback()
        return f"problemas ao atualizar dados"

@categoria_bp.route("/<id>", methods=['DELETE'])
def delete(id):
    sql = text("DELETE FROM categorias WHERE id = :id")
    dados = {"id": id}
    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"categoria com o ID {id} foi removida"
    else:
        db.session.rollback()
        return f"apagou o que não devia"

