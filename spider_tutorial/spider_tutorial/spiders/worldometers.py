                          ##### USING BASIC FORMAT #####

import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
       # Extracting "a" elements for each country
        countries = response.xpath('//td/a')

        # Looping through the countries list
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url=link,callback=self.parse_country, meta={'country':country_name})  # sending a request with the relative url
    
    def parse_country(self, response):
        
        country = response.request.meta['country']
        rows= response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population= row.xpath('.//td[2]/strong/text()').get()

            yield {
                
                'country': country,
                'year': year,
                'population':population,
                
            }

       ##### HERE YOU HAVE TO WRITE scrapy crawl (name of the file) to execute it #####
       # scrapy crawl worldometers