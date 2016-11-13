from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from porn_spider.items import PornSpiderItem


class DoubanSpider(CrawlSpider):
    name = "porn_cl_spider"

    download_delay = 1

    allowed_domains = []

    start_urls = [
        'http://cl.miicool.info/thread0806.php?fid=22&search=&page=1'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'http://cl.miicool.info/thread0806.php\?fid=22&search=&page=[1]')),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):

        print response

        sel = Selector(response)
        item = PornSpiderItem()

        movie_name = sel.xpath("//h3/a/text()").extract()
        url = sel.xpath("//h3/a/@href").extract()

        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['url'] = [n.encode('utf-8') for n in url]

        yield item
