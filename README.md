# LTMPT-Scraper

## Overview
A web scraper program to retrieve data on the top 1000 schools based on UTBK scores in 2022 using Scrapy

URL : https://top-1000-sekolah.ltmpt.ac.id

image.png

## Official Docs
Scrapy Documentation
https://scrapy.org/

## Installation
```
pip install scrapy
pip3 install scrapy
```

## Run Program
    scrapy runspider scraper.py
    
## Export Data
### csv
    scrapy runspider scraper.py -o data.csv

### json
    scrapy runspider scraper.py -o data.json