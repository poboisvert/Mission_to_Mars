# Import Splinter, BeautifulSoup, and Pandas - 10.5.3
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    # Slack configuration for Mac
    browser = Browser("chrome", **{'executable_path': '/usr/local/bin/chromedriver'}, headless=True) # For Mac
    # Kwars learning: https://www.geeksforgeeks.org/args-kwargs-python/

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere_data(browser) # hemisphere will be call in templates/index.html
    } # In app.py, it will be refer to mars. Line 20

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere_data(browser):
    try:
        # 1. Use browser to visit the URL 
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # 2. Create a list to hold the images and titles. - Dictionary
        hemisphere_list = []

        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        html = browser.html
        main_page_soup = soup(html, 'html.parser')  

        # Range total items
        list_range = len(main_page_soup.select("div.item"))

        # for loop for each item
        for i in range(list_range):

            # Get A link for the i selected
            link_image = main_page_soup.select("div.description a")[i].get('href')
            
            # Second page opened
            browser.visit(f'https://astrogeology.usgs.gov{link_image}')
            
            # Parse again the new HTML page
            html = browser.html
            sample_image_soup = soup(html, 'html.parser')
            
            # Save the full .JPG for the selected hemisphere
            img_url = sample_image_soup.select_one("div.downloads ul li a").get('href')
            
            # Save the img_title for the selected hemisphere
            img_title = sample_image_soup.select_one("h2.title").get_text()
            
            # Create a dictionary for the selected hemisphere 
            hemisphere = {'img_url': img_url,'title': img_title,  }
            
            # Append results dict to hemisphere image urls list
            hemisphere_list.append(hemisphere)
            
            # Reset hemisphere
            hemisphere = {}
            
            # Return to main page
            browser.back()

    except BaseException:
        return None
        
    # Return the list that holds the dictionary of each image url and title
    return hemisphere_list    


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())