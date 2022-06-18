# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Scrape the title
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the quick summary text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts


# Scrape the entire table with Pandas
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# Convert DataFrame back into HTML-ready code
df.to_html()


# 1. Use browser to visit the URL 
url_3 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url_3)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
        browser.find_by_css("a.product-item h3")[i].click()
        html = browser.html
        image_soup = soup(html, 'html.parser')
        image_url_rel = image_soup.find("a", text="Sample").get("href")
        hemisphere_title = image_soup.find('h2', class_='title').get_text()
        hemisphere_image_url = f'https://astrogeology.usgs.gov/search/results?=hemisphere+enhanced&k1=target&v1=Mars{image_url_rel}'
        hemispheres = {"title":hemisphere_title,"img_url":image_url_rel}
        hemisphere_image_urls.append(hemispheres)
        browser.back()


browser.quit()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls





