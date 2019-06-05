
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

import matplotlib.pyplot as plt
import numpy as np
''' This class is to draw 3D map using Basemap '''
# reference : https://buildmedia.readthedocs.org/media/pdf/basemaptutorial/latest/basemaptutorial.pdf

'''
class mpl_toolkits.basemap.Basemap
(llcrnrlon=None, llcrnrlat=None, urcrnrlon=None, urcrnrlat=None, llcrnrx=None,
llcrnry=None, urcrnrx=None, urcrnry=None, width=None, height=None, projection='cyl',
resolution='c', area_thresh=None, rsphere=6370997.0, ellps=None,
lat_ts=None, lat_1=None, lat_2=None, lat_0=None, lon_0=None, lon_1=None, lon_2=None,
o_lon_p=None, o_lat_p=None, k_0=None, no_rot=False, suppress_ticks=True, satellite_height=35786000,
boundinglat=None, fix_aspect=True, anchor='C', celestial=False, round=False, epsg=None, ax=None)
'''


class Map3D:

    def __init__(self, userdata):

        style.use('fivethirtyeight')
        self.userdata = userdata

    def draw3dMap(self):

        map = Basemap(projection='gall',

                      llcrnrlon=124.5,            # left longitude

                      urcrnrlon=129.7,            # right longitude

                      urcrnrlat=38.7,              # upper latitude

                      llcrnrlat=33.1,                # lower latitude

                      resolution='i',

                      area_thresh=200
                      )

        fig = plt.figure()
        ax = Axes3D(fig)
        print(self.userdata)
        ax.set_axis_on()
        ax.azim = 270
        ax.dist = 7

        polys = []
        for polygon in map.landpolygons:
            polys.append(polygon.get_coords())

        lc = PolyCollection(polys, edgecolor='black',
                            facecolor='#DDDDDD', closed=False)

        ax.add_collection3d(lc)
        ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
        ax.add_collection3d(map.drawcountries(linewidth=0.35))

        lons = list()
        lats = list()
        values = list()

        for eachUserdata in self.userdata:
            lons.append(eachUserdata[0])
            lats.append(eachUserdata[1])
            values.append(eachUserdata[2])

        lons = np.array(lons)
        print(lons)
        lats = np.array(lats)
        print(lats)
        values = np.array(values)

        x, y = map(lons, lats)

        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude')
        ax.set_zlabel('Value')

        ax.bar3d(x, y, values,
                 2, 2, 2, color='r', alpha=0.8)

    def show3Dmap(self):
        plt.show()
