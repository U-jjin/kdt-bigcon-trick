import json
import pandas as pd

from plotly.offline import plot
import plotly.express as px

from config.settings import DATA_DIRS


map1 = pd.read_csv(DATA_DIRS[0]+'/0816_瘤开喊_夸老喊.csv', encoding ='cp949')
geo_path2 = DATA_DIRS[0]+'/LSMD_ADM_SECT_UMD_力林.zip.geojson'
geo_data2 = json.load(open(geo_path2, encoding='utf-8'))

def fig1():
    return plot(px.choropleth_mapbox(map1, geojson=geo_data2,
                                 locations='emd_nm',
                                 color='em_kg',
                                 color_continuous_scale="matter",
                                 range_color=(0, 50000),
                                 mapbox_style="carto-positron",
                                 featureidkey="properties.EMD_NM",
                                 zoom=9, center={"lat": 33.39075486566194, "lon": 126.53390204213252},
                                 opacity=0.5,
                                 labels={'emd_nm': 'em_kg'},
                                 animation_frame='week'), output_type='div')

def fig2():
    return plot(px.choropleth_mapbox(map1, geojson=geo_data2,
                                 locations='emd_nm',
                                 color='pay_amt',
                                 color_continuous_scale="matter",
                                 range_color=(10000, 1200000),
                                 mapbox_style="carto-positron",
                                 featureidkey="properties.EMD_NM",
                                 zoom=9, center={"lat": 33.39075486566194, "lon": 126.53390204213252},
                                 opacity=0.5,
                                 labels={'emd_nm': 'pay_amt'},
                                 animation_frame='week'), output_type='div')