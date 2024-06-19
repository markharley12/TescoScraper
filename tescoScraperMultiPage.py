from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
import json
import time
import os
import argparse

# Setup Chrome options (remove headless mode)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
# driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

def getFoodItems(url: str, driver) -> list:
    """
    Fetches food items from a given URL, filters out non-food items, and returns a list of food items.

    Args:
        url (str): The URL containing the food items.
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        list: A list of food items.
    """
    # Open the URL
    driver.get(url)

    try:
        # Wait for the elements to load
        # The WebDriverWait class provides a way to wait for a certain condition to be met
        # The condition is specified using the expected_conditions module
        wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
        # Locate elements with the class name 'ddsweb-link__text'
        # The By class provides a way to locate elements by different criteria
        # The presence_of_all_elements_located method waits for all elements to be present
        elements = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'ddsweb-link__text')))

        # Extract and filter the text from each element
        # The text of each element is stripped to remove leading and trailing whitespace
        # Non-food items are identified by keywords in the text
        # The any function checks if any of the keywords are present in the text
        food_items = []
        for element in elements:
            text = element.text.strip()
            if text and not any(keyword in text for keyword in [
                "Help", "Contact us", "Sign in", "Register", "Skip to",
                "Write a review", "Rest of", "shelf", "Checkout"
            ]):
                food_items.append(text)

        return food_items
    except Exception as e:
        print(f"Error occurred while loading elements: {e}")
        return []



def printFoodItems(food_items: list) -> None:
    """
    Prints the given list of food items.

    Args:
        food_items (List[str]): The list of food items to print.
    """
    # Iterate over each food item
    for item in food_items:
        # Print the food item
        print(item)



def writeFoodItems(food_items: list, filename: str = 'food_items.json') -> None:
    """
    Writes the given food items to a JSON file.

    Args:
        food_items (List[str]): The list of food items to write.
        filename (str, optional): The name of the file to write to. Defaults to 'food_items.json'.
    """
    # Open the file in write mode
    with open(filename, 'w') as json_file:
        # Write the food items to the file in JSON format
        # The indent parameter is used to format the JSON output with indentation for readability
        json.dump(food_items, json_file, indent=4)

    # Print confirmation that the food items have been written to the file
    # The f-string is used to format the string with the filename as a placeholder
    print(f"Food items have been written to {filename}")

def getFoodPage(foodType: str, pageNumber: int, driver, output_dir: str) -> bool : 
    """
    Scrapes the specified foodType from Tesco's groceries website for the given page number.
    Writes the extracted food items to a JSON file.

    Args:
        foodType (str): The type of food to scrape.
        pageNumber (int): The page number to scrape.
        driver (WebDriver): The Selenium WebDriver instance.
        output_dir (str): The directory to write the JSON files to.

    Returns:
        None
    """
    # Construct the Tesco URL
    # Example: https://www.tesco.com/groceries/en-GB/shop/fresh-food/all?page=1&count=48
    tesco_url = (f"https://www.tesco.com/groceries/en-GB/shop/{foodType}/all?"
                 f"page={pageNumber}&count=48")

    # Construct the filename for the JSON file
    # Example: fresh-food_1.json
    filename = os.path.join(output_dir, f"{foodType}_{pageNumber}.json")

    try:
        # Get the food items from the Tesco URL
        url_foods = getFoodItems(tesco_url, driver)

        # Print the extracted food items
        # Example: Tesco Medium Free Range Eggs 12 Pack
        printFoodItems(url_foods)

        # Write the extracted food items to a JSON file
        # Example: fresh-food_1.json
        writeFoodItems(url_foods, filename)

        if len(url_foods) == 0:
            return True
        return False

    except Exception as e:
        # Print the error and exit with a non-zero status
        print(f"An error occurred: {e}")
        sys.exit(1)


# Main execution block
if __name__ == "__main__":
    # TESCO_FOOD_TYPES = ["fresh-food", "bakery", "frozen-food", "treats-and-snacks", "food-cupboard"]
    # APPROXIMATE_LENGTHS = [90, 20, 25, 40, 120]

    # Setup argument parser
    parser = argparse.ArgumentParser(description='Scrape food data from TESCO website.')
    parser.add_argument('--output_dir', type=str, default='json_database', help='Directory to save the JSON files (default: json_database)')
    parser.add_argument('--food_type', type=str, required=True, choices=["fresh-food", "bakery", "frozen-food", "treats-and-snacks", "food-cupboard"], help='Type of food to scrape (required)')
    parser.add_argument('--start_page', type=int, default=1, help='Starting page number (default: 1)')
    parser.add_argument('--end_page', type=int, default=120, help='Ending page number (default: 120)')


    args = parser.parse_args()

    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    try:
        for pageNumber in range(args.start_page, args.end_page + 1):
            driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)  # Reinitialize the driver
            finalpage = getFoodPage(args.food_type, pageNumber, driver, args.output_dir)
            driver.close()
            if finalpage:
                break
            time.sleep(2)  # Add delay to ensure pages load properly
    finally:
        driver.quit()