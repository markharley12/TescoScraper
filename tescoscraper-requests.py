import requests
from bs4 import BeautifulSoup

# URL of the Tesco groceries page
url = 'https://www.tesco.com/groceries/en-GB/shop/fresh-food/all?page=1&count=48'

try:
    # Send a GET request to the URL with a timeout
    response = requests.get(url, timeout=10)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the request with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements with the specified class names
        elements = soup.find_all('span', class_='styled__Text-sc-1i711qa-1 xZAYu ddsweb-link__text')
        
        # Extract and print the text from each element
        for element in elements:
            print(element.get_text())
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
