import json

FILE_IN = 'lect8\\1.0_day_in.json'
FILE_OUT = 'lect8\\1.0_day_out.json'

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
coordinates = []
for i in range(0, len(all_days['features'])):
    mags.append(all_days['features'][i]['properties']['mag'])
    titles.append(all_days['features'][i]['properties']['title'])
    coordinates.append(all_days['features'][i]['geometry']['coordinates'])
print(mags[:10])
print(titles[:10])
print(coordinates[:10])
title = all_days['metadata']['title']
print(title)
