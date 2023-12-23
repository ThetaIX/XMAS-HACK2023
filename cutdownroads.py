import pandas as pd
import matplotlib.pyplot as plt

def cut():
    """
    docstring
    """
    eps = 0.004
    roads = open('input/road_network.csv', 'r').read().splitlines()
    routers = open('input/wifi_routers.csv', 'r').read().splitlines()
    roads_cut = open('input/road_network_cut.csv', 'w+')
    mxx = 20
    mnx = 60
    mxy = 20
    mny = 60
    roads_cut.write(roads[0] + '\n')
    for router in routers[1:]:
        x, y = router.split(';')[1][7:-1].split()
        x = float(x)
        y = float(y)
        if mxx < x: mxx = x  # noqa: E701
        if mnx > x: mnx = x  # noqa: E701
        if mxy < y: mxy = y  # noqa: E701
        if mny > y: mny = y  # noqa: E701
    
    mxx += eps
    mnx -= eps
    mxy += eps
    mny -= eps
    print(f"X: ({mxx}, {mnx})   Y: ({mxy}, {mny})")
    for road in roads[1:]:
        coo = road.split(';')[0][13:-2].split(',')[0].split()
        if mxx < float(coo[0]) or mnx > float(coo[0]) or mxy < float(coo[1]) or mny > float(coo[1]):
            continue
        roads = road.split(';')
        s = f'{roads[0][1:-1]};{roads[1][1:-1]};{roads[2][1:-1]};{roads[3][1:-1]};{roads[4]}\n'
        roads_cut.write(s)

cut()