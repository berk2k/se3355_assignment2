# product.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)

    
