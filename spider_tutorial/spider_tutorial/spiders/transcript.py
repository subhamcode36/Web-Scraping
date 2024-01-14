                                ##### CRAWL FORMAT #####
            ##### scrapy genspider -t crawl transcript subslikescript.com #####

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptSpider(CrawlSpider):
    name = "transcript"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies"]

    rules = (Rule(LinkExtractor(restrict_xpaths=('/html/body/div/div/main/article/ul/a')), callback="parse_item", follow=True),)
                                                 #this puts the direct link no need of href
    def parse_item(self, response):
       # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")

        # Extract the data we want and then yield it
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'url': response.url,
        }
### scrapy runspider transcript.py -o transcript.csv