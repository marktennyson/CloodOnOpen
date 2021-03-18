from flask import Flask, render_template, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from requests import get
from models import *

app:Flask = Flask(__name__)

app.config['SECRET_KEY'] = "this-is-most-secret-key-of-theuniverse"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
admin = Admin(app, name="Flask country app")
admin.add_view(ModelView(Country, db.session))

def create_db() -> bool:
    with app.app_context():
        # db.create_all()
        try: 
            db.create_all()
            return True
        except Exception as e:
            print (e)
            return False

@app.route("/")
def index() -> render_template: 
    countryData = get("https://restcountries.eu/rest/v2/all").json()
    for country in countryData:
        newCountry = Country(name=country["name"], flag=country["flag"], population=country["population"],
                            capital=country["capital"], continent=country["region"], area=country["area"])
        db.session.add(newCountry)
    db.session.commit()
    return jsonify(msg="Done")
    # return render_template('index.html', countryData= get('https://restcountries.eu/rest/v2/all').text)

@app.route("/getall")
def getAll():
    allCountry = Country.query.all()
    allCountryL:list = list()
    for country in allCountry: 
        _dict:dict = country.__dict__
        del _dict['_sa_instance_state']
        allCountryL.append(_dict)
    return jsonify(allCountry=allCountryL)

app.debug = True

if __name__ == '__main__':
    app.run(port=8000)