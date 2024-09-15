# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkScraperItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    technologies = scrapy.Field()
    salary = scrapy.Field()
    description = scrapy.Field()
