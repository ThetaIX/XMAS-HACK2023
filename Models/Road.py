import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads

class Road(object):
    def __init__(self, dataString):
        dataList = dataString.split(';')
        self.geom = dataList[1]
        self.fromVertex = dataList[2]
        self.toVertex = dataList[3]
        self.weights = dataList[4]
