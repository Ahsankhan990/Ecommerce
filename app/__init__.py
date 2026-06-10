
from flask import Flask, render_template, redirect,url_for
from app.extensions import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.secret_key = "ahsan2200" 
    app.config.from_object(Config)
    db.init_app(app)
    
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.models.user import User    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.blueprints.auth import auth
    app.register_blueprint(auth)
    
    from app.blueprints.admin import admin
    app.register_blueprint(admin)
    
    from app.blueprints.customer import customer
    app.register_blueprint(customer)
    
    @app.route("/")
    def home():
        # return redirect(url_for("admin.deshboard"))
        return redirect(url_for("auth.login"))
        
        # return redirect(url_for("customer.home_page"))
        # return redirect(url_for("customer.product_view"))
        
        

    return app
    