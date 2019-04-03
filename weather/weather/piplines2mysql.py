# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class WeatherPipeline(object):
    def process_item(self, item, spider):
        city = item['city']
        Date1 = item['Date']
        week = item['week']
        weather = item['weather']
        temperature = item['temperature']
        wind = item['wind']

        conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '1234',
            db = 'discount',
            charset = 'utf8')
        cur = conn.cursor()
        mysqlCmd = "insert into weather(Date1,city,week,temperature,weather,wind) values('%s','%s','%s','%s','%s','%s');" %(city,Date1,week,temperature,weather,wind)
        cur.execute(mysqlCmd)
        cur.close()
        conn.commit()
        conn.close()

        return item

