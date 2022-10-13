from config.config import db
from import_modelos import *
import os

if os.path.exists(db):
    os.remove(db)

# criar tabelas
db.create_all()

print("Banco de dados e tabelas criadas")