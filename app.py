# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"


mongo = PyMongo(app)

#  create route that renders index.html template
@app.route("/")
def index():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars_dict=mars)


@app.route("/scrape")
def scrape():

    # Run scraped functions
    
    news = scrape_mars.scrape_news()
    jpl = scrape_mars.scrape_jpl()
    weather = scrape_mars.scrape_weather()
    facts = scrape_mars.scrape_facts()
    hemi = scrape_mars.scrape_hemisphere()
    
    # Store results into a dictionary
    mars_data = {
        "news_title": news["news_title"],
        "news_p": news["news_p"],
        "featured_image_url": jpl["featured_image_url"],
        "mars_weather": weather["mars_weather"],
        "mars_facts": facts["mars_facts"],
        "mars_hemisphere": hemi["mars_hemisphere"],
    }
    # Remove old record
    mongo.db.collection.remove({})
    # Insert forecast into database
    mongo.db.collection.insert_one(mars_data)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)