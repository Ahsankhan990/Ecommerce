# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Config:
#     SQLALCHEMY_DATABASE_URI = (
#         "mssql+pyodbc://@.\SQLEXPRESS/DB_Ecommerce?"
#         "driver=ODBC+Driver+17+for+SQL+Server"
#     )
import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:RYfIWSTFGunHMhBmqoAfCLFimVHwmIVF@acela.proxy.rlwy.net:20794/railway"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ahsan2200'