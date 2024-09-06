# 4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask,render_template,request

from flask.ext.sqlalchemy import SQLAlchemy
import os

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

lm= LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
lm.login_view = 'login'

db = SQLAlchemy(app)

from app import views, models

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['username']
        return render_template('submit.html',username=user_name)

if __name__ == "__main__":
    app.run(debug = True)