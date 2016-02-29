from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI] = 'postgresql://psql@localhost/psql
db = SQLAlchemy(app)

from app import views, models