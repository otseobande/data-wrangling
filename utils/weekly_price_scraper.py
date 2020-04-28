import requests
import logging
import csv
import calendar
from bs4 import BeautifulSoup

def get_weekly_prices():
    weekly_data_url = 'https://www.eia.gov/dnav/ng/hist/rngwhhdW.htm'

    page = requests.get(weekly_data_url)

    logging.info(f'Getting content from {weekly_data_url}')

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="html.parser")
        tables = soup.find_all('table')
        data_table = tables[5]

        data_rows = data_table.findChildren('tr', recursive=False)

        with open('data/weekly-prices.csv', mode='w') as weekly_prices_file:
            weekly_prices_writer = csv.writer(weekly_prices_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            weekly_prices_writer.writerow(['Date', 'Price'])

            for row in data_rows[2:]:
                cells = row.findChildren('td', recursive=False)
                date_cell = cells[0]

                for i in range(1, len(cells) - 1, 2):
                    date = f'{date_cell.text.strip()}-{cells[i].text.strip()[-2:]}'
                    data = cells[i+1].text.strip()

                    if data:
                        weekly_prices_writer.writerow([date, data])

            logging.info(f'Weekly gas prices saved successfully.')


    else:
        logging.error('Page cannot be accessed at the moment')
