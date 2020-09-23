import scrapy
from scrapy import Spider
from scrapy import Selector
from Steam.items import SteamItem
from scrapy.spiders import CrawlSpider
    
class JuegosSpider(CrawlSpider):
    name = 'juegos'
    allowed_domains = ['steampowered.com']
    start_urls = [
    "https://store.steampowered.com/search/?sort_by=Released_DESC&sort_order=DESC&page=%d" % i for i in range(1,2845)]


    def parse(self, response):
    	games=Selector(response).xpath('//*[@id="search_resultsRows"]/a')
    	for game in games:
    		item=SteamItem()
    		item['nombre']=game.xpath('div[2]/div[1]/span/text()').extract()[0]
    		item['link']=game.xpath('@href').extract()[0]
    		item['fecha']=game.xpath('div[2]/div[2]/text()').extract()[0]
    		item['precio']=game.xpath('div[2]/div[4]/div[2]/text()').extract()[0]
    		yield item
//*[@id="search_resultsRows"]/a[39]