# LTMPT-Scraper
A web scraper program to retrieve data on the top 1000 schools based on UTBK scores in 2022 using Scrapy

## Official Docs
https://scrapy.org/

## Installation
```
pip install scrapy
```

## Run Program
    scrapy runspider scraper.py
    
## Export Data
### csv
    scrapy runspider scraper.py -o data.csv

### json
    scrapy runspider scraper.py -o data.json