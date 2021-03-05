from flask import Flask, render_template, request, redirect # Flask to render a template.
from flask_pymongo import PyMongo # PyMongo to interact with our Mongo database.
import scraping # will convert from Jupyter notebook to Python.

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app" # connect to Mongo using a URI, a uniform resource identifier similar to a URL.
mongo = PyMongo(app) # ocalhost server, using port 27017, using a database named "mars_app".

@app.route("/")
def index():
    mars = mongo.db.mars.find_one() #  PyMongo to find the "mars" collection in our database
    return render_template("index.html", mars=mars) # to return an HTML template using an index.html fil AND , mars=mars) tells Python to use the "mars" collection in MongoDB.

@app.route("/scrape") # defines the route
def scrape():
    mars = mongo.db.mars # PyMongo to find the "mars" collection in our database
    mars_data = scraping.scrape_all() # scrape_all function in the scraping.py
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

@app.route("/clear") # defines the route
def clear():
    try:
        mongo.db.mars.remove({})
        return redirect('/', code=302)
    except:
        print("Hello")
        return None

if __name__ == "__main__":
   app.run(debug=True)