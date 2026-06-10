from flask import Flask,redirect,render_template, url_for,request,flash
from . import customer
from app.models.product import Product
from app.models.cart import Cart
from flask_login import login_required,current_user
from app.models.user import User 
from app.models.order import Order
from app.models.order_item import OrderItem
from app.extensions import db

@customer.route("/home_page", methods=['GET', 'POST'])
def home_page():
    return render_template("customer/home_page.html", products=Product.query.all())   

 
@customer.route("/product_view/<int:product_id>")
def product_view(product_id):
    product = Product.get_by_id(product_id)
    return render_template("customer/product_view.html", product=product)


@customer.route("/add_to_cart/<int:product_id>", methods=['POST'])
@login_required
def add_to_cart(product_id):
    
    user_id = int(current_user.get_id())
    quantity = int(request.form.get("quantity"))
    Cart.add_to_Cart(user_id=user_id, product_id=product_id, quantity=quantity)
    flash("Item added to cart!", "success")
    return redirect(url_for("customer.cart_page"))



@customer.route("/cart")
@login_required
def cart_page():
    user_id = int(current_user.get_id())
    cart_items = Cart.get_user_cart(user_id)
 
    # attach product to each cart item
    for item in cart_items:
        item.product = Product.get_by_id(item.product_id)
 
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("customer/cart.html", cart_items=cart_items, total=total)
 
 
@customer.route("/remove_from_cart/<int:cart_id>", methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    user_id = int(current_user.get_id())
    Cart.remove_item(cart_id=cart_id, user_id=user_id)
    return redirect(url_for("customer.cart_page"))
 
 
@customer.route("/checkout")
@login_required
def checkout_page():
    user_id = int(current_user.get_id())
    cart_items = Cart.get_user_cart(user_id)
 
    if not cart_items:
        flash("Your cart is empty!", "warning")
        return redirect(url_for("customer.home_page"))
 
    for item in cart_items:
        item.product = Product.get_by_id(item.product_id)
 
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("customer/checkout.html", cart_items=cart_items, total=total)
 
 
@customer.route("/place_order", methods=['POST'])
@login_required
def place_order():
    user_id = int(current_user.get_id())
    cart_items = Cart.get_user_cart(user_id)

    if not cart_items:
        flash("Your cart is empty!", "warning")
        return redirect(url_for("customer.home_page"))

    for item in cart_items:
        item.product = Product.get_by_id(item.product_id)

    total = sum(item.product.price * item.quantity for item in cart_items)

   
    order = Order.create_order(
        user_id=user_id,
        full_name=request.form.get("full_name"),
        phone=request.form.get("phone"),
        address=request.form.get("address"),
        city=request.form.get("city"),
        province=request.form.get("province"),
        notes=request.form.get("notes"),
        payment_method=request.form.get("payment_method"),
        total_amount=total
    )

    if order:
       
        for item in cart_items:
            OrderItem.create_item(
                order_id=order.order_id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price
            )

       
        Cart.clear_cart(user_id)

        return render_template("customer/order_success.html", order=order)
    else:
        flash("Something went wrong. Please try again.", "danger")
        return redirect(url_for("customer.checkout_page"))
    
    
@customer.route("/shop")
def shop_page():
    query = request.args.get("q", "").strip()
    if query:
        products = Product.query.filter(
            Product.name.ilike(f"%{query}%"),
            Product.product_status == "published"
        ).all()
    else:
        products = Product.query.filter_by(product_status="published").all()
    return render_template("customer/shop.html", products=products, query=query)


@customer.route("/contact")
def contact_page():
    return render_template("customer/contact.html")