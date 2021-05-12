from flask import Flask, jsonify
from models.db import db
from models.model import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sys import argv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "most_secret_key_of_the_universe"

db.init_app(app)
admin = Admin(app, name="basic blog app admin", template_mode="bootstrap4")

admin.add_view(ModelView(User, db.session, category="Team"))
admin.add_view(ModelView(Post, db.session, category="Team"))

@app.route("/")
def index(): 
    return jsonify(message="Salve Mundi!")

def create_db():
    with app.app_context():
        db.create_all()
        print ("Done")

if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1].lower() == "create_db": create_db()
        else: print ("invalid input")
    else: app.run(debug=True, port=3000)