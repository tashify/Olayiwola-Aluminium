from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    admin_id = db.Column(db.Integer(), primary_key=True, autoincrement =True)
    admin_name = db.Column(db.String(255), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    
class Contact(db.Model):
    cont_id = db.Column(db.Integer(), primary_key=True, autoincrement =True)
    cont_name = db.Column(db.String(255), nullable=False)
    cont_email = db.Column(db.String(255), nullable=False)
    cont_phone = db.Column(db.String(255), nullable=False)
    cont_msg = db.Column(db.Text(), nullable=False)
    cont_reg_date =db.Column(db.DateTime(), default=datetime.utcnow)
    