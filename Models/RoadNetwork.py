import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads
from Models.Road import Road

class RoadNetwork(object):
    def __init__(self, pas):
        self.roads = []
        with open(pas, 'r') as s:
            lines = s.readlines()
            for line in range(1, len(lines)):
                self.roads.append(Road(lines[line]))
                
    def getDF(self):
        self.dd = {"geom" : []}
        for a in self.roads:
            self.dd['geom'].append(a.geom)
        df = pd.DataFrame(self.dd)
        return df
