import requests
from bs4 import BeautifulSoup
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred for {url}: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred for {url}: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred for {url}: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred for {url}: {req_err}")
    return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    products = []
    # The selector might need adjustments based on the actual HTML structure of the page
    for product in soup.select('a._1fQZEK'):
        name = product.select_one('div._4rR01T').get_text(strip=True)
        price = product.select_one('div._30jeq3._1_WHN1').get_text(strip=True)
        products.append({'name': name, 'price': price})
    
    
    
    return products



    
def scrape_website(urls):
    all_products = []
    
    for url in urls:
        html_content = fetch_page(url)
        if html_content:
            products = parse_html(html_content)
            all_products.extend(products)
        
        #time.sleep(random.uniform(1, 3))
    
    return all_products

def main():
    urls = [
        'https://www.flipkart.com/',
    ]
    
    all_products = scrape_website(urls)
    
    
    for product in all_products:
        print(f"Product Name: {product['name']}, Price: {product['price']}")

main()
