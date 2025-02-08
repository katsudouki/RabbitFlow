from extensions import db
from app import app  
import models
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # INFO: 'income' ou 'expense'
    color = db.Column(db.String(10), nullable=False,default="#88dbda")
    icon = db.Column(db.String(10), nullable=False,)
with app.app_context():
    db.create_all()
    
def create_categories():
    categorylist = Category.query.all()
    if Category.query.first() is None:
        default_list=[
             ("food", "expense","#fa4b6e","🍔"),
             ("waste", "expense","#8c2119","💸"),
             ("clothes", "expense","#a87732","👚"),
             ("Basic bills", "expense","#a85c32","🧾"),
             ("Leisure", "expense","#6432a8","🎮")
        ]
        for cat in default_list:
            db.session.add(Category(name=cat[0],type=cat[1],color=cat[2],icon=cat[3]))
        
        db.session.commit()
        print("default categories created.")
    else:
        print("default categories already exist.")
with app.app_context():
    create_categories()