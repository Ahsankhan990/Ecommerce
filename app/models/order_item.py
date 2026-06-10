from app.extensions import db

class OrderItem(db.Model):
    __tablename__ = "Order_Items"

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id      = db.Column(db.Integer, nullable=False)
    product_id    = db.Column(db.Integer, nullable=False)
    quantity      = db.Column(db.Integer, nullable=False)
    price         = db.Column(db.Float, nullable=False)

    @classmethod
    def create_item(cls, order_id, product_id, quantity, price):
        try:
            item = cls(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                price=price
            )
            db.session.add(item)
            
            return item
        except Exception as e:
            print("OrderItem create error:", e)
            return None

    @classmethod
    def get_by_order(cls, order_id):
        return cls.query.filter_by(order_id=order_id).all()