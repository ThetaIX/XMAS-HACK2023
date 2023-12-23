import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads

class Road(object):
    def __init__(self, dataString):
        dataList = dataString.split(',')
        self.geom = dataList[0]
        self.fromVertex = dataList[1]
        self.toVertex = dataList[2]
        self.weights = dataList[3]