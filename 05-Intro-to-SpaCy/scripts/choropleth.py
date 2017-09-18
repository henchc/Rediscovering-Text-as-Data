def us_choropleth(t):
    import matplotlib.cm
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    from matplotlib.colors import Normalize
    import shapefile
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    import random
    import pandas as pd
    from collections import Counter

    plt.title("NER", fontsize=12)

    us_locations_map = Basemap(
        resolution="l",
        llcrnrlon=-128.94,
        llcrnrlat=23.52,
        urcrnrlon=-60.12,
        urcrnrlat=50.93,
        lat_0=37.26,
        lon_0=-94.53)
    us_locations_map.drawmapboundary(
        fill_color="#46bcec")  # Fills in the oceans
    us_locations_map.fillcontinents(
        color="#eabc77",
        lake_color="#46bcec")  # Defines the continents
    us_locations_map.drawcoastlines()

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(15.5, 12.5)  # Sets the size of the map

    # Converts the coordinates to map points
    lons, lats = us_locations_map(t["longitude"], t["latitude"])
    us_locations_map.scatter(
        lons,
        lats,
        color="black",
        zorder=10)  # Draws the points on the map

    # Labels each point with the location name
    for i in range(t.num_rows):
        lat_lon = (
            t.row(i).item("longitude") + .2,
            t.row(i).item("latitude") - .1)
        plt.annotate(np.array(t.row(i).item("name")), lat_lon, fontsize=10)

    # Here we are reading in a shape file, which places state boundary
    # information for our Basemap
    us_locations_map.readshapefile(
        "data/us_shapefiles/cb_2016_us_state_20m", "us_states")

    state_names = []
    for shape_dict in us_locations_map.us_states_info:
        state_names.append(shape_dict['NAME'])

    ax = plt.gca()  # get current axes instance
    cmap = plt.get_cmap('Reds')

    names = []
    shapes = []
    counts = []

    state_counts = Counter(t["state"])

    for index, state in enumerate(state_names):
        seg = us_locations_map.us_states[index]
        poly = Polygon(seg)
        names.append(state)
        shapes.append(poly)
        if state in t['state']:
            counts.append(state_counts[state])
        else:
            counts.append(0)

    # Loading our lists into the DataFrame
    shape_table = pd.DataFrame()
    shape_table["State Name"] = np.array(names)
    shape_table["Shapes"] = np.array(shapes)
    shape_table["Count"] = np.array(counts)

    pc = PatchCollection(shape_table["Shapes"], zorder=2)
    norm = Normalize()

    pc.set_facecolor(cmap(norm(shape_table['Count'].fillna(0).values)))
    pc.set_edgecolor("black")
    ax.add_collection(pc)

    # Adds colorbar showing the scale
    mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
    mapper.set_array(shape_table['Count'])
    plt.colorbar(mapper, shrink=0.4)
