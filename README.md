# LTMPT-Scraper

## Overview
A web scraper program to retrieve data on the top 1000 schools based on UTBK scores in 2022 using Scrapy.
The website to be scraped is a static website, data is not loaded using javascript. 
Therefore, Scrapy is a suitable choice because it has speed and efficiency for static data on websites.

URL: https://top-1000-sekolah.ltmpt.ac.id

Website:
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/74947224/211158299-7400a156-57a0-45c8-a5f9-6c608bb3c0d6.png">

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
