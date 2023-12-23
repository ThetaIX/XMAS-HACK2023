import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads

class Log(object):
    def __init__(self, dataString):
        dataList = dataString.split(';')
        self.guid = dataList[1]
        self.tm = dataList[2].split(' ')[0] + ' ' + dataList[2].split(' ')[1]
        self.router_mac = dataList[3]
        self.user_mac = dataList[4]
        self.signal = 1 if -24 <= int(dataList[5]) < -41 else 2 if -41<= int(dataList[5]) < -58 else 3
        self.router_id = dataList[6]
