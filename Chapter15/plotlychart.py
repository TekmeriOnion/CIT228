import matplotlib.pyplot as plt
from numpy.random import random
import plotly.graph_objects as go
from plotly import offline 

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
tempsJune = [99,86,87,88,111,86,103,87,94,78,77,85,88,82,85,85,88,89,89,90,89,78,80,81,82,83,82,83,84,85]
tempsJuly = [100,105,84,105,90,99,90,95,94,100,79,112,99,100,101,100,99,97,96,98,97,92,89,88,88,86,87,85,86,88]
tempsJan = [10,8,15,11,23,33,23,44,30,32,34,35,34,35,22,32,34,35,34,35,32,34,35,34,35,32,34,35,34,35,]
tempsFeb=[19,21,18,22,23,25,29,30,33,35,55,56,60,55,58,55,56,52,51,50,50,49,48,48,45,44,42,41,40,41]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=days,
    y=tempsJan,
    name='Jan Temps',
    marker_color='blue'
))
fig.add_trace(go.Scatter(
    x=days,
    y=tempsFeb,
    name='Feb Temps',
    marker_color='purple'
))
fig.add_trace(go.Scatter(
    x=days,
    y=tempsJune,
    name='June Temps',
    marker_color='orange'
))
fig.add_trace(go.Scatter(
    x=days,
    y=tempsJuly,
    name='July Temps',
    marker_color='red'
))
fig.update_traces(mode='markers')
layout = fig.update_layout(
    title="Temps by Day of Month",
    title_font_color='green',
    title_font_size=24,
    xaxis_tickfont_size=12,
    xaxis=dict(title='Day of Month',titlefont_size=14, tickfont_size=12),
    yaxis=dict(title='Temp (Degrees F)',titlefont_size=14, tickfont_size=12),
    legend=dict(x=1, y=1.0)
)
#fig.show()
offline.plot({'data':fig, 'layout':layout},filename="plotly.html")