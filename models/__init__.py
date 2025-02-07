import os
import importlib
from flask_sqlalchemy import SQLAlchemy
from app import app  
db = SQLAlchemy()
models_dir = os.path.dirname(__file__)
for filename in os.listdir(models_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"models.{filename[:-3]}"
        importlib.import_module(module_name)
        print("loading: "+ module_name)
