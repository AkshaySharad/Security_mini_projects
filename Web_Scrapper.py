# Scraping the imdb site

import requests
from bs4 import BeautifulSoup
import time

# URL of the website to scrape
url = "https://www.hackthissite.org/"
url = "https://realpython.github.io/fake-jobs/"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
result = soup.find(id = 'ResultsContainer')
print(result.prettify())
job_elements = result.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



