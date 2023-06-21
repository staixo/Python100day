import requests
from bs4 import BeautifulSoup

def scrape_crypto_prices():
    # Send a GET request to the CoinMarketCap website
    response = requests.get('https://coinmarketcap.com')

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the crypto prices
    table = soup.find('table', class_='cmc-table')

    # Extract the rows from the table
    rows = table.find_all('tr')

    # Iterate over the rows and extract the data
    for row in rows[1:]:  # Skip the header row
        columns = row.find_all('td')
        name = columns[2].text.strip()
        price = columns[3].text.strip()
        print(f'{name}: {price}')

# Call the function to scrape crypto prices
scrape_crypto_prices()
