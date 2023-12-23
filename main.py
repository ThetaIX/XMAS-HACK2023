import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads
import Models
from Models.RoadNetwork import RoadNetwork
from Models.RouterArray import RouterArray

def main():


    # Загрузка данных из Excel-файлов
    Roads = RoadNetwork('input/road_network.xlsx')
    Routers = RouterArray('input/wifi_routers.xlsx')

    # Преобразование данных в GeoDataFrame
    
    gdf1 = gpd.GeoDataFrame(df1, geometry=gpd.GeoSeries(['geom'].apply(loads)))
    gdf2 = gpd.GeoDataFrame(df2, geometry=gpd.GeoSeries(df2['geom'].apply(loads)))

    # Визуализация данных
    fig, ax = plt.subplots(figsize=(10, 10))

    # Визуализация первой таблицы
    # gdf1.plot(ax=ax, color='blue', linewidth=2, label='Table 1')

    # Визуализация второй таблицы
    gdf2.plot(ax=ax, color='red', markersize=50, label='Table 2', marker='o')

    # Отображение карты
    plt.title('Географическая визуализация данных')
    plt.legend()
    plt.show()