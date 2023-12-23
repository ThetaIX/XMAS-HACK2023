import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads

class Router(object):
    def __init__(self, dataString):
        dataList = dataString.split(';')
        self.guid = dataList[1]
        self.geom = dataList[2]
