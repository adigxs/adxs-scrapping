# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#from scrapy_djangoitem import DjangoItem
#from loadingd.models import Website


# class WebsiteItem(DjangoItem):
#     django_model = Website


import scrapy


class ScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DurrellProductItem(scrapy.Item):
    site = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    price_init = scrapy.Field()
    price_red = scrapy.Field()
    url = scrapy.Field()
    store_name = scrapy.Field()
    fone_s = scrapy.Field()
