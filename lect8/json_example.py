import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

FILE_IN = 'lect8\\1.0_day_in.json'
FILE_OUT = 'lect8\\1.0_day_out.json'
FILE_HTML = 'lect8\\1.0_day_out.html'

with open(FILE_IN, 'r', encoding='utf-8') as f:
    all_days = json.load(f)

# with open(FILE_OUT, 'w') as f:
#     json.dump(all_days, f, indent=4)

# print(all_days['features'][0])
# print(all_days['features'][0]['properties'])
# print(all_days['features'][0]['properties']['mag'])
# print(all_days['features'][0]['properties']['title'])
# print(all_days['features'][0]['geometry']['coordinates'])
# print(len(all_days['features']))


mags = []
titles = []
# coordinates = []
lons, lats = [], []
for i in range(0, len(all_days['features'])):
    mags.append(all_days['features'][i]['properties']['mag'])
    titles.append(all_days['features'][i]['properties']['title'])
    lons.append(all_days['features'][i]['geometry']['coordinates'][0])
    lats.append(all_days['features'][i]['geometry']['coordinates'][1])
    # coordinates.append(all_days['features'][i]['geometry']['coordinates'])
# print(mags[:10])
# print(lons[:10])
# print(lats[:10])
# print(titles[:10])
# # print(coordinates[:10])
title = all_days['metadata']['title']
# print(title)
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'reversescale': True,
        # 'colorscale': 'Viridis',
        'colorbar': {'title': 'Magnitude'},
    }
}]
layout = Layout(title=title)
fig = {'data': data, 'layout': layout}
offline.plot(fig, filename=FILE_HTML)
