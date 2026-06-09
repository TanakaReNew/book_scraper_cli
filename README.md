# Books Scraper CLI Tool

## Overview

This is a Python-based command-line tool that scrapes book data from the website **books.toscrape.com** and saves it into an organised CSV file.

It extracts:

* Book title
* Price
* Star rating

---

## Features

* Scrapes multiple pages of book listings
* Converts star ratings into numeric values
* Saves clean data into a CSV file
* Simple CLI interface using argparse

---

## How it works

1. The user specifies how many pages to scrape
2. The script collects book data from each page
3. Data is combined into a single dataset
4. Results are saved into `books.csv`

---

## How to run

```bash
python scraper.py --pages 5
```

---

## Output

A file called `books.csv` with the following structure:

| Title     | Price  | Star rating |
| --------- | ------ | ----------- |
| Olio      | £23.88 | 1           |

---

## Tech Stack

* Python
* Requests
* BeautifulSoup (bs4)
* CSV module
* argparse

---

## Future improvements

* Filter books by rating
* Save to JSON/Excel
* Add error handling for network issues
