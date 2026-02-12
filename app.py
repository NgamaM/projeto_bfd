from flask import Flask
#import do banco de dados
from conf.database import init_db


#Importar módulos 
from control.marca import marca_bp
from control.usuario import usuario_bp
from control.categoria import categoria_bp
from control.cor import cor_bp
from control.maquina import maquina_bp
from control.peca import peca_bp





app = Flask(__name__)


#Conexao Geral do meu app
init_db(app)


#Registro de controladores 
app.register_blueprint(marca_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(cor_bp)
app.register_blueprint(maquina_bp)
app.register_blueprint(peca_bp)




if __name__ == "__main__":
    app.run(debug=True)
