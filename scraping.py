def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all() # scrape_all function in the scraping.py
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
   app.run()