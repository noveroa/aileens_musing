"""
first step is to gather large, diverse, and clean data.  


* Respect Website Policies: Check the site’s terms of use or robots.txt file to ensure scraping is allowed.
* Avoid Overloading Servers: Use rate limits and polite scraping practices.
* Clean the Data: Remove unwanted tags, special characters, or advertisements.

- also : 
https://www.kaggle.com/datasets
https://github.com/mlabonne/llm-datasets
"""
import requests
from bs4 import BeautifulSoup

# Step 1: Specify the URL
url = "https://wikipedia.com"

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Parse the website content
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract all text from the page
text_data = soup.get_text()

# Step 5: Print the first 500 characters of the text
print(text_data[:500])