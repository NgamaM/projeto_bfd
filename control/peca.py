from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from conf.database import db

peca_bp = Blueprint('peca', __name__, url_prefix = '/peca')

#CRUD peças (precisa ser criado no banco de dados)
@peca_bp.route("/criar", methods=["POST"])
def post_criar():
    nome = request.form.get("nome")
    sku = request.form.get("sku")
    preco = request.form.get("preço")
    fabricante = request.form.get("fabricante")
    id_marca = request.form.get("id_marca")
    id_categoria = request.form.get("id_categoria")


    sql = text("INSERT INTO peças (nome_peças, sku, preco, fabricante, id_marca, id_categoria) VALUES (:nome, :sku, :preco, :fabricante, :id_marca, :id_categoria) RETURNING id")
    dados = {"nome": nome, "sku": sku, "preco": preco, "fabricante": fabricante, "id_marca": id_marca, "id_categoria": id_categoria}

    result = db.session.execute(sql, dados)
    db.session.commit()

    id = result.fetchone()[0]
    dados['id'] = id

    return dados

@peca_bp.route("/ver", methods=["GET"])
def get_ver():
    sql_query = text("SELECT * FROM peças ") 
    
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

#precisa testar o PUT
@peca_bp.route("/<id>", methods=["PUT"])
def put_atualizar(id):
    nome = request.form.get("nome")
    sku = request.form.get("sku")
    preco = request.form.get("preço")
    fabricante = request.form.get("fabricante")
    id_marca = request.form.get("id_marca")
    id_categoria = request.form.get("id_categoria")

    sql = text("UPDATE peças SET nome_modelo = :nome WHERE id = :id")
    dados = {"nome": nome, "id": id} #os dados que veio do bd sql


    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"informações de peças com o ID {id} foram atualizadas"
    else:
        db.session.rollback()
        return f"problemas ao atualizar dados"

@peca_bp.route("/id", methods=["DELETE"])
def deletar(id):
    sql = text("DELETE FROM peças WHERE id = :id")
    dados = {"id": id}
    result = db.session.execute(sql, dados)


    linhas_afetadas = result.rowcount #conta quantas linhas foram afetadas
    
    if linhas_afetadas == 1: 
        db.session.commit()
        return f"peça com o ID {id} foi removida."
    else:
        db.session.rollback()
        return f"item não encontrado."

# delete não foi testado    