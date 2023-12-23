import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.wkt import loads
from Models.RoadNetwork import RoadNetwork
from Models.RouterArray import RouterArray

def main():


    # Загрузка данных из Excel-файлов
    Roads = RoadNetwork('input/road_network_cut.csv')
    Routers = RouterArray('input/wifi_routers.csv')

    # Преобразование данных в GeoDataFrame
    df1 = Roads.getDF()
    df2 = Routers.getDF()

    gdf1 = gpd.GeoDataFrame(df1, geometry=gpd.GeoSeries(df1['geom'].apply(loads)))
    gdf2 = gpd.GeoDataFrame(df2, geometry=gpd.GeoSeries(df2['geom'].apply(loads)))

    # Визуализация данных
    fig, ax = plt.subplots(figsize=(10, 10))

    # Визуализация первой таблицы
    gdf1.plot(ax=ax, color='gray', linewidth=2, label='Table 1', zorder=0)

    # Визуализация второй таблицы
    gdf2.plot(ax=ax, color='#FB62F6', markersize=50, label='Table 2', marker='o', zorder=1)

    # Отображение карты
    plt.title('Географическая визуализация данных')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

