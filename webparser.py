import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'https://www.blockchain.com/explorer/prices'

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An error occurred while requesting the URL: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
name = soup.find_all(class_="sc-89fc2ff1-5 fYsYrO")
price = soup.find_all(class_="sc-89fc2ff1-0 iQXnyB")
market_cap = soup.find_all(class_="sc-89fc2ff1-11 cBoudl")
volume_24h = soup.find_all(class_="sc-89fc2ff1-16 jBxFfE")
supply = soup.find_all(class_="sc-89fc2ff1-17 pyRes")

parsed_info = []

for names, prices, market_caps, volumes, supplies in zip(name, price, market_cap, volume_24h, supply):
    parsed_info.append((names.text.strip(), prices.text.strip(), market_caps.text.strip(), volumes.text.strip(), supplies.text.strip()))


current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d_%H-%M")

filename = f"blockchain_{timestamp}.csv"
try:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Market Cap', 'Volume(24h)', 'Circulating Supply'])
        
        for info in parsed_info:
            writer.writerow(info)

    print(f"Data has been written to {filename}.")
except IOError as e:
    print(f"An error occurred while writing to the CSV file: {e}")


#sc-89fc2ff1-5 fYsYrO    - coin names
#sc-89fc2ff1-0 iQXnyB    - coin prices
#sc-89fc2ff1-11 cBoudl   - market cap
#sc-89fc2ff1-12 gyTnri   - 1hour +
#sc-89fc2ff1-12 gDkPkJ   - 1hour -
#sc-89fc2ff1-12 eqrrWH   - 1hour 0
#sc-89fc2ff1-16 jBxFfE   - volume 24h
#sc-89fc2ff1-17 pyRes    - circulating supply