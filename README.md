# Blockchain Data Scraper

This Python script scrapes data from the website [blockchain.com](https://www.blockchain.com/explorer/prices) and saves the data to a CSV file. The scraped data includes coin names, prices, market caps, volume (24h), and circulating supply.

## Requirement

- Python 3 
- Requests library: `pip install requests`
- BeautifulSoup library: `pip install beautifulsoup4`
- csv module
- datetime module

## Usage

1. Clone the repository or download the script file.

2. Open the script file `blockchain_scraper.py`.

3. Modify the `url` variable if necessary. By default, it is set to 'https://www.blockchain.com/explorer/prices'.

4. Run the script by executing the command `python blockchain_scraper.py` in the terminal.

5. The script will fetch the data from the website and save it to a CSV file named 'blockchain_<timestamp>.csv', where `<timestamp>` represents the current date and time (e.g., `blockchain_2023-06-05_15-30.csv`).

6. Check the console output for success or error messages.

## Data Fields

The script extracts the following data fields from the website:

- Coin names: class `sc-89fc2ff1-5 fYsYrO`
- Coin prices: class `sc-89fc2ff1-0 iQXnyB`
- Market cap: class `sc-89fc2ff1-11 cBoudl`
- Volume (24h): class `sc-89fc2ff1-16 jBxFfE`
- Circulating supply: class `sc-89fc2ff1-17 pyRes`

## Additional info for parsing from blockchain.com:
- `sc-89fc2ff1-5 fYsYrO`    - coin names
- `sc-89fc2ff1-0 iQXnyB`    - coin prices
- `sc-89fc2ff1-11 cBoudl`   - market cap
- `sc-89fc2ff1-12 gyTnri`   - 1hour +
- `sc-89fc2ff1-12 gDkPkJ`   - 1hour -
- `sc-89fc2ff1-12 eqrrWH`   - 1hour 0
- `sc-89fc2ff1-16 jBxFfE`   - volume 24h
- `sc-89fc2ff1-17 pyRes`    - circulating supply

## Error Handling

The script includes error handling to handle potential errors during the scraping process. If an error occurs while requesting the URL or writing to the CSV file, an appropriate error message will be displayed.

Feel free to explore and modify the script according to your needs.

