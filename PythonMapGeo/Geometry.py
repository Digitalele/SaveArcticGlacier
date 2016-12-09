import shapely.geometry
import pyproj

# Set up projections
p_ll = pyproj.Proj(init='epsg:4326')
p_mt = pyproj.Proj(init='epsg:3857') # metric;

# Create corners of rectangle to be transformed to a grid
nw = shapely.geometry.Point((75.0, -89.0))
se = shapely.geometry.Point((84.0, -10.0))

stepsize = 5000 # 5 km grid step size

# Project corners to target projection
s = pyproj.transform(p_ll, p_mt, nw.x, nw.y) # Transform NW point to 3857
e = pyproj.transform(p_ll, p_mt, se.x, se.y) # same for SE

# Iterate over 2D area
gridpoints = []
x = s[0]
while x < e[0]:
    y = s[1]
    while y < e[1]:
        p = shapely.geometry.Point(pyproj.transform(p_mt, p_ll, x, y))
        gridpoints.append(p)
        y += stepsize
    x += stepsize

# Print in csv
with open('testout.csv', 'wb') as of:
    of.write('lon,lat\n')
    for p in gridpoints:
        of.write('{:f},{:f}&zoom=8&size=600x600\n'.format(p.x, p.y))