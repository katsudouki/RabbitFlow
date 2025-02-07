from extensions import db
from datetime import datetime


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    type = db.Column(db.String(10), nullable=False)  # INFO: 'income' ou 'expense'
