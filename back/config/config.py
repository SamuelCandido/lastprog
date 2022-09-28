# importações
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


from flask_cors import CORS # permitir back receber json do front

# configurações
app = Flask(__name__)
CORS(app) # aplicar o cross domain
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) 
banco_de_dados = os.path.join(path, '../db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+banco_de_dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)


# importações de JWT
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from datetime import timedelta

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this! VER ISSO COM PROFESSOR
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10) #hours=1)
jwt = JWTManager(app)