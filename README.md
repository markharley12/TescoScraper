# Tesco Groceries Scraper

This project scrapes product information from Tesco's groceries website for a specific food category and saves the data into JSON files.

## Features

- Uses Selenium to automate web scraping
- Extracts product information and filters out non-food items
- Saves data to JSON files in a specified directory

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone this repository:
```sh
git clone https://github.com/markharley12/TescoScraper.git
cd TescoScraper
```
2. Install the required Python packages:

```sh
pip install -r requirements.txt
```
Ensure you have Google Chrome installed. Download and install ChromeDriver from here or use webdriver_manager to handle it automatically.

## Usage
Run the scraper:

```sh
python tescoScraperMultiPage.py --food_type food-cupboard --start_page 1 --end_page 120 --output_dir json_database
```
The script will scrape product information from Tesco's groceries website for the specified category and pages, then save the data to JSON files in the specified output directory (default: json_database).
Configuration
You can configure the scraper using command-line arguments:

- **--food_type**: (required) Specify the food category to scrape. Choices are: "fresh-food", "bakery", "frozen-food", "treats-and-snacks", "food-cupboard".
- **--start_page**: (optional) Define the starting page number. Default is 1.
- **--end_page**: (optional) Define the ending page number. Default is 120.
- **--output_dir**: (optional) Specify the directory to save the JSON files. Default is json_database.

For example, to scrape the "bakery" category from pages 5 to 10 and save to a custom directory:

```sh
python tescoScraperMultiPage.py --food_type bakery --start_page 5 --end_page 10 --output_dir custom_directory
```
## File Structure
```
TescoScraper/
│
├── tescoScraperMultiPage.py
├── requirements.txt
└── json_database/
```
- tescoScraperMultiPage.py: Main script to run the scraper.
- requirements.txt: List of required Python packages.
- json_database/: Directory where JSON files are saved (default).

## Notes
Ensure that ChromeDriver is compatible with your version of Google Chrome.
If running in a headless environment, uncomment the headless option in the Chrome options configuration.
In my testing environment the scraper only worked in non headless mode.
## License
This project is licensed under the MIT License.
