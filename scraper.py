import scrapy

class LTMPTScraper(scrapy.Spider):

    name="ltmpt-scraper"

    def start_requests(self):
        url = 'https://top-1000-sekolah.ltmpt.ac.id'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for data in response.css('tbody tr'):
            yield{
                'rank': data.css('td:nth-child(1)::text').get(),
                'rank_change' : data.css('td:nth-child(2)::text').get(),
                'npsn' : data.css('td:nth-child(3)::text').get(),
                'sekolah' : data.css('td:nth-child(4)::text').get(),
                'nilai_total' : data.css('td:nth-child(5)::text').get(),
                'provinsi' : data.css('td:nth-child(6)::text').get(),
                'kota_kab' : data.css('td:nth-child(7)::text').get(),
                'jenis_sekolah' : data.css('td:nth-child(8)::text').get()
            }

        # get the href of next button
        next_button = response.css('li.next a::attr(href)').get()

        # if the href of next button is exist, then follow that url
        if next_button is not None:
            yield response.follow(next_button, callback=self.parse)

    