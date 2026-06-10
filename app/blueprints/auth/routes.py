
from flask import render_template, request, redirect, url_for, flash
from app.models.user import User
from werkzeug.security import check_password_hash 
from werkzeug.security import generate_password_hash
from app.extensions import db
from flask_login import login_user
from . import auth


@auth.route("/signup", methods=["GET", "POST"], endpoint="signup")
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        
        
        if not email or not password or not name:
            flash("Email, Password and name cannot be empty!")
            return redirect(url_for("auth.signup"))
        
        user = User.query.filter_by(email=email).first()
        
        
        if user:
            flash("You are already registered, please login instead.")
            return render_template("login.html")

        else: 
            hashed_password = generate_password_hash(password)
            new_user = User(name= name, email=email, password=hashed_password, role= "customer")
            db.session.add(new_user)
            db.session.commit()
      
            flash("Signup successful! Please login now.")
            return render_template("login.html")
    
    return render_template("signup.html")

@auth.route("/login", methods = ["GET", "POST"], endpoint = "login")
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        if not email or not password:
            flash("Email and Password cannot be empty!", "error")
            return redirect(url_for("auth.login"))
        
      
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            
            login_user(user)
            flash(f"Welcome {user.__repr__()}!", "success")
            
            
            if user.is_admin():
                # return redirect(url_for("admin.dashboard"))  # Admin dashboard
                return redirect(url_for("admin.deshboard"))
            else:
                # return redirect(url_for("customer.dashboard"))  # Customer dashboard
                return redirect(url_for("customer.home_page"))
        else:
            flash("Invalid email or password!", "error")
            return redirect(url_for("auth.login"))
    
    
    return render_template("login.html")