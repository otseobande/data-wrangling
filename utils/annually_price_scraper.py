import requests
import logging
import csv
import calendar
from bs4 import BeautifulSoup

def get_annually_prices():
    annually_data_url = 'https://www.eia.gov/dnav/ng/hist/rngwhhdA.htm'

    page = requests.get(annually_data_url)

    logging.info(f'Getting content from {annually_data_url}')

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="html.parser")
        tables = soup.find_all('table')
        data_table = tables[5]

        data_rows = data_table.findChildren('tr', recursive=False)

        with open('data/annually-prices.csv', mode='w') as annually_prices_file:
            annually_prices_writer = csv.writer(annually_prices_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            annually_prices_writer.writerow(['Date', 'Price'])

            for row in data_rows[1:]:
                cells = row.findChildren('td', recursive=False)
                year = int(cells[0].text.strip()[:-2])

                for data_cell in cells[1:]:
                    date = f'{year}-Dec-31'
                    year += 1

                    annually_prices_writer.writerow([date, data_cell.text.strip()])

            logging.info(f'Annually gas prices saved successfully.')

    else:
        logging.error('Page cannot be accessed at the moment')
