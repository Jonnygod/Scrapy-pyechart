# -*- coding: utf-8 -*-

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from weather.resource import UserAgents
from weather.resource import PROXIES
import random

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self,request,spider):
        ua = random.choice(UserAgents)
        # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        request.headers.setdefault('User-Agent',ua)

class CustomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = proxy