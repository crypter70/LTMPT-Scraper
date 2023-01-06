import scrapy


class DosenSpider(scrapy.Spider):
    name = "dosen-scraper"
    
    # initialize start request
    def start_requests(self):
        urls = []
        
        # get the url start from page 1 to page 175 
        for a in range (1, 2):

            # initialize url + page number 
            urll = 'https://sinta.kemdikbud.go.id/affiliations/authors/414?page=' + str(a)

            # assign to urls
            urls.append(urll)   

        # yield the url then callback to the parse function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # parse the profile link
    def parse(self, response):

        # yield the url to request then callback to parse_profile function
        # url taken from css selector
        for link in response.css('div.profile-name a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_profile)

    def parse_profile(self, response):

        # yield data using css selector to dictionary
        yield{
            'name' : response.css('body > div > div.col-md-8 > div.content > div > div.row.p-3 > div.col-lg.col-md > h3 > a::text').get(),
            'sinta_id' : response.css('body > div > div.col-md-8 > div.content > div > div.row.p-3 > div.col-lg.col-md > div.meta-profile > a:nth-child(5)::text').get().replace('SINTA ID :', '').replace(' ', ''),
            'dept' : response.css('body > div > div.col-md-8 > div.content > div > div.row.p-3 > div.col-lg.col-md > div.meta-profile > a:nth-child(3)::text').get().strip(),
            'sinta_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(2) > div.pr-num::text').get(),
            'sinta_3yr_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(4) > div.pr-num::text').get(),
            'affil_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(6) > div.pr-num::text').get(),
            'affil_3yr_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(8) > div.pr-num::text').get(),
            'scopus_h_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td.text-warning::text').get(),
            'gs_h_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td.text-success::text').get(),
            'wos_h_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td.text-primary::text').get(),
            'scopus_i10_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td.text-warning::text').get(),
            'gs_i10_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td.text-success::text').get(),
            'wos_i10_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td.text-primary::text').get(),
            'scopus_g_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(6) > td.text-warning::text').get(),
            'gs_g_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(6) > td.text-success::text').get(),
            'wos_g_index' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(6) > td.text-primary::text').get(),
            'scopus_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.text-warning::text').get(),
            'scopus_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td.text-warning::text').get(),
            'scopus_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td.text-warning::text').get(),
            'gs_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.text-success::text').get(),
            'gs_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td.text-success::text').get(),
            'gs_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td.text-success::text').get(),
            'wos_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.text-primary::text').get(),
            'wos_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td.text-primary::text').get(),
            'wos_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td.text-primary::text').get()
            # 'article_q1' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[0].strip(),
            # 'article_q2' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[1].strip(),
            # 'article_q3' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[2].strip(),
            # 'article_q4' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[3].strip(),
            # 'article_undefined_q' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[4].strip(),
            # 'articles_ro' : re.findall("data: (.+?)]\n", response.body.decode("utf-8"), re.S)[5],
            # 'conference_ro' : re.findall("value:(.+?),", response.body.decode("utf-8"), re.S)[7].replace('[\n', '').replace(' ', ''),
            # 'conference_ro' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[6],
            # 'other_ro' : re.findall("value:(.+?),\n", response.body.decode("utf-8"), re.S)[7],
        }