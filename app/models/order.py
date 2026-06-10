from app.extensions import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "Orders"

    order_id       = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, nullable=False)
    full_name      = db.Column(db.String(100), nullable=False)
    phone          = db.Column(db.String(20), nullable=False)
    address        = db.Column(db.String(255), nullable=False)
    city           = db.Column(db.String(50), nullable=False)
    province       = db.Column(db.String(50))
    notes          = db.Column(db.String(500))
    payment_method = db.Column(db.String(50), default="cash_on_delivery")
    total_amount   = db.Column(db.Float, nullable=False)
    status         = db.Column(db.String(30), default="pending")
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create_order(cls, user_id, full_name, phone, address, city, province, notes, payment_method, total_amount):
        try:
            order = cls(
                user_id=user_id,
                full_name=full_name,
                phone=phone,
                address=address,
                city=city,
                province=province,
                notes=notes,
                payment_method=payment_method,
                total_amount=total_amount,
                status="pending"
            )
            db.session.add(order)
            db.session.flush()  # ← get order_id without committing
            return order
        except Exception as e:
            db.session.rollback()
            print("Order create error:", e)
            return None