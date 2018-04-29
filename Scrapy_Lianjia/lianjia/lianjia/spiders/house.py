# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import random
import time
from ..items import LianjiaItem,LianjiaItemLoader

class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['nj.lianjia.com/ershoufang']
    start_urls = ['https://nj.lianjia.com/ershoufang/pg{0}/'.format(x) for x in range(1,101)]

    headers = {
                'Host':'nj.lianjia.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }
    custom_settings = {
            'DOWNLOAD_DELAY':1.5,
            'COOKIES_ENABLED':False,
            'DEFAULT_REQUEST_HEADERS':headers
        }


    def parse(self, response):

        links = response.css('ul.sellListContent li.clear')
        for link in links:
            house_url = link.css('a::attr(href)').extract_first()
            sleep_time = random.randint(2,3) + random.random()
            time.sleep(sleep_time)
            yield Request(url=house_url,callback=self.parse_house,dont_filter=True)


    def parse_house(self,response):

        item_loader = LianjiaItemLoader(item = LianjiaItem(),response=response)
        item_loader.add_css('title','.title-wrapper .content .title h1::text')
        item_loader.add_css('community_name','.communityName a::text')
        item_loader.add_css('room_type','.houseInfo .room .mainInfo::text')
        item_loader.add_css('room_floor','.houseInfo .room .subInfo::text')
        item_loader.add_css('room_direction','.houseInfo .type .mainInfo::text')
        item_loader.add_css('room_area','.houseInfo .area .mainInfo::text')
        item_loader.add_css('unti_price','span.unitPriceValue::text')
        item_loader.add_css('room_year','.houseInfo .area .subInfo::text')
        item_loader.add_css('room_decoration','.houseInfo .type .subInfo::text')
        item_loader.add_css('room_location','.areaName span.info a:first-child::text')

        house = item_loader.load_item()
        yield house