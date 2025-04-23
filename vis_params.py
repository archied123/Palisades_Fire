#### Set the lists/dicts to display different band combinations & viewing parameters for GEEMAP

### Bands for S2 -------------------------------------------------------------------------
rgb = ['B4', 'B3', 'B2']
false_colour = ["B8", "B4", "B3"]

### S2 Imagery Vis -------------------------------------------------------------------------------
vis_rgb = {
    'min': 0.0,
    'max': 3000,
    'bands': rgb,
}

vis_false_colour = {
    'min': 0.0,
    'max': 3000,
    'bands': false_colour,
}

### Polygons -----------------------------------------------------------------------------
vis_small_polygon = {
    'color': 'white',   # Red border
    'width': 2,       # Border thickness
    'fillColor': '00000000'  # Transparent fill (hex RGBA: 00000000)
}

vis_large_polygon = {
    'color': 'red',   # Red border
    'width': 2,       # Border thickness
    'fillColor': '00000000'  # Transparent fill (hex RGBA: 00000000)
}

### NDVI ----------------------------------------------------------------------------
NDVI_vis_params = {
    'min': -0.2,
    'max': 1.0,
    'palette': ['#2c7bb6', '#d7191c', '#fdae61', '#a6d96a', '#1a9641', '#004529']
}

NDVI_legend_keys = [
    "Water / Non-Vegetated (< 0.0)",
    "Barren / Urban (0.0 – 0.2)",
    "Sparse Vegetation (0.2 – 0.4)",
    "Moderate Vegetation (0.4 – 0.6)",
    "Healthy Vegetation (0.6 – 0.8)",
    "Very Dense Vegetation (> 0.8)"
]

NDVI_legend_colors = [
    "#2c7bb6",
    "#d7191c",
    "#fdae61",
    "#a6d96a",
    "#1a9641",
    "#004529"
]

### nDVDI ----------------------------------------------------------------------------
dNDVI_vis_params = {
    'min': -0.5,
    'max': 0.5,
    'palette': ['#8c510a', '#d8b365', '#f6e8c3', '#c7eae5', '#5ab4ac', '#01665e']
}

dNDVI_legend_keys = [
    "Very High Loss (-0.5 – -0.2)",
    "High Loss (-0.2 – -0.1)",
    "Moderate Loss (-0.1 – 0.0)",
    "No Change (0.0 – 0.1)",
    "Moderate Gain (0.1 – 0.2)",
    "High Gain (0.2 – 0.5)"
]

dNDVI_legend_colors = [
    "#8c510a",  # Very High Loss
    "#d8b365",  # High Loss
    "#f6e8c3",  # Moderate Loss
    "#c7eae5",  # No Change
    "#5ab4ac",  # Moderate Gain
    "#01665e"   # High Gain
]

### dNBR ------------------------------------------------------------------
dNBR_vis_params = {
    'min': -0.5,
    'max': 1.0,
    'palette': [
        '#1a9850',  # dark green - enhanced regrowth
        '#91cf60',  # light green - unburned
        '#d9ef8b',  # yellow - low severity
        '#fee08b',  # light orange - moderate
        '#f46d43',  # orange - high
        '#d73027'   # red - extreme
    ]
}

dNBR_legend_keys = [
    "Enhanced Regrowth (< -0.1)",
    "Unburned (-0.1 – 0.1)",
    "Low Burn Severity (0.1 – 0.27)",
    "Moderate Burn Severity (0.27 – 0.44)",
    "High Burn Severity (0.44 – 0.66)",
    "Extreme Burn Severity (> 0.66)"
]

dNBR_legend_colors = [
    '#1a9850',
    '#91cf60',
    '#d9ef8b',
    '#fee08b',
    '#f46d43',
    '#d73027'
]
#-------------------------------------------------------------------------

### Burned/Unburned regions -------------------------------------------------
burned_region_params = {'min': -1, 
                        'max': 1, 
                        'palette': ['red']}

non_burned_region_params = {'min': -1, 
                            'max': 1, 
                            'palette': ['green']}