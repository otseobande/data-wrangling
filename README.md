# Henry Hub Gas Price Data Wrangler

This is a CLI tool that scrapes and saves Henry Hub gas prices for different time periods as CSV files.

## Requirements

Python 3.8+ is required to run this tool. You can download python from [here](https://www.python.org/downloads/)

## Installation

To install dependencies, simply run:

```bash
pip install -r requirements.txt
```

## Usage

The entry file for the tool is the `scraper.py` file. You can run it from your terminal with:

```bash
python scraper.py
```

By default, the tool would get `daily` prices but you can get prices for other time periods like Weekly, Monthly or Annually by passing a `-p` or `--period` argument. If I want to get and save annual gas prices I can simply run:

```bash
python scraper.py --period annually
```

For usage help run:

```bash
python scraper.py -h
```

Collected data is saved to a csv file in the data folder with this format: `{period}-prices.csv`. You should see a `daily-prices.csv` if the tool is run by default.
