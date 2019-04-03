import csv
import time
import codecs
import os

class pipelines2Csv(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        dirs = './views'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        fileName = './views/'+today+".csv"
        with codecs.open(fileName,'a','utf-8-sig') as fp:
            writer = csv.writer(fp)
            writer.writerow((item['Date'],item['city']+"市", item['temperatureMax'], item['temperatureMin'],item['wind']))
        fp.close()
        return item
