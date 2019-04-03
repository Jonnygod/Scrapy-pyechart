import pandas as pd
from pyecharts import Page,Grid,Line,Map
from weather.resource import pro
import time

today = time.strftime('%Y%m%d',time.localtime())
filePath = '../views/' + today + ".csv"
# df = pd.read_csv(filePath,usecols=['Date','City','Max','Min'])
# df = pd.read_csv(filePath)
dd = pd.read_csv(filePath,names=['Date','City','Max','Min','Wind'])
grouper = dd.groupby([dd['City']]).mean().round(1)
grouper.to_csv('./Result.csv',encoding='utf_8_sig')

Pros = str(input('哪个省：'))
df = pd.read_csv('./Result.csv')

page = Page()
for Pro in pro:
    map = Map(Pro,  title_color="#fff", background_color='#404a59')   #, title_pos="center"
    map.add("平均最高温度", df.City, df.Max, maptype=Pro,visual_text_color='#000',is_visualmap=True, is_label_show=True,visual_range=[-5,30],legend_text_color='red')
    map.add("平均最低温度", df.City, df.Min, maptype=Pro,visual_text_color='#000',is_visualmap=True, is_label_show=True,visual_range=[-20,30],legend_text_color='red')
    page.add(map)
# grid = Grid()
# grid.add(map, grid_left="left")
# grid.add(map, grid_right="right")
# grid.render('01.html')

page.render('01.html')







