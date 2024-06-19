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
Install the required Python packages:

```sh
pip install -r requirements.txt
```
Ensure you have Google Chrome installed. Download and install ChromeDriver from here or use webdriver_manager to handle it automatically.

## Usage
1. Run the scraper:

```sh
python tescoScraperMultiPage.py
```
2. The script will scrape product information from Tesco's groceries website for the specified category and pages, then save the data to JSON files in the json_database directory.

## Configuration
- *foodType*: Change the food category to scrape. Modify the foodType variable in the tescoScraperMultiPage.py script.
- *pageNumbers*: Adjust the range of page numbers to scrape. Modify the pageNumbers variable in the tescoScraperMultiPage.py script.
## File Structure
```
TescoScraper/
│
├── tescoScraperMultiPage.py
├── requirements.txt
└── json_database/
```
- scraper.py: Main script to run the scraper.
- requirements.txt: List of required Python packages.
- json_database/: Directory where JSON files are saved.
## Notes
Ensure that ChromeDriver is compatible with your version of Google Chrome.
If running in a headless environment, uncomment the headless option in the Chrome options configuration.
## License
This project is licensed under the MIT License.
