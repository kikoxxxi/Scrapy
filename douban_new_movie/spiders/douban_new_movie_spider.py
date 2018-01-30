from scrapy.spiders import Spider
from scrapy.selector import Selector
from douban_new_movie.items import DoubanNewMovieItem
from scrapy.http import Request

class DoubanNewMovieSpider(Spider):
    name="douban_new_movie_spider"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    def start_requests(self):
        return [Request(url='http://movie.douban.com/chart',
                        callback=self.parse, headers=self.headers)]
    def parse(self, response):
        sel=Selector(response)
        
        movie_name=sel.xpath("//div[@class='pl2']/a/text()").extract()
        movie_url=sel.xpath("//div[@class='pl2']/a/@href").extract()
        movie_star=sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()
        
        item=DoubanNewMovieItem()
        
        item['movie_name']=[n.encode('utf-8') for n in movie_name if n !='\n                    ']
        item['movie_url']=[n for n in movie_url]
        item['movie_star']=[n for n in movie_star]
        
        yield item
        
        print movie_name