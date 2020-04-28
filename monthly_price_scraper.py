import requests
import logging
import csv
import calendar
from bs4 import BeautifulSoup

def get_monthly_prices():
    monthly_data_url = 'https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm'

    page = requests.get(monthly_data_url)

    logging.info(f'Getting content from {monthly_data_url}')

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="html.parser")
        tables = soup.find_all('table')
        data_table = tables[5]

        data_rows = data_table.findChildren('tr', recursive=False)

        with open('data/monthly-prices.csv', mode='w') as monthly_prices_file:
            monthly_prices_writer = csv.writer(monthly_prices_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            monthly_prices_writer.writerow(['Date', 'Price'])

            # getting rid of empty string as the first element of the iterable
            months = list(calendar.month_abbr)[1:]

            for row in data_rows[1:]:
                cells = row.findChildren('td', recursive=False)
                year = cells[0].text.strip()

                if year:
                    for data_cell, month in zip(cells[1:], months):
                        date = f'{year}-{month}-01'
                        monthly_prices_writer.writerow([date, data_cell.text.strip()])

            logging.info(f'Monthly gas prices saved successfully.')


    else:
        logging.error('Page cannot be accessed at the moment')
