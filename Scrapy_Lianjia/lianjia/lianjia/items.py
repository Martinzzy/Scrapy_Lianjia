# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import re
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,MapCompose,Join

def get_num(value):
    result = re.match('(\d+)',value).group(1)
    return int(result)


def get_intnum(value):
    return int(value)


class LianjiaItemLoader(ItemLoader):

    default_output_processor = TakeFirst()


class LianjiaItem(scrapy.Item):

    title = scrapy.Field()

    community_name = scrapy.Field()
    room_type = scrapy.Field()
    room_floor = scrapy.Field()
    room_direction = scrapy.Field()
    room_area = scrapy.Field(input_processor = MapCompose(get_num))
    unti_price = scrapy.Field(input_processor = MapCompose(get_intnum))
    room_year = scrapy.Field()
    room_decoration = scrapy.Field()
    room_location = scrapy.Field()

