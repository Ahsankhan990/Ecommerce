from app.extensions import db

class Cart(db.Model):
    __tablename__ = "cart"

    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1)
   
    @classmethod
    def add_to_Cart(cls, user_id, product_id, quantity=1):
        try:
            new_item = cls(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity
            )
            db.session.add(new_item)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    @classmethod
    def get_user_cart(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def remove_item(cls, cart_id, user_id):
        try:
            item = cls.query.filter_by(cart_id=cart_id, user_id=user_id).first()
            if item:
                db.session.delete(item)
                db.session.commit()
                return True
            return False
        except:
            db.session.rollback()
            return False

    @classmethod
    def clear_cart(cls, user_id):
        try:
            cls.query.filter_by(user_id=user_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False