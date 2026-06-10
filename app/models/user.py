from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
# from app.models import cart
# from app.models import order

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    
  
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='customer')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # carts = db.relationship('Cart', backref='user', lazy=True)
    # orders = db.relationship('Order', backref='user', lazy=True)
    
    def get_id(self):
        return str(self.user_id) 
    
    def __repr__(self):
        return f'<User {self.name}>'
    
    def is_admin(self):
        return self.role == 'admin'
    

