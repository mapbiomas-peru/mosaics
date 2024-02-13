#!/usr/bin/env python

import ee, folium
ee.Initialize()

def addLayer(eeObject, visParams={}, name='layer'):
    """Function to view Google Earth Engine tile layer as a Folium map.
    
    Parameters
        m (object): Folium map
        eeObject (ee.Object): Earth Engine Object.
        visParams (dict): Dictionary with visualization parameters.
        name (str): Layer name.
    
    Returns:
    """
        
    mapid = eeObject.getMap(visParams)

    url = "https://earthengine.googleapis.com/map/{mapid}/{{z}}/{{x}}/{{y}}?token={token}"

    tiles = url.format(**mapid)

    m = folium.Map(zoom_start=8, tiles='Cartodb dark_matter')

    # rgb layer
    folium.raster_layers.TileLayer(
        tiles = tiles,
        attr = 'Google Earth Engine',
        name = name,
        max_zoom = 20,
        subdomains = ['mt0', 'mt1', 'mt2', 'mt3'],
        overlay = True,
        control = True,
    ).add_to(m)

    return m