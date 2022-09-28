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
moedasbd = os.path.join(path, '../db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+moedasbd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)
