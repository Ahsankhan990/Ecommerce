from app.extensions import db
from flask_login import UserMixin
from datetime import datetime


class Product(db.Model, UserMixin):
    __tablename__ = "Products"
    
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image_url = db.Column(db.String(255)) 
    product_status = db.Column(db.String(20), default="draft")
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    
    
    @classmethod
    def add_product(cls, name, description, price, stock, image_url,product_status="draft"):
        try:
            new_product =  cls(
                name=name,
                description=description,
                price=price,
                stock=stock,
                image_url=image_url,
                product_status=product_status
            )
            db.session.add(new_product)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    
    def delete(id):
        try:
            db.session.delete(id)
            db.session.commit()
            return True
        except:
            return False
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get_or_404(id)
    
    
    def __repr__(self):
        return f"<Product {self.name}>"
    
    def get_id(self):
        return str(self.product_id)
    
    
    
    
    
    