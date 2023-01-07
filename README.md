# LTMPT-Scraper

## Overview
A web scraper program to retrieve data on the top 1000 schools based on UTBK scores in 2022 using Scrapy

URL: https://top-1000-sekolah.ltmpt.ac.id

Website:
<img width="1552" alt="image" src="https://user-images.githubusercontent.com/74947224/211157991-19095918-a2fc-4f74-b0ff-e98b5e756002.png">


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
