from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

from controller import *

from models import Fish
db.create_all()
if __name__ == '__main__':
    app.run()