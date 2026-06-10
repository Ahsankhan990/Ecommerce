import os
from flask import Flask, redirect, request, render_template, url_for, flash, current_app
from . import admin
from app.models.product import Product
from app.extensions import db
from app.models.order import Order
from app.models.order_item import OrderItem


@admin.route("/deshboard", methods=['GET', 'POST'], endpoint="deshboard")
def deshboard():
    if request.method == "POST":
        image = request.files.get("image_file")
        image_url = None
        if image and image.filename != "":
            upload_folder = os.path.join(current_app.root_path, "static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)
            save_path = os.path.join(upload_folder, image.filename)
            image.save(save_path)
            image_url = f"uploads/{image.filename}"

        new = Product.add_product(
            name=request.form.get("name"),
            description=request.form.get("description"),
            price=request.form.get("price"),
            stock=request.form.get("stock"),
            image_url=image_url,
            product_status=request.form.get("status")
        )

        if new:
            flash("Successfully inserted!", "success")
        else:
            flash("Not inserted!", "failed")

        return redirect(url_for("admin.add_products"))

    products = Product.query.all()
    return render_template("admin/admin_deshboard.html", products=products)
   



@admin.route("/delete_products/<int:product_id>", methods=["POST"])
def delete_products(product_id):
    prod = Product.get_by_id(product_id)
    Product.delete(prod)
    flash("Product deleted!", "success")
    return redirect(url_for("admin.deshboard"))


@admin.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    edit_prod = Product.get_by_id(product_id)

    if request.method == "POST":
        edit_prod.name = request.form.get("name")
        edit_prod.description = request.form.get("description")
        edit_prod.price = request.form.get("price")
        edit_prod.stock = request.form.get("stock")
        edit_prod.product_status = request.form.get("status")

        image = request.files.get("image_file")
        if image and image.filename != "":
            upload_folder = os.path.join(current_app.root_path, "static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)
            save_path = os.path.join(upload_folder, image.filename)
            image.save(save_path)
            edit_prod.image_url = f"uploads/{image.filename}"

        db.session.commit()
        flash("Product updated successfully!", "success")
        return redirect(url_for("admin.deshboard"))

    return render_template("admin/edit_product.html", product=edit_prod)


@admin.route("/orders")
def orders():
    all_orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template("admin/admin_orders.html", orders=all_orders)
 
 
@admin.route("/order/<int:order_id>")
def order_detail(order_id):
    order = Order.query.get(order_id)
    order_items = OrderItem.get_by_order(order_id)
 
    # attach product to each item
    for item in order_items:
        item.product = Product.get_by_id(item.product_id)
 
    return render_template("admin/admin_order_detail.html", order=order, order_items=order_items)
 
 
@admin.route("/order/<int:order_id>/update_status", methods=["POST"])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    new_status = request.form.get("status")
    if order and new_status:
        order.status = new_status
        db.session.commit()
        flash(f"Order #{order_id} status updated to {new_status}!", "success")
    return redirect(url_for("admin.orders"))