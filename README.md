# LTMPT-Scraper

## Overview
The program aimed to extract data on the top 1000 schools based on UTBK scores in 2022 using Scrapy. The targeted website was a static one, and the data was not loaded using JavaScript. Therefore, Scrapy was an appropriate choice due to its efficiency and speed in handling static data on websites. The program extracted relevant data such as the schools' names, locations, UTBK scores, and other relevant information. The extracted data was useful for analyzing and evaluating the schools' academic performance and ranking. The data was saved in CSV format for further processing and analysis.

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
