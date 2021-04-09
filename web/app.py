from flask import Flask, request, make_response, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 
import config
app = Flask(__name__)




app.config['SERCET_KEY'] = 'Najahsaid'

if os.environ.get('DEBUG') == '1':
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DEV_DB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] =config.PROD_DB

# app.config['SQLALCHEMY_DATABASE_URI'] = config.DEV_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True)
    password=db.Column(db.String(250))

    def __init__(self, usernmae, email,password):
        self.username = usernmae
        self.email = email
        self.password =password

        # def __repr__(self):
        #     return '<User %>' % self.username


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/post', methods=['POST'])
def post_user():
    username=request.form['username']
    email=request.form['email']
    password=request.form['password']
    
    print(username,email,password)
    user = User(username,email,password)
    print(User.id)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=os.environ.get('DEBUG')=='1')
    # app.run( port=5000,debug=True)
