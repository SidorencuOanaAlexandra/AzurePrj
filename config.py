import os

class Config:
    #Driver={ODBC Driver 18 for SQL Server};Server=tcp:server1234.database.windows.net,1433;Database=cloud_db;Uid=server1234;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
    SERVER = 'tcp:server1234.database.windows.net,1433'
    SERVER2 = 'tcp:server1234.database.windows.net'
    DATABASE = 'cloud_db'
    USERNAME = 'server1234'
    PASSWORD = 'test211!'
    DRIVER = '{ODBC Driver 17 for SQL Server}'

    # SQL_SERVER = os.getenv("SQL_SERVER", "<nume-server>.database.windows.net")
    # SQL_DATABASE = os.getenv("SQL_DATABASE", "idea_voting_db")
    # SQL_USER = os.getenv("SQL_USER", "<utilizator>")
    # SQL_PASSWORD = os.getenv("SQL_PASSWORD", "<parola>")
    # SQL_DRIVER = "ODBC Driver 17 for SQL Server"
    #SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER2}:1433/{DATABASE}?driver={DRIVER}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret" #os.getenv("SECRET_KEY", "super-secret-key")
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://server1234:test211!@server1234.database.windows.net:1433/"
        "cloud_db?driver=ODBC+Driver+17+for+SQL+Server"
    )
    endpoint = "https://languageaiservice123.cognitiveservices.azure.com/"
    key = "2mj4KVRggvMrDZLQz7hHJRHgfCiX0c9EwsC7G5W74EGjZU8m3sLiJQQJ99BEAC5RqLJXJ3w3AAAEACOGFDCs"
