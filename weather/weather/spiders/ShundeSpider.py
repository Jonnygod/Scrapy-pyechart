# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
import sys
import time
import codecs
import os
import csv
from weather.resource import citys
from weather.resource import city
from weather.resource import shis

class ShundespiderSpider(scrapy.Spider):
    name = 'ShundeSpider'
    allowed_domains = ['tianqi.com']  #域范围\
    try:
        first = int(input("查询天气：1:全国(包活区) 2:单独城市 3:全市\n"))
        if first == 1:
            num = 1
        elif first == 3:
            num = 3
        else:
            num = input("直接输入你想查询城市(区)的拼音如：beijing\n输入：")
    except:
        print("请输入正确的格式")
        time.sleep(1)
        sys.exit(-1)
    start_urls = []
    if num == 1:
        for each in citys:
            start_urls.append("https://www.tianqi.com/" + each)
    elif num == 3:
        for each2 in shis:
            start_urls.append("https://www.tianqi.com/" + each2)
    else:
        if num in city.keys() == True:
            url = "https://www.tianqi.com/" + city[num]
            start_urls.append(url)
        else:
            print("你所输入的城市不存在")
            time.sleep(1)
            sys.exit(-1)




    def parse(self, response):
        items = []
        city = response.xpath('//dd[@class="name"]/h2/text()').extract()
        selectors = response.xpath('//div[@class="day7"]')
        date = selectors.xpath('ul[@class="week"]/li/b/text()').extract()
        week = selectors.xpath('ul[@class="week"]/li/span/text()').extract()
        wind = selectors.xpath('ul[@class="txt"]/li/text()').extract()
        weather = selectors.xpath('ul[@class="txt txt2"]/li/text()').extract()
        temperatureMax = selectors.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()
        temperatureMin = selectors.xpath('div[@class="zxt_shuju"]/ul/li/b/text()').extract()
        for i in range(7):
            item = WeatherItem()
            try:
                item['city'] = city[0]
                item['Date'] = date[i]
                item['week'] = week[i]
                item['wind'] = wind[i]
                item['weather'] = weather[i]
                item['temperatureMax'] = temperatureMax[i]
                item['temperatureMin'] = temperatureMin[i]
                item['temperature'] = temperatureMin[i] + '~' + temperatureMax[i]
            except:
                sys.exit(-1)
            items.append(item)
        return items





