from config.config import db
from import_modelos import *
import os

# criar tabelas
db.create_all()

print("Banco de dados e tabelas criadas")