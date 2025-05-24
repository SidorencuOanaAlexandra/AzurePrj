import pyodbc
from flask import Flask
from config import Config
from models.models import db
from routes import ui

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(ui)

if __name__ == '__main__':
    # try:
    #     connection = pyodbc.connect(
    #         f'Driver={Config.DRIVER};Server={Config.SERVER};Database={Config.DATABASE};Uid=server1234;Pwd={Config.PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
    #     )
    #     # connection = pyodbc.connect(
    #     #     'Driver={ODBC Driver 17 for SQL Server};Server=tcp:server1234.database.windows.net,1433;Database=cloud_db;Uid=server1234;Pwd=test211!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
    #     # )
    #     print ("connection ok")
    # except pyodbc.Error as e:
    #     print ("error", e)

    with app.app_context():
        db.create_all()
    app.run(debug=True)

