# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    city = scrapy.Field()
    Date = scrapy.Field()
    week = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
    img = scrapy.Field()
    temperatureMax = scrapy.Field()
    temperatureMin = scrapy.Field()

