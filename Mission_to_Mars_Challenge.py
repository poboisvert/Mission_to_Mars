#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


#### SQL under MAC OS X
# Start MongoDB: brew services start mongodb-community@4.4
# mongodb
# use practicedb
# https://blog.hartleybrody.com/web-scraping-cheat-sheet/


# In[ ]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# In[ ]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1) # telling our browser to wait one second, delay is useful because sometimes dynamic pages take while to load


# In[ ]:


html = browser.html # set up the HTML parser:
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide') # One is that we're searching for elements with a specific combination of tag (ul and li) + . is for selecting classe


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL 10.3.4
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[ ]:


# Create DF 10.3.5
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()

browser.quit()


# In[ ]:


""" # Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Path to chromedriver
!which chromedriver

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# ## JPL Space Images Featured Image

# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url

# ## Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()

df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df

df.to_html()

browser.quit() """


# In[ ]:


###
#
#
# Challenger Below
#
#
###


# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[3]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# ### Visit the NASA Mars News Site

# In[4]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[6]:


slide_elem.find("div", class_='content_title')


# In[7]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[9]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[12]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# ### Mars Facts

# In[14]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()


# In[15]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[16]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[17]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[18]:


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


# In[19]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_list


# In[20]:


# 5. Quit the browser
browser.quit()

