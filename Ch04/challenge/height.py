# Draw the running track from track.csv
#
# - Sample data to a minute interval
# - Markers should be blue if the height is below 100 meter, otherwise red

#%%
import pandas as pd
df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
df = df.resample('min').mean()
df.head()
# %%
import folium

m = folium.Map(
    location=[df['lat'].mean(), df['lng'].mean()],
    zoom_start=15,
)
m
# %%
m = folium.Map(
    location=[df['lat'].mean(), df['lng'].mean()],
    zoom_start=15,
)
m
def b_height(row):
    loc = tuple(row[['lat', 'lng']])
    marker = folium.CircleMarker(
        loc,
        radius=5,
        color='blue' if row['height']<100 else 'red',
        popup=row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

df.apply(b_height,axis = 1)
m
# %%
