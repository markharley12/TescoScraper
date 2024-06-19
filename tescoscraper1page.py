from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

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

    # Print the page source for debugging purposes
    # print("Page Source:")
    # print(driver.page_source)

    # Print the number of elements found
    print(f"Number of elements found: {len(elements)}")

    # Extract and print the text from each element
    for element in elements:
        print("Element Text:")
        print(element.text)
except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
    sys.exit(1)


driver.quit()

