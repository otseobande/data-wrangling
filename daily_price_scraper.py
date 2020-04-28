import requests
import logging
import csv
import calendar
from bs4 import BeautifulSoup

def get_daily_prices():
    url = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'

    page = requests.get(url)

    logging.info(f'Getting content from {url}')

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="html.parser")
        tables = soup.find_all('table')
        data_table = tables[5]

        data_rows = data_table.findChildren('tr', recursive=False)


        with open('data/daily-prices.csv', mode='w') as daily_prices_file:
            daily_prices_writer = csv.writer(daily_prices_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            daily_prices_writer.writerow(['Date', 'Price'])

            for row in data_rows[1:]:
                cells = row.findChildren('td', recursive=False)

                date_info = cells[0].text.strip()
                if date_info:
                    year = int(date_info[0:4])
                    start_month = date_info[5:8]
                    end_month = date_info[15:18]
                    start_day = int(date_info[9:11])
                    end_day = int(date_info[-2:])

                    dates = []
                    if end_day > start_day:
                        dates = [f'{year}-{start_month}-{day}' for day in range(start_day, end_day + 1)]
                    else:
                        _ , last_day_of_start_month = calendar.monthrange(
                            year,
                            list(calendar.month_abbr).index(start_month)
                        )

                        start_month_dates = [f'{year}-{start_month}-{day}' for day in range(start_day, last_day_of_start_month + 1)]
                        end_month_dates = [f'{year}-{end_month}-{day}' for day in range(1, end_day + 1)]
                        dates = start_month_dates + end_month_dates

                    for index, cell in enumerate(cells[1:]):
                        date = dates[index]
                        daily_prices_writer.writerow([date, cell.text.strip()])

            logging.info(f'Daily gas prices saved successfully.')


    else:
        logging.error('Page cannot be accessed at the moment')
