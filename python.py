import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set up Selenium with Chrome browser
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Define the search URL for Google Maps
search_url = "https://www.google.com/maps/search/restaurants+near+me"

# Fetch the search results page
driver.get(search_url)
time.sleep(5)  # Wait for 5 seconds
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the business listings
business_listings = soup.find_all("div", class_="section-result")

# Loop through each business listing
for listing in business_listings:
    # Get the business name
    business_name = listing.find("h3").text if listing.find("h3") else "Unknown"

    # Check if the business has a website link
    website_link = listing.find("a", class_="e07Vkf kA9KIf")
    has_website = bool(website_link)

    if not has_website:
        print(f"Business: {business_name} (No website found)")

# Close the browser
driver.quit()