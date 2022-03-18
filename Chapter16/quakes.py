import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

"""filename='data/2.5_week.json'
with open(filename) as f:
    allData = json.load(f)

readable_file='data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(allData, f, indent=4)"""

filename='data/readable_eq_data.json'
with open(filename) as f:
    allEqData = json.load(f)

allEqDicts = allEqData['features']

mags, lons, lats, hover_texts = [],[],[],[]
for eqDict in allEqDicts:
    mag = eqDict['properties']['mag']
    lon = eqDict['geometry']['coordinates'][0]
    lat = eqDict['geometry']['coordinates'][1]
    title=eqDict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
# print(mags[:10])
#print(lons[:5])
#print(lats[:5])

data = [{
    'type':'scattergeo',
    'lon':lons, 
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes This Week > Magnitude 2.5')

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='quakes.html')