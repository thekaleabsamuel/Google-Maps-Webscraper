from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_google_maps():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Open Google Maps centered on Denver with a search for restaurants
    driver.get("https://www.google.com/maps/search/restaurants+near+me")

    try:
        # Wait for search box to appear
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.tactile-searchbox-input"))
        )

        # Search for restaurants in your desired location
        search_box.send_keys("restaurants in [Denver, CO]")
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.section-result"))
        )

        # Simulate scrolling to the bottom of the page for 10 seconds
        for _ in tqdm(range(10), desc="Scrolling"):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        # Extract restaurant details
        restaurant_cards = driver.find_elements_by_css_selector("div.section-result")
        for card in restaurant_cards:
            name = card.find_element_by_css_selector("h3").text
            phone = card.find_element_by_css_selector("span[data-item-id='phone']").text
            website = card.find_element_by_css_selector("div.section-result-details > div").get_attribute("innerHTML")
            # Extracting store hours may require additional logic

            # Print restaurant details
            print("Name:", name)
            print("Phone:", phone)
            print("Website:", website)
            print("-----------------------")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    scrape_google_maps()
