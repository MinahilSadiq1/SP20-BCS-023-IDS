import folium
import pandas as pd

pakistan_map = folium.Map(location=[30.37,69.34],zoom_start=4.5,tiles='OpenStreetMap')

#load the dataset (csv file) into the Pandas dataframe
df = pd.read_csv('')
df

#calculate total number of cases using a loop
t = 0
for c in df['Total Cases']:
  t = int(c)+int(t)

# mark circles on the map and display the map
for state, lat, long, tc, de, re, ac in zip(list(df['State']), list(df['Latitude']), list(df['Longitude']),
                                            list(df['Total Cases']), list(df['Deaths']), list(df['Recoveries']),
                                            list(df['Active Cases'])):
    folium.CircleMarker(location=[long,lat],
                        radius=(tc / t) * 100,
                        color='red',
                        fill=False,
                        fill_color='blue').add_to(pakistan_map)
    xyz = '<strong>State:  ' + state + '</strong><br>' + 'Total Cases: ' + str(tc) + '<br>' + 'Deaths: ' + str(
        de) + '<br>' + 'Recoveries: ' + str(re) + '<br>' + 'Active Cases: ' + str(ac)
    iframe = folium.IFrame(xyz, width=200, height=150)
    popupData = folium.Popup(iframe, max_width=500)
    folium.Marker(location=[lat, long], popup=popupData).add_to(pakistan_map)