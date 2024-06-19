from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import json

# Setup Chrome options (remove headless mode)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL of the Tesco groceries page
url = 'https://www.tesco.com/groceries/en-GB/shop/fresh-food/all?page=1&count=48'

# Open the URL
driver.get(url)

try:
    # Wait for the elements to load
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ddsweb-link__text')))

    # Print the number of elements found
    print(f"Number of elements found: {len(elements)}")

    # Extract and filter the text from each element
    food_items = []
    for element in elements:
        text = element.text.strip()
        # Filter out non-food items
        if text and not any(keyword in text for keyword in ["Help","Contact us","Sign in","Register","Skip to", "Write a review", "Rest of", "shelf", "Checkout", "Food Item:"]):
            food_items.append(text)

    # Print the filtered food items
    for item in food_items:
        print("Food Item:")
        print(item)

    # Write the food items to a JSON file
    with open('food_items.json', 'w') as json_file:
        json.dump(food_items, json_file, indent=4)

    print(f"Food items have been written to food_items.json")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
    sys.exit(1)

# Close the browser
driver.quit()
