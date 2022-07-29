import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import contextily as ctx
from shapely import geometry
from shapely.ops import cascaded_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords
coords = np.load("well_vertices.npy", 'r')
boundary = np.load("boundary.npy",'r') 

c = np.array([(i[0], i[1]) for i in coords])

s = geometry.Polygon(boundary)
print("c = ", c)
print("s = ", s)
region_polys, region_pts = voronoi_regions_from_coords(c, s)

fig, ax = subplot_for_map(figsize=(18, 16))
plot_voronoi_polys_with_points_in_area(ax, s, region_polys, c, region_pts)
plt.show()

def get_voronoi_graph(vertices, boundary_edges):
    v_graph = [[[]]]
    
    return v_graph


def print_voronoi(v_graph):
    fig,ax = plt.subplots()
    plt.show()
