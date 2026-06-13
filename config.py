class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@.\\SQLEXPRESS/DB_Ecommerce?"
        "driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ahsan2200'