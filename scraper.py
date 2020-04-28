import argparse
import logging
from daily_price_scraper import get_daily_prices
from weekly_price_scraper import get_weekly_prices
from monthly_price_scraper import get_monthly_prices
from annually_price_scraper import get_annually_prices

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    periods = ['daily', 'weekly', 'monthly', 'annually']

    parser = argparse.ArgumentParser(description='Get Natural Gas Prices')
    parser.add_argument(
        '-p',
        '--period',
        help='Period to get prices for. Can be Daily, Weekly, Monthly or Annually',
        default='daily',
        choices=periods
    )

    args = parser.parse_args()

    selected_period = args.period.lower()

    if selected_period == 'daily':
        get_daily_prices()
    elif selected_period == 'weekly':
        get_weekly_prices()
    elif selected_period == 'monthly':
        get_monthly_prices()
    elif selected_period == 'annually':
        get_annually_prices()
