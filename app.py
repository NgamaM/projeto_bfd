from flask import Flask
#import do banco de dados
from conf.database import init_db


#Importar módulos 
from control.marca import marca_bp
from control.usuario import usuario_bp
#from control.produto import produto_bp




app = Flask(__name__)


#Conexao Geral do meu app
init_db(app)


#Registro de controladores 
app.register_blueprint(marca_bp)
app.register_blueprint(usuario_bp)




if __name__ == "__main__":
    app.run(debug=True)
