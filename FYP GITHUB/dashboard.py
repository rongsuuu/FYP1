import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from dash.dependencies import Input, Output
from engine import session
from model import ENR2_1table, ENR3_3_Signpointtable, ENR3_6table,\
                  ENR4_1table, ENR4_4table, ENR4_5table,ENR5_1table,\
                  ENR5_2table,ENR3_1_Signpointtable,ENR3_ATS_ROUTES_table
import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate

df2_1 = pd.read_sql(session.query(ENR2_1table).statement,session.bind)
df3_1 = pd.read_sql(session.query(ENR3_1_Signpointtable).statement,session.bind)
df3_3 = pd.read_sql(session.query(ENR3_3_Signpointtable).statement,session.bind)
df3 = pd.read_sql(session.query(ENR3_ATS_ROUTES_table).statement,session.bind)

df3_6 = pd.read_sql(session.query(ENR3_6table).statement,session.bind)
df3_6['id'] = df3_6['Id']
df3_6.set_index('id', inplace=True, drop=False)

df4_1 = pd.read_sql(session.query(ENR4_1table).statement,session.bind)
df4_1['id'] = df4_1['Name_of_station']
df4_1.set_index('id', inplace=True, drop=False)

df4_4 = pd.read_sql(session.query(ENR4_4table).statement,session.bind)
df4_4['id'] = df4_4['Name_Code_designator']
df4_4.set_index('id', inplace=True, drop=False)

df4_5 = pd.read_sql(session.query(ENR4_5table).statement,session.bind)
df4_5['id'] = df4_5['Name_Ident_coordinates']
df4_5.set_index('id', inplace=True, drop=False)

df5_1 = pd.read_sql(session.query(ENR5_1table).statement,session.bind)
df5_2 = pd.read_sql(session.query(ENR5_2table).statement,session.bind)

#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 SINGAPORE FIR#
fig1_1 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103,108,114,116.5,108.5,108.5,108.9,108.9,108.89,108.84,108.87,108.86,108.91,108.91,108.91,108.9,108.93,
          108.93,108.91,108.93,108.97,109.01,109,109,108,106,105.16,105.16,104.83,104.71,104.58,104.44,104.31,104.16,
          104.02,103.88,103.73,103.59,103.44,103.31,103.17,103.04,102.92,102.81,102.7,102.6,102.51,102.43,102.37,
          102.31,102.27,102.24,102.22,102.16,103.5,103.6,103.68,103.83,103.93,104.02,104.04,104.06,104.08,104.09,104.08,
          104.07,104.09,104.33,104.75,103.66,103.73,102.66], lat = [7,7,10.5,8.416,2.25,1,1,1.01,0.869,0.814,0.766,0.703,
          0.653,0.588,0.518,0.483,0.44,0.39,0.332,0.307,0.307,0.292,0.25,0,0,-0.83,0,0,-0.03,-0.11,-0.18,-0.23,-0.28,
          -0.31,-0.33,-0.33,-0.33,-0.31,-0.28,-0.23,-0.18,-0.11,-0.03,0.052,0.15,0.258,0.374,0.497,
          0.627,0.762,0.901,1.044,1.188,1.65,1.216,1.283,1.433,1.473,1.423,1.436,
          1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,2.6,3.666,4.833,6.75],
    marker = { 'size': 1, 'color': "orange" }))

fig1_1.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 108, 'lat': 7 },
        'zoom': 4},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 SINGAPORE FIR for query sector area#
fig1_1SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    mode="markers+lines",
    lon = [103,108,114,116.5,108.5,108.5,108.9,108.9,108.89,108.84,108.87,108.86,108.91,108.91,108.91,108.9,108.93,
          108.93,108.91,108.93,108.97,109.01,109,109,108,106,105.16,105.16,104.83,104.71,104.58,104.44,104.31,104.16,
          104.02,103.88,103.73,103.59,103.44,103.31,103.17,103.04,102.92,102.81,102.7,102.6,102.51,102.43,102.37,
          102.31,102.27,102.24,102.22,102.16,103.5,103.6,103.68,103.83,103.93,104.02,104.04,104.06,104.08,104.09,104.08,
          104.07,104.09,104.33,104.75,103.66,103.73,102.66], lat = [7,7,10.5,8.416,2.25,1,1,1.01,0.869,0.814,0.766,0.703,0.653,0.588,0.518,0.483,0.44,0.39,0.332,0.307
           ,0.307,0.292,0.25,0,0,-0.83,0,0,-0.03,-0.11,-0.18,-0.23,-0.28,-0.31,-0.33,-0.33,-0.33,-0.31,-0.28,-0.23
           ,-0.18,-0.11,-0.03,0.052,0.15,0.258,0.374,0.497,0.627,0.762,0.901,1.044,1.188,1.65,1.216,1.283
           ,1.433,1.473,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,2.6,3.666,4.833,6.75],
    name = 'SINGAPORE FIR',
    marker = { 'size': 1, 'color': "orange" },))

fig1_1SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 108, 'lat': 7 },
        'zoom': 4},
    height=650,width=850,
    showlegend =   True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})


fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.135,104.701,104.867],
    lat = [1.222,0.805,-0.04,-0.283],
    name = 'B470',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.111,104.468,105.998,108.927],
    lat = [2.916,2.875,2.669,2.578],
    name = 'G334',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.712,103.743,103.79,103.856,103.96,104.05,104.155,104.217],
    lat = [1.664,1.5,1.439,1.348,1.222,0.728,0.273,-0.268,-0.567,],
    name = 'G579',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.405,105.788,106.759,107.991,108.5],
    lat = [1.222,1.33,1.363,1.385,1.414,1.428],
    name = 'G580',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,103.223],
    lat = [6.937,5.753],
    name = 'R208',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.269,103.165,103.498,103.882],
    lat = [0.7,0.997,1.042,1.092],
    name = 'R469',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.405,103.99,103.828,103.712,103.414,103.336],
    lat = [1.33,1.522,1.509,1.5,1.458,1.447],
    name = 'W401',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,103.882],
    lat = [1.415,1.092],
    name = 'W407',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.931,109],
    lat = [0.418,0],
    name = 'L504',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [109.582,111.109],
    lat = [4.256,4.287],
    name = 'L517',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,106.926,106.407,105.788],
    lat = [8.215,3.561,2.559,1.363],
    name = 'L625',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,104.799,104.095,103.728,103.423],
    lat = [4.811,4.387,3.873,3.606,3.383],
    name = 'L629',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.213,105.263,104.761,104.131,103.823,103.423],
    lat = [4.288,3.98,3.817,3.613,3.513,3.383],
    name = 'L635',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,106.213,106.355,106.388,106.47,106.545,106.64,106.6963,106.759,107.09],
    lat = [7,4.288,3.532,3.354,2.92,2.521,2.016,1.7155,1.385,-0.379],
    name = 'L644',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,114.833,114.848],
    lat = [9.827,8.192,7.148],
    name = 'L649',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.165,102.138],
    lat = [0.997,1.397],
    name = 'L762',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.195],
    lat = [8.642,8.183],
    name = 'M522',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.984,103.498,104.514],
    lat = [1.385,1.042,0.904],
    name = 'M630',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,104.514,105.354,106.522],
    lat = [1.415,0.904,0.407,-0.616],
    name = 'M635',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.927,107.846,107.44,106.696,105.788],
    lat = [2.578,2.161,2.003,1.716,1.363],
    name = 'M646',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.245],
    lat = [7,4.873],
    name = 'M753',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.015],
    lat = [8.642,8.045],
    name = 'M754',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.929,104.113,104.526,105.21,105.805,106.926,109.582,111.855],
    lat = [3.383,3.409,3.418,3.439,3.474,3.504,3.561,4.256,4.836],
    name = 'M758',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,104.162,104.335,104.673,105.191,107.099,107.846,108.5],
    lat = [3.383,3.178,3.131,3.038,2.895,2.368,2.161,1.978],
    name = 'M761',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,102.817],
    lat = [6.937,6.48],
    name = 'M765',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [115.862,112.593,109.582,107.099,105.788],
    lat = [8.949,6.527,4.256,2.368,1.363],
    name = 'M767',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,111.545,112.593,113.346],
    lat = [8.215,7.276,6.527,5.985,],
    name = 'M768',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,113.929,113.346],
    lat = [9.827,7.517,5.985],
    name = 'M772',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.514,106.931,107.728],
    lat = [0.904,0.418,-0.113],
    name = 'M774',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.833,103.025,103.344,104.245],
    lat = [6.875,6.604,6.151,4.873],
    name = 'M904',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.498,104.217],
    lat = [1.042,-0.567],
    name = 'N502',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.245,104.799,105.004,105.263,105.537,105.805,106.101,107.099,107.44,107.991,108.813],
    lat = [4.873,4.387,4.207,3.98,3.739,3.504,3.244,2.368,2.003,1.414,0.528],
    name = 'N875',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,111.545,106.926,106.101,105.191,104.659,103.872],
    lat = [9.827,7.276,3.561,3.244,2.895,2.69,2.388],
    name = 'N884',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.153,106.213,105.537,105.21,104.673,104.468,104.105,103.872],
    lat = [7.089,4.288,3.739,3.474,3.038,2.875,2.577,2.388],
    name = 'N892',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.475],
    lat = [7,4.869],
    name = 'Q801',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.475,104.558],
    lat = [7,4.869,4.211],
    name = 'Q802',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.344,103.989,104.162,104.558],
    lat = [6.151,4.853,4.658,4.211],
    name = 'Q803',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,103.989,103.929],
    lat = [7,4.853,3.409],
    name = 'T611',
    marker = {'size': 5}))

fig1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,103.929],
    lat = [4.811,3.409],
    name = 'T612',
    marker = {'size': 5}))
#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 1B#
fig1_2 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.27,103.28,103.29,103.3,103.32,103.34,103.37,103.4,103.42,103.57,103.68,103.6,103.5],
    lat = [1.287,1.324,1.374,1.423,1.47,1.515,1.558,1.599,1.613,1.506,1.433,1.283,1.216],
    marker = { 'size': 1, 'color': "green" }))

fig1_2.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47 },
        'zoom': 8},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#-----------------------------------------------------------------------------------------------------------------------------

fig1_2SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.27,103.28,103.29,103.3,103.32,103.34,103.37,103.4,103.42,103.57,103.68,103.6,103.5],
    lat = [1.287,1.324,1.374,1.423,1.47,1.515,1.558,1.599,1.613,1.506,1.433,1.283,1.216],
    name = 'SECTION 1B',
    marker = { 'size': 1, 'color': "green" }))

fig1_2SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47 },
        'zoom': 8},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.405,103.99,103.828,103.712,103.414,103.336],
    lat = [1.33,1.522,1.509,1.5,1.458,1.447],
    name = 'W401',
    marker = {'size': 5}))

fig1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))


#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 1D#
fig1_3 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.42,103.4,103.37,103.34,103.32,103.3,103.29,
           103.28,103.27,103.11,103.11,103.13,103.15,103.17,103.2,103.24,103.28,103.28],
    lat = [1.613,1.599,1.558,1.515,1.47,1.423,1.374,1.324,
           1.287,1.34,1.353,1.417,1.48,1.541,1.599,1.654,1.707,1.708],
    marker = { 'size': 1, 'color': "blue" }))

fig1_3.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47},
        'zoom': 8},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig1_3SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.42,103.4,103.37,103.34,103.32,103.3,103.29,103.28,103.27,103.11,103.11,103.13,103.15,103.17,103.2,103.24,103.28,103.28],
    lat = [1.613,1.599,1.558,1.515,1.47,1.423,1.374,1.324,1.287,1.34,1.353,1.417,1.48,1.541,1.599,1.654,1.707,1.708],
    name='SECTION 1D',
    marker = { 'size': 1, 'color': "blue" }))

fig1_3SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47},
        'zoom': 8},
    height=650, width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_3SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig1_3SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig1_3SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))

#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 1F#
fig1_4 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.03,103.07,103.13,103.21,103.28,103.28,103.24,103.2,103.17,103.15,103.13,103.11,103.11],
    lat = [1.367,1.508,1.641,1.758,1.708,1.707,1.654,1.599,1.541,1.48,1.417,1.353,1.34],
    marker = { 'size': 1, 'color': "pink" }))

fig1_4.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47},
        'zoom': 8},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig1_4SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.03,103.07,103.13,103.21,103.28,103.28,103.24,103.2,103.17,103.15,103.13,103.11,103.11],
    lat = [1.367,1.508,1.641,1.758,1.708,1.707,1.654,1.599,1.541,1.48,1.417,1.353,1.34],
    name = 'SECTION 1F',
    marker = { 'size': 1, 'color': "pink" }))

fig1_4SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.32, 'lat': 1.47},
        'zoom': 8},
    height=650, width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_4SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig1_4SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig1_4SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))

#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 2A#
fig1_5 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.84,103.93,104.02,104.04,104.06,104.08,104.09,104.08,104.07,104.09,104.33,104.4,104.4,
           104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81],
    lat = [1.535,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,1.565,1.595,
           1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91
],
    marker = { 'size': 1, 'color': "purple" }))

fig1_5.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig1_5SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.84,103.93,104.02,104.04,104.06,104.08,104.09,104.08,104.07,104.09,104.33,104.4,104.4,
           104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81],
    lat = [1.535,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,1.565,1.595,
           1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91
],
    name='SECTION 2A',
    marker = { 'size': 1, 'color': "purple" }))

fig1_5SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_5SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.872,103.97,104.022,104.313,104.735,104.867],
    lat = [2.388,1.758,1.415,0.817,-0.023,-0.283],
    name = 'B338',
    marker = {'size': 5}))

fig1_5SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.526,103.643,103.719,103.872,103.901,103.912,103.923,103.933,103.856,104.045,104.407,104.576],
    lat = [3.383,3.155,2.895,2.727,2.388,1.922,1.756,1.59,1.423,1.222,0.755,-0.208,-0.483,],
    name = 'B469',
    marker = {'size': 5}))

fig1_5SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.041,104.033,104.022],
    lat = [2.614,1.915,1.415],
    name = 'G219',
    marker = {'size': 5}))

fig1_5SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_5SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.99],
    lat = [1.664,1.522],
    name = 'W651',
    marker = {'size': 5}))

fig1_5SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.912,103.406],
    lat = [1.756,2.146],
    name = 'Y339',
    marker = {'size': 5}))
#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 2C#
fig1_6 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.79,103.76,103.93,104.1,104.28,104.44,104.58,104.61,104.4,104.4,104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81],
    lat = [2.367,2.429,2.445,2.429,2.383,2.308,2.205,2.178,1.565,1.595,1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91],
    marker = { 'size': 1, 'color': "lavender" }))

fig1_6.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#-----------------------------------------------------------------------------------------------------------------------------

fig1_6SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.79,103.76,103.93,104.1,104.28,104.44,104.58,104.61,104.4,104.4,104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81],
    lat = [2.367,2.429,2.445,2.429,2.383,2.308,2.205,2.178,1.565,1.595,1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91],
    name='SECTION 2C',
    marker = { 'size': 1, 'color': "lavender" }))

fig1_6SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.872],
    lat = [1.664,2.388],
    name = 'A224',
    marker = {'size': 5},))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.872,103.97,104.022,104.313,104.735,104.867],
    lat = [2.388,1.758,1.415,0.817,-0.023,-0.283],
    name = 'B338',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.526,103.643,103.719,103.872,103.901,103.912,103.923,103.933,103.856,104.045,104.407,104.576],
    lat = [3.383,3.155,2.895,2.727,2.388,1.922,1.756,1.59,1.423,1.222,0.755,-0.208,-0.483,],
    name = 'B469',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,111.545,106.926,106.101,105.191,104.659,103.872],
    lat = [9.827,7.276,3.561,3.244,2.895,2.69,2.388],
    name = 'N884',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.153,106.213,105.537,105.21,104.673,104.468,104.105,103.872],
    lat = [7.089,4.288,3.739,3.474,3.038,2.875,2.577,2.388],
    name = 'N892',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig1_6SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.041,104.033,104.022],
    lat = [2.614,1.915,1.415],
    name = 'G219',
    marker = {'size': 5}))
#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 2E#
fig1_7 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.56,103.72,103.93,104.19,104.44,104.56,104.75,104.61,104.58,104.44,104.28,104.1,103.93,103.76],
    lat = [2.876,2.908,2.93,2.907,2.839,2.784,2.593,2.178,2.205,2.308,2.383,2.429,2.445,2.429],
    marker = { 'size': 1, 'color': "light blue" }))

fig1_7.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#-----------------------------------------------------------------------------------------------------------------------------

fig1_7SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.56,103.72,103.93,104.19,104.44,104.56,104.75,104.61,104.58,104.44,104.28,104.1,103.93,103.76],
    lat = [2.876,2.908,2.93,2.907,2.839,2.784,2.593,2.178,2.205,2.308,2.383,2.429,2.445,2.429],
    name='SECTION 2E',
    marker = { 'size': 1, 'color': "light blue" }))

fig1_7SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 7},
    height=650, width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.526,103.643,103.719,103.872,103.901,103.912,103.923,103.933,103.856,104.045,104.407,104.576],
    lat = [3.383,3.155,2.895,2.727,2.388,1.922,1.756,1.59,1.423,1.222,0.755,-0.208,-0.483,],
    name = 'B469',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,111.545,106.926,106.101,105.191,104.659,103.872],
    lat = [9.827,7.276,3.561,3.244,2.895,2.69,2.388],
    name = 'N884',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.153,106.213,105.537,105.21,104.673,104.468,104.105,103.872],
    lat = [7.089,4.288,3.739,3.474,3.038,2.875,2.577,2.388],
    name = 'N892',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig1_7SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.041,104.033,104.022],
    lat = [2.614,1.915,1.415],
    name = 'G219',
    marker = {'size': 5}))
#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Section 2H#
fig1_8 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.72,103.93,104.19,104.44,104.56,103.69],
    lat = [2.908,2.93,2.907,2.839,2.784,3.639],
    marker = { 'size': 1, 'color': "palegreen" }),

)

fig1_8.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 6},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#-----------------------------------------------------------------------------------------------------------------------------

fig1_8SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.72,103.93,104.19,104.44,104.56,103.69],
    lat = [2.908,2.93,2.907,2.839,2.784,3.639],
    name='SECTION 2F',
    marker = { 'size': 1, 'color': "palegreen" }),

)

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,104.799,104.095,103.728,103.423],
    lat = [4.811,4.387,3.873,3.606,3.383],
    name = 'L629',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.213,105.263,104.761,104.131,103.823,103.423],
    lat = [4.288,3.98,3.817,3.613,3.513,3.383],
    name = 'L635',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig1_8SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 104.25, 'lat': 1.808 },
        'zoom': 6},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.929,104.113,104.526,105.21,105.805,106.926,109.582,111.855],
    lat = [3.383,3.409,3.418,3.439,3.474,3.504,3.561,4.256,4.836],
    name = 'M758',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,104.162,104.335,104.673,105.191,107.099,107.846,108.5],
    lat = [3.383,3.178,3.131,3.038,2.895,2.368,2.161,1.978],
    name = 'M761',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.111,104.468,105.998,108.927],
    lat = [2.916,2.875,2.669,2.578],
    name = 'G334',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.728,103.526],
    lat = [3.606,3.155],
    name = 'Y333',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.823,103.526],
    lat = [3.513,3.155],
    name = 'Y334',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.929,103.526],
    lat = [3.409,3.155],
    name = 'Y335',
    marker = {'size': 5}))

fig1_8SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.162,103.526],
    lat = [3.178,3.155],
    name = 'Y336',
    marker = {'size': 5}))
#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR2.1 Combine#
fig1_9 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103,108,114,116.5,108.5,108.5,108.9,108.9,108.89,108.84,108.87,108.86,108.91,108.91,108.91,108.9,108.93,
          108.93,108.91,108.93,108.97,109.01,109,109,108,106,105.16,105.16,104.83,104.71,104.58,104.44,104.31,104.16,
          104.02,103.88,103.73,103.59,103.44,103.31,103.17,103.04,102.92,102.81,102.7,102.6,102.51,102.43,102.37,
          102.31,102.27,102.24,102.22,102.16,103.5,103.6,103.68,103.83,103.93,104.02,104.04,104.06,104.08,104.09,104.08,
          104.07,104.09,104.33,104.75,103.66,103.73,102.66,
           None,103.27,103.28,103.29,103.3,103.32,103.34,103.37,103.4,103.42,103.57,103.68,103.6,103.5,
           None,103.42,103.4,103.37,103.34,103.32,103.3,103.29,103.28,103.27,103.11,103.11,103.13,103.15,103.17,103.2,103.24,103.28,103.28,
           None,103.03,103.07,103.13,103.21,103.28,103.28,103.24,103.2,103.17,103.15,103.13,103.11,103.11,
           None,103.84,103.93,104.02,104.04,104.06,104.08,104.09,104.08,104.07,104.09,104.33,104.4,104.4,
           104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81,
           None,103.79,103.76,103.93,104.1,104.28,104.44,104.58,104.61,104.4,104.4,104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81,
           None,103.56,103.72,103.93,104.19,104.44,104.56,104.75,104.61,104.58,104.44,104.28,104.1,103.93,103.76,
           None,103.72,103.93,104.19,104.44,104.56,103.69],
     lat = [7,7,10.5,8.416,2.25,1,1,1.01,0.869,0.814,0.766,0.703,0.653,0.588,0.518,0.483,0.44,0.39,0.332,0.307
           ,0.307,0.292,0.25,0,0,-0.83,0,0,-0.03,-0.11,-0.18,-0.23,-0.28,-0.31,-0.33,-0.33,-0.33,-0.31,-0.28,-0.23
           ,-0.18,-0.11,-0.03,0.052,0.15,0.258,0.374,0.497,0.627,0.762,0.901,1.044,1.188,1.65,1.216,1.283
           ,1.433,1.473,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,2.6,3.666,4.833,6.75,
            None,1.287,1.324,1.374,1.423,1.47,1.515,1.558,1.599,1.613,1.506,1.433,1.283,1.216,
            None,1.613,1.599,1.558,1.515,1.47,1.423,1.374,1.324,1.287,1.34,1.353,1.417,1.48,1.541,1.599,1.654,1.707,1.708,
            None,1.367,1.508,1.641,1.758,1.708,1.707,1.654,1.599,1.541,1.48,1.417,1.353,1.34,
            None,1.535,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,1.565,1.595,
            1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91,
            None,2.367,2.429,2.445,2.429,2.383,2.308,2.205,2.178,1.565,1.595,1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91,
            None,2.876,2.908,2.93,2.907,2.839,2.784,2.593,2.178,2.205,2.308,2.383,2.429,2.445,2.429,
            None,2.908,2.93,2.907,2.839,2.784,3.639],
      marker = { 'size': 1, 'color': "springgreen" }))

fig1_9.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 108, 'lat': 7}, 'zoom': 4},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#-----------------------------------------------------------------------------------------------------------------------------

fig1_9SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103,108,114,116.5,108.5,108.5,108.9,108.9,108.89,108.84,108.87,108.86,108.91,108.91,108.91,108.9,108.93,
          108.93,108.91,108.93,108.97,109.01,109,109,108,106,105.16,105.16,104.83,104.71,104.58,104.44,104.31,104.16,
          104.02,103.88,103.73,103.59,103.44,103.31,103.17,103.04,102.92,102.81,102.7,102.6,102.51,102.43,102.37,
          102.31,102.27,102.24,102.22,102.16,103.5,103.6,103.68,103.83,103.93,104.02,104.04,104.06,104.08,104.09,104.08,
          104.07,104.09,104.33,104.75,103.66,103.73,102.66,
           None,103.27,103.28,103.29,103.3,103.32,103.34,103.37,103.4,103.42,103.57,103.68,103.6,103.5,
           None,103.42,103.4,103.37,103.34,103.32,103.3,103.29,103.28,103.27,103.11,103.11,103.13,103.15,103.17,103.2,103.24,103.28,103.28,
           None,103.03,103.07,103.13,103.21,103.28,103.28,103.24,103.2,103.17,103.15,103.13,103.11,103.11,
           None,103.84,103.93,104.02,104.04,104.06,104.08,104.09,104.08,104.07,104.09,104.33,104.4,104.4,
           104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81,
           None,103.79,103.76,103.93,104.1,104.28,104.44,104.58,104.61,104.4,104.4,104.36,104.31,104.25,104.18,104.1,104.01,103.93,103.84,103.81,
           None,103.56,103.72,103.93,104.19,104.44,104.56,104.75,104.61,104.58,104.44,104.28,104.1,103.93,103.76,
           None,103.72,103.93,104.19,104.44,104.56,103.69],
     lat = [7,7,10.5,8.416,2.25,1,1,1.01,0.869,0.814,0.766,0.703,0.653,0.588,0.518,0.483,0.44,0.39,0.332,0.307
           ,0.307,0.292,0.25,0,0,-0.83,0,0,-0.03,-0.11,-0.18,-0.23,-0.28,-0.31,-0.33,-0.33,-0.33,-0.31,-0.28,-0.23
           ,-0.18,-0.11,-0.03,0.052,0.15,0.258,0.374,0.497,0.627,0.762,0.901,1.044,1.188,1.65,1.216,1.283
           ,1.433,1.473,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,2.6,3.666,4.833,6.75,
            None,1.287,1.324,1.374,1.423,1.47,1.515,1.558,1.599,1.613,1.506,1.433,1.283,1.216,
            None,1.613,1.599,1.558,1.515,1.47,1.423,1.374,1.324,1.287,1.34,1.353,1.417,1.48,1.541,1.599,1.654,1.707,1.708,
            None,1.367,1.508,1.641,1.758,1.708,1.707,1.654,1.599,1.541,1.48,1.417,1.353,1.34,
            None,1.535,1.423,1.436,1.441,1.435,1.421,1.401,1.375,1.358,1.332,1.333,1.565,1.595,
            1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91,
            None,2.367,2.429,2.445,2.429,2.383,2.308,2.205,2.178,1.565,1.595,1.674,1.746,1.808,1.858,1.895,1.918,1.925,1.918,1.91,
            None,2.876,2.908,2.93,2.907,2.839,2.784,2.593,2.178,2.205,2.308,2.383,2.429,2.445,2.429,
            None,2.908,2.93,2.907,2.839,2.784,3.639],
       name='COMBINE',
      marker = { 'size': 1, 'color': "Yellow" }))

fig1_9SA.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 108, 'lat': 7}, 'zoom': 4},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_9SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 108, 'lat': 7 },
        'zoom': 4},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.872],
    lat = [1.664,2.388],
    name = 'A224',
    marker = {'size': 5},))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.872,103.97,104.022,104.313,104.735,104.867],
    lat = [2.388,1.758,1.415,0.817,-0.023,-0.283],
    name = 'B338',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.526,103.643,103.719,103.872,103.901,103.912,103.923,103.933,103.856,104.045,104.407,104.576],
    lat = [3.383,3.155,2.895,2.727,2.388,1.922,1.756,1.59,1.423,1.222,0.755,-0.208,-0.483,],
    name = 'B469',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.135,104.701,104.867],
    lat = [1.222,0.805,-0.04,-0.283],
    name = 'B470',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.041,104.033,104.022],
    lat = [2.614,1.915,1.415],
    name = 'G219',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.111,104.468,105.998,108.927],
    lat = [2.916,2.875,2.669,2.578],
    name = 'G334',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.712,103.743,103.79,103.856,103.96,104.05,104.155,104.217],
    lat = [1.664,1.5,1.439,1.348,1.222,0.728,0.273,-0.268,-0.567,],
    name = 'G579',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.405,105.788,106.759,107.991,108.5],
    lat = [1.222,1.33,1.363,1.385,1.414,1.428],
    name = 'G580',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,103.223],
    lat = [6.937,5.753],
    name = 'R208',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.269,103.165,103.498,103.882],
    lat = [0.7,0.997,1.042,1.092],
    name = 'R469',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.405,103.99,103.828,103.712,103.414,103.336],
    lat = [1.33,1.522,1.509,1.5,1.458,1.447],
    name = 'W401',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,103.882],
    lat = [1.415,1.092],
    name = 'W407',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.892,103.661],
    lat = [1.737,1.664],
    name = 'W534',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.99],
    lat = [1.664,1.522],
    name = 'W651',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.931,109],
    lat = [0.418,0],
    name = 'L504',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [109.582,111.109],
    lat = [4.256,4.287],
    name = 'L517',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,106.926,106.407,105.788],
    lat = [8.215,3.561,2.559,1.363],
    name = 'L625',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,104.799,104.095,103.728,103.423],
    lat = [4.811,4.387,3.873,3.606,3.383],
    name = 'L629',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.213,105.263,104.761,104.131,103.823,103.423],
    lat = [4.288,3.98,3.817,3.613,3.513,3.383],
    name = 'L635',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,106.213,106.355,106.388,106.47,106.545,106.64,106.6963,106.759,107.09],
    lat = [7,4.288,3.532,3.354,2.92,2.521,2.016,1.7155,1.385,-0.379],
    name = 'L644',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,114.833,114.848],
    lat = [9.827,8.192,7.148],
    name = 'L649',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.165,102.138],
    lat = [0.997,1.397],
    name = 'L762',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.195],
    lat = [8.642,8.183],
    name = 'M522',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.984,103.498,104.514],
    lat = [1.385,1.042,0.904],
    name = 'M630',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,104.514,105.354,106.522],
    lat = [1.415,0.904,0.407,-0.616],
    name = 'M635',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.927,107.846,107.44,106.696,105.788],
    lat = [2.578,2.161,2.003,1.716,1.363],
    name = 'M646',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.245],
    lat = [7,4.873],
    name = 'M753',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.015],
    lat = [8.642,8.045],
    name = 'M754',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.929,104.113,104.526,105.21,105.805,106.926,109.582,111.855],
    lat = [3.383,3.409,3.418,3.439,3.474,3.504,3.561,4.256,4.836],
    name = 'M758',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,104.162,104.335,104.673,105.191,107.099,107.846,108.5],
    lat = [3.383,3.178,3.131,3.038,2.895,2.368,2.161,1.978],
    name = 'M761',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,102.817],
    lat = [6.937,6.48],
    name = 'M765',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [115.862,112.593,109.582,107.099,105.788],
    lat = [8.949,6.527,4.256,2.368,1.363],
    name = 'M767',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,111.545,112.593,113.346],
    lat = [8.215,7.276,6.527,5.985,],
    name = 'M768',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,113.929,113.346],
    lat = [9.827,7.517,5.985],
    name = 'M772',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.514,106.931,107.728],
    lat = [0.904,0.418,-0.113],
    name = 'M774',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.833,103.025,103.344,104.245],
    lat = [6.875,6.604,6.151,4.873],
    name = 'M904',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.498,104.217],
    lat = [1.042,-0.567],
    name = 'N502',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.245,104.799,105.004,105.263,105.537,105.805,106.101,107.099,107.44,107.991,108.813],
    lat = [4.873,4.387,4.207,3.98,3.739,3.504,3.244,2.368,2.003,1.414,0.528],
    name = 'N875',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,111.545,106.926,106.101,105.191,104.659,103.872],
    lat = [9.827,7.276,3.561,3.244,2.895,2.69,2.388],
    name = 'N884',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.153,106.213,105.537,105.21,104.673,104.468,104.105,103.872],
    lat = [7.089,4.288,3.739,3.474,3.038,2.875,2.577,2.388],
    name = 'N892',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.475],
    lat = [7,4.869],
    name = 'Q801',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.475,104.558],
    lat = [7,4.869,4.211],
    name = 'Q802',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.344,103.989,104.162,104.558],
    lat = [6.151,4.853,4.658,4.211],
    name = 'Q803',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,103.989,103.929],
    lat = [7,4.853,3.409],
    name = 'T611',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,103.929],
    lat = [4.811,3.409],
    name = 'T612',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.677,103.526],
    lat = [3.843,3.155],
    name = 'Y332',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.728,103.526],
    lat = [3.606,3.155],
    name = 'Y333',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.823,103.526],
    lat = [3.513,3.155],
    name = 'Y334',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.929,103.526],
    lat = [3.409,3.155],
    name = 'Y335',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.162,103.526],
    lat = [3.178,3.155],
    name = 'Y336',
    marker = {'size': 5}))

fig1_9SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.912,103.406],
    lat = [1.756,2.146],
    name = 'Y339',
    marker = {'size': 5}))


#-----------------------------------------------------------------------------------------------------------------------------
fig3_1 = px.line_mapbox(df3_1, lat="Latitude", lon="Longitude", color="Route_Designator", zoom=3, height=650,width=950)

fig3_1.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 1.385, mapbox_center_lon = 106.759,
    margin={"r":0,"t":0,"l":0,"b":0})
#-----------------------------------------------------------------------------------------------------------------------------
fig3_3 = px.line_mapbox(df3_3, lat="Latitude", lon="Longitude", color="Route_Designator", zoom=3, height=650,width=950)

fig3_3.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 1.385, mapbox_center_lon = 106.759,
    margin={"r":0,"t":0,"l":0,"b":0})
#-----------------------------------------------------------------------------------------------------------------------------
fig3 = px.line_mapbox(df3, lat="Latitude", lon="Longitude", color="Route_Designator", zoom=3, height=650,width=950)

fig3.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 1.385, mapbox_center_lon = 106.759,
    margin={"r":0,"t":0,"l":0,"b":0})

#-----------------------------------------------------------------------------------------------------------------------------
#Filled map coding for ENR5.1 #
fig5_1_RA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.048,102.582,102.998,103.765,103.348,103.265,103.215,103.048],
    lat = [3.483,2.666,2.383,2.383,3.35,3.316,3.433,3.483],
    marker = { 'size': 1, 'color': "pink" }))

fig5_1_RA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 102.765, 'lat': 3.15},
        'zoom': 8},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------
fig5_1_1SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.048,102.582,102.998,103.765,103.348,103.265,103.215,103.048],
    lat = [3.483,2.666,2.383,2.383,3.35,3.316,3.433,3.483],
    name = 'Restricted area',
    marker = { 'size': 1, 'color': "pink" }))

fig5_1_1SA.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 102.765, 'lat': 3.15},
        'zoom': 8},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig5_1_1SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.222,103.642],
    lat = [3.291,2.895],
    name = 'Y514',
    marker = {'size': 5}))

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD11 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.673,103.651,103.653,103.633,103.669,103.684,103.684,103.69],
     lat = [1.431,1.393,1.384,1.349,1.326,1.362,1.379,1.411],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD11.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD11A = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.673,103.651,103.653,103.671,103.684,103.69],
     lat = [1.431,1.393,1.384,1.378,1.379,1.411],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD11A.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD11B = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.653,103.671,103.684,103.684,103.669,103.633],
     lat = [1.384,1.378,1.379,1.362,1.326,1.349],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD11B.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD13 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.6,104.6,104.917,104.917],
     lat = [2,2.5,2.5,2],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD13.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------


fig5_1_WSD14 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.6,104.6,104.917,104.917],
     lat = [1.5,2,2,1.5],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD14.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD15 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.917,104.917,105.5,105.5],
     lat = [1.5,2,2,1.5],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD15.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WSD20 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.6,104.6,104.917,104.917],
     lat = [2.5,3.0,3.0,2.5],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD20.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------
fig5_1_WSD34 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.036,104.059,104.044,104.033],
     lat = [1.403,1.405,1.397,1.398,],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD34.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------
fig5_1_WSD44 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.917,104.917,105.208,105.208],
     lat = [2.0,2.5,2.5,2],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD44.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------
fig5_1_WSD45 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [105.208,105.208,105.5,105.5],
     lat = [2.0,2.5,2.5,2.0],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD45.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD8 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.333,104.333,104.583,104.583],
     lat = [1.5,2.0,2,1.5],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD8.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD12 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.283,104.283,104.6,104.6],
     lat = [2.0,2.5,2.5,2.0],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD12.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD21 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.6,104.6,104.283,104.283],
     lat = [2.5,3.0,3,2.5],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD21.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD224 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [102.998,102.998,103.165,103.165],
     lat = [1.417,1.5,1.45,1.367],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD224.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD227 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.223,104.223,104.283,104.283,104.223],
     lat = [2.317,2.0,2.0,2.317,2.317,],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD227.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD230 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.89,103.86,103.832,103.861],
     lat = [1.622,1.644,1.618,1.592],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD230.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_WMD231 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.831,103.841,103.825,103.806,103.774,103.774,103.811,],
     lat = [1.638,1.658,1.711,1.711,1.693,1.644,1.649],
      marker = { 'size': 1, 'color': "red" }))

fig5_1_WMD231.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#-----------------------------------------------------------------------------------------------------------------------------

fig5_1_2SA = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.673,103.651,103.653,103.633,103.669,103.684,103.684,103.69,
           None,103.673,103.651,103.653,103.671,103.684,103.69,
           None,103.653,103.671,103.684,103.684,103.669,103.633,
           None,104.6,104.917,
           None,104.6,104.917,
           None,104.917,105.5,
           None,104.6,104.917,
           None,104.036,104.059,104.044,104.033,
           None,104.917,105.208,
           None,105.208,105.5,
           None,104.333,104.583,
           None,104.283,104.6,
           None,104.6,104.283,
           None,102.998,102.998,103.165,103.165,
           None,104.223,104.223,104.283,104.283,104.223,
           None,103.89,103.86,103.832,103.861,
           None,103.831,103.841,103.825,103.806,103.774,103.774,103.811,
           ],
     lat = [1.431,1.393,1.384,1.349,1.326,1.362,1.379,1.411,
            None,1.431,1.393,1.384,1.378,1.379,1.411,
            None,1.384,1.378,1.379,1.362,1.326,1.349,
            None,2,2.5,
            None,1.5,2,
            None,1.5,2,
            None,2.5,3.0,
            None,1.403,1.405,1.397,1.398,
            None,2.0,2.5,
            None,2.0,2.5,
            None,1.5,2.0,
            None,2.0,2.5,
            None,2.5,3.0,
            None,1.417,1.5,1.45,1.367,
            None,2.317,2.0,2.0,2.317,2.317,
            None,1.622,1.644,1.618,1.592,
            None,1.638,1.658,1.711,1.711,1.693,1.644,1.649,
            ],
       name = 'Danger area',
      marker = { 'size': 1, 'color': "red" }))

fig5_1_2SA.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=950,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.872],
    lat = [1.664,2.388],
    name = 'A224',
    marker = {'size': 5},))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.287,102.881],
    lat = [1.664,1.848,2.047],
    name = 'A457',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.34,103.414,103.629,103.856,104.514],
    lat = [1.615,1.498,1.458,1.344,1.222,0.904],
    name = 'A464',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.089,103.336,103.619,103.856],
    lat = [1.552,1.447,1.324,1.222],
    name = 'A576',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.872,103.97,104.022,104.313,104.735,104.867],
    lat = [2.388,1.758,1.415,0.817,-0.023,-0.283],
    name = 'B338',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.211],
    lat = [1.664,2.018],
    name = 'B466',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.526,103.643,103.719,103.872,103.901,103.912,103.923,103.933,103.856,104.045,104.407,104.576],
    lat = [3.383,3.155,2.895,2.727,2.388,1.922,1.756,1.59,1.423,1.222,0.755,-0.208,-0.483,],
    name = 'B469',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.135,104.701,104.867],
    lat = [1.222,0.805,-0.04,-0.283],
    name = 'B470',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.041,104.033,104.022],
    lat = [2.614,1.915,1.415],
    name = 'G219',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.111,104.468,105.998,108.927],
    lat = [2.916,2.875,2.669,2.578],
    name = 'G334',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.712,103.743,103.79,103.856,103.96,104.05,104.155,104.217],
    lat = [1.664,1.5,1.439,1.348,1.222,0.728,0.273,-0.268,-0.567,],
    name = 'G579',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.856,104.405,105.788,106.759,107.991,108.5],
    lat = [1.222,1.33,1.363,1.385,1.414,1.428],
    name = 'G580',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,103.223],
    lat = [6.937,5.753],
    name = 'R208',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.083,103.661],
    lat = [2.332,1.664],
    name = 'R325',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.269,103.165,103.498,103.882],
    lat = [0.7,0.997,1.042,1.092],
    name = 'R469',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.405,103.99,103.828,103.712,103.414,103.336],
    lat = [1.33,1.522,1.509,1.5,1.458,1.447],
    name = 'W401',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,103.882],
    lat = [1.415,1.092],
    name = 'W407',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.892,103.661],
    lat = [1.737,1.664],
    name = 'W534',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.99],
    lat = [1.664,1.522],
    name = 'W651',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.931,109],
    lat = [0.418,0],
    name = 'L504',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [109.582,111.109],
    lat = [4.256,4.287],
    name = 'L517',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,106.926,106.407,105.788],
    lat = [8.215,3.561,2.559,1.363],
    name = 'L625',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,104.799,104.095,103.728,103.423],
    lat = [4.811,4.387,3.873,3.606,3.383],
    name = 'L629',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.213,105.263,104.761,104.131,103.823,103.423],
    lat = [4.288,3.98,3.817,3.613,3.513,3.383],
    name = 'L635',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.245,104.095,104.013,103.95,103.872],
    lat = [7,4.873,3.873,3.326,2.911,2.388],
    name = 'L642',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,106.213,106.355,106.388,106.47,106.545,106.64,106.6963,106.759,107.09],
    lat = [7,4.288,3.532,3.354,2.92,2.521,2.016,1.7155,1.385,-0.379],
    name = 'L644',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,114.833,114.848],
    lat = [9.827,8.192,7.148],
    name = 'L649',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.165,102.138],
    lat = [0.997,1.397],
    name = 'L762',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.195],
    lat = [8.642,8.183],
    name = 'M522',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.984,103.498,104.514],
    lat = [1.385,1.042,0.904],
    name = 'M630',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.022,104.514,105.354,106.522],
    lat = [1.415,0.904,0.407,-0.616],
    name = 'M635',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.927,107.846,107.44,106.696,105.788],
    lat = [2.578,2.161,2.003,1.716,1.363],
    name = 'M646',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.245],
    lat = [7,4.873],
    name = 'M753',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [116.23,116.015],
    lat = [8.642,8.045],
    name = 'M754',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,103.929,104.113,104.526,105.21,105.805,106.926,109.582,111.855],
    lat = [3.383,3.409,3.418,3.439,3.474,3.504,3.561,4.256,4.836],
    name = 'M758',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.423,104.162,104.335,104.673,105.191,107.099,107.846,108.5],
    lat = [3.383,3.178,3.131,3.038,2.895,2.368,2.161,1.978],
    name = 'M761',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.585,102.817],
    lat = [6.937,6.48],
    name = 'M765',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [115.862,112.593,109.582,107.099,105.788],
    lat = [8.949,6.527,4.256,2.368,1.363],
    name = 'M767',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [110.218,111.545,112.593,113.346],
    lat = [8.215,7.276,6.527,5.985,],
    name = 'M768',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [106.81,105.38,105.004,104.761,104.526,104.335,104.287,103.872],
    lat = [7,4.811,4.207,3.817,3.439,3.131,3.055,2.388],
    name = 'M771',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,113.929,113.346],
    lat = [9.827,7.517,5.985],
    name = 'M772',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.514,106.931,107.728],
    lat = [0.904,0.418,-0.113],
    name = 'M774',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [102.833,103.025,103.344,104.245],
    lat = [6.875,6.604,6.151,4.873],
    name = 'M904',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.498,104.217],
    lat = [1.042,-0.567],
    name = 'N502',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.245,104.799,105.004,105.263,105.537,105.805,106.101,107.099,107.44,107.991,108.813],
    lat = [4.873,4.387,4.207,3.98,3.739,3.504,3.244,2.368,2.003,1.414,0.528],
    name = 'N875',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [114.808,111.545,106.926,106.101,105.191,104.659,103.872],
    lat = [9.827,7.276,3.561,3.244,2.895,2.69,2.388],
    name = 'N884',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
   mode = "markers+lines",
    lon = [103.585,103.919,104.245,104.131,104.113,104.098,104.094,103.933],
    lat = [6.937,5.894,4.873,3.613,3.418,3.242,3.198,1.423],
    name = 'N891',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [108.153,106.213,105.537,105.21,104.673,104.468,104.105,103.872],
    lat = [7.089,4.288,3.739,3.474,3.038,2.875,2.577,2.388],
    name = 'N892',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.12,103.351,103.498,104.867],
    lat = [1.615,1.266,1.042,-0.283],
    name = 'P501',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.555,104.475],
    lat = [7,4.869],
    name = 'Q801',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,104.475,104.558],
    lat = [7,4.869,4.211],
    name = 'Q802',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.344,103.989,104.162,104.558],
    lat = [6.151,4.853,4.658,4.211],
    name = 'Q803',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.132,103.989,103.929],
    lat = [7,4.853,3.409],
    name = 'T611',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [105.38,103.929],
    lat = [4.811,3.409],
    name = 'T612',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.677,103.526],
    lat = [3.843,3.155],
    name = 'Y332',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.728,103.526],
    lat = [3.606,3.155],
    name = 'Y333',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.823,103.526],
    lat = [3.513,3.155],
    name = 'Y334',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.929,103.526],
    lat = [3.409,3.155],
    name = 'Y335',
    marker = {'size': 5}))
fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [104.162,103.526],
    lat = [3.178,3.155],
    name = 'Y336',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.912,103.406],
    lat = [1.756,2.146],
    name = 'Y339',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.661,103.406],
    lat = [1.664,2.146],
    name = 'Y342',
    marker = {'size': 5}))

fig5_1_2SA.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [103.222,103.642],
    lat = [3.291,2.895],
    name = 'Y514',
    marker = {'size': 5}))
#Filled map coding for ENR5.2 LIGHT AIRCRAFT TRAINING AREA A#-----------------------------------------------------------------

fig5_2_1 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.772,103.761,103.782,103.838,103.823,103.798,103.772], lat = [1.447,1.38,1.35,1.376,1.391,1.454,1.447],
    marker = { 'size': 1, 'color': "orange" }))

fig5_2_1.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 10},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#Filled map coding for ENR5.2 LIGHT AIRCRAFT TRAINING AREA A EAST#---------------------------------------------------------------

fig5_2_2 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.787,103.823,103.838,103.802,103.787], lat = [1.406,1.391,1.376,1.359,1.406],
    marker = { 'size': 1, 'color': "green" }))

fig5_2_2.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 10},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#Filled map coding for ENR5.2 LIGHT AIRCRAFT TRAINING AREA A WEST#-------------------------------------------------------------------

fig5_2_3 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.772,103.798,103.787,103.802,103.782,103.761,103.772], lat = [1.447,1.454,1.406,1.359,1.35,1.38,1.447],
    marker = { 'size': 1, 'color': "yellow" }))

fig5_2_3.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 10},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#Filled map coding for ENR5.2 LIGHT AIRCRAFT TRAINING AREA B#--------------------------------------------------------------------------------

fig5_2_4 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.772,103.819,103.838,103.866,103.889,103.823,103.772], lat = [1.447,1.368,1.376,1.374,1.427,1.458,1.447],
    marker = { 'size': 1, 'color': "red" }))

fig5_2_4.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 10},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})
#Filled map coding for ENR5.2 LIGHT AIRCRAFT TRAINING AREA B#-------------------------------------------------------------------------

fig5_2_5 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [103.761,103.782,103.819,103.772], lat = [1.38,1.35,1.368,1.447],
    marker = { 'size': 1, 'color': "purple" }))

fig5_2_5.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 10},
    height=650,width=950,
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

#coding for Query1-----------------------------------------------------------------------------------------------------
longitude = [0,0,0,0]
latitude = [0,0,0,0]

figQ1 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = longitude,
    lat = latitude,
    marker = { 'size': 10, 'color': "orange" }))

figQ1.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 103.761, 'lat': 1.38 },
        'zoom': 5},
    height=650,width=950,
    showlegend = False)

#danger area code for query3--------------------------------------------------------------------------------------------
fig5_1_WSD34Q3 = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [104.036,104.059,104.044,104.033],
    lat = [1.403,1.405,1.397,1.398,],
    name = 'WSD34 PULAU TEKONG',
    marker = { 'size': 1, 'color': "red" }))

fig5_1_WSD34Q3.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 103.831, 'lat': 1.638}, 'zoom': 8},
    height=650,width=850,
    showlegend = True,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig5_1_WSD34Q3.add_trace(go.Scattermapbox(
    mode="markers+lines",
    lon=[104.022, 104.514, 105.354, 106.522],
    lat=[1.415, 0.904, 0.407, -0.616],
    name='M635',
    marker={'size': 5}))


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def custom_input(paragraph_text,id, min_value=0, max_value=200, step=1): #def for Query1#
    return html.Div(
        children=[
            html.P(paragraph_text, style={"paddingRight": 10}),
            dbc.Input(type="float", min=min_value, max=max_value, step=step,id=id),
        ],
        style={"display": "flex"},
    )

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "19rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow": "scroll"
}

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",

}

sidebar = html.Div(
    [
        html.H2("e-AIP", className="display-4"),
        html.Hr(),
        html.P(
            "AIP SINGAPORE", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("ENR 2.1 FIR, UIR, TMA", href="/ENR2_1", active="exact"),
                dbc.NavLink("ENR 3 ATS ROUTES", href="/ENR3", active="exact"),
                dbc.NavLink("ENR 3.6 ENROUTE HOLDING", href="/ENR3_6", active="exact"),
                dbc.NavLink("ENR 4.1 RADIO NAVIGATION AIDS - ENROUTE", href="/ENR4_1", active="exact"),
                dbc.NavLink("ENR 4.4 NAME-CODE DESIGNATIONS FOR SIGNIFICANT POINTS", href="/ENR4_4", active="exact"),
                dbc.NavLink("ENR 4.5 AERONAUTICAL GROUND LIGHTS - ENROUTE", href="/ENR4_5", active="exact"),
                dbc.NavLink("ENR 5.1 PROHIBITED, RESTRICTED AND DANGER AREAS", href="/ENR5_1", active="exact"),
                dbc.NavLink("ENR 5.2 MILITARY EXERCISE AND TRAINING AREAS", href="/ENR5_2", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "QUREY", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Qurey1", href="/Query1", active="exact"),
                dbc.NavLink("Section Area", href="/Section_Area", active="exact"),
                dbc.NavLink("Danger Area", href="/Danger_Area", active="exact")
                ,
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,

)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("SINGAPORE CIVIL AVIATION AUTHORITY OF SINGAPORE",style={'text-align': 'center', 'fontSize': 30})

    elif pathname == "/ENR2_1" :
        return html.P(
            html.Div(children=[html.Div([
                html.H1("FIR, UIR, TMA", style={'text-align': 'center', 'fontSize': 30}),
                dash_table.DataTable(
                    id='adding-rows-table_2_1',
                    columns=[{"name": i, "id": i,
                              'deletable': False,  # enable to delete the column
                              'renamable': True  # enable to rename the column
                              } for i in df2_1.columns],

                    data=df2_1.to_dict('records'),  # design of the table
                    page_current=0,
                    page_size=15,
                    page_action='native',
                    sort_action='native',
                    column_selectable="single",
                    sort_mode='multi',
                    style_table={'overflowX': '',
                                 'maxHeight': '10000px'},
                    style_header={'backgroundColor': 'rgb(119, 184, 199)'},
                    style_cell={'backgroundColor': 'rgb(207,227,232)',
                                'color': 'black',
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'textAlign': 'left',
                                },
                    export_format='xlsx',  # export the table in csv
                    export_headers='display',
                    merge_duplicate_headers=True,
                    filter_action='native',  # filtering function
                    editable=True,  # allow editing in the table
                    row_deletable=True,  # deleting of rows
                    sort_by=[]),
            html.Button('Singapore FIR', id='button', n_clicks=0),
            html.Button('Section 1B', id='button2', n_clicks=0),
            html.Button('Section 1D', id='button3', n_clicks=0),
            html.Button('Section 1F', id='button4', n_clicks=0),
            html.Button('Section 2A', id='button5', n_clicks=0),
            html.Button('Section 2C', id='button6', n_clicks=0),
            html.Button('Section 2E', id='button7', n_clicks=0),
            html.Button('Section 2H', id='button8', n_clicks=0),
            html.Button('Combine', id='button9', n_clicks=0),

                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='graph', figure={})),
                       ])
            ])]))


    elif pathname == "/ENR3" :
        return html.P(
            html.Div(children=[html.Div([
                html.H1("AIR ROUTES", style={'text-align': 'center', 'fontSize': 30}),
                dash_table.DataTable(
                    id='adding-rows-table_3',
                    columns=[{"name": i, "id": i,
                              'deletable': False,  # enable to delete the column
                              'renamable': True  # enable to rename the column
                              } for i in df3.columns],
                    data=df3.to_dict('records'),  # design of the table
                    page_current=0,
                    page_size=20,
                    page_action='native',
                    sort_action='native',
                    column_selectable="single",
                    sort_mode='multi',
                    style_table={'overflowX': '',
                                 'maxHeight': '700px'},
                    style_header={'backgroundColor': 'rgb(119, 184, 199)'},
                    style_cell={'backgroundColor': 'rgb(207,227,232)',
                                'color': 'black',
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'textAlign': 'left',
                                },
                    export_format='xlsx',  # export the table in csv
                    export_headers='display',
                    merge_duplicate_headers=True,
                    filter_action='native',  # filtering function
                    editable=True,  # allow editing in the table
                    row_deletable=True,  # deleting of rows
                    sort_by=[]),
                dcc.Graph(figure=fig3),  # figure map

            ])
        ]))

    elif pathname == "/ENR3_6" :
        return html.P(
            html.Div(children=[html.Div([
                html.H1("ENROUTE HOLDING", style={'text-align': 'center', 'fontSize': 30}),

                dash_table.DataTable(
                    id='table3_6',
                    columns=[{"name": i, "id": i,
                              'deletable': False,  # enable to delete the column
                              'renamable': True  # enable to rename the column
                              } for i in df3_6.columns],

                    data=df3_6.to_dict('records'),  # design of the table
                    page_current=0,
                    page_size=20,
                    page_action='native',
                    sort_action='native',
                    column_selectable="single",
                    sort_mode='multi',
                    style_table={'overflowX': '',
                                 'maxHeight': '1500px'},
                    style_header={'backgroundColor': 'rgb(119, 184, 199)'},
                    style_cell={'backgroundColor': 'rgb(207,227,232)',
                                'color': 'black',
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'textAlign': 'left',
                                },
                    export_format='xlsx',  # export the table in csv
                    export_headers='display',
                    merge_duplicate_headers=True,
                    filter_action='native',  # filtering function
                    editable=True,  # allow editing in the table
                    row_deletable=True,  # deleting of rows
                    sort_by=[]),
                dcc.Graph(id='fig3_6',figure={}),

            ])
        ]))


    elif pathname == "/ENR4_1":
        return html.P(
            html.Div(children=[html.Div([
          html.H1("RADIO NAVIGATION AIDS - ENROUTE", style={'text-align': 'center','fontSize': 30}),

            #the title of the table
            dash_table.DataTable(  # starting of the table coding
                id='table4_1',
                columns=[{"name": i, "id": i,
                          'deletable': False,  # enable to delete the column
                          'renamable': True  # enable to rename the column
                          } for i in df4_1.columns],
                data=df4_1.to_dict('records'),  # design of the table
                page_current=0,
                page_size=20,
                page_action='native',
                sort_action='native',
                column_selectable="single",
                sort_mode='multi',
                style_table={'overflowX': '',
                             'maxHeight': '1000px'},
                style_header={'backgroundColor': 'rgb(119, 184, 199)'},
                style_cell={'backgroundColor': 'rgb(207,227,232)',
                            'color': 'black',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'textAlign': 'left',
                            },
                export_format='xlsx',  # export the table in csv
                export_headers='display',
                merge_duplicate_headers=True,
                filter_action='native',  # filtering function
                editable=True,  # allow editing in the table
                row_deletable=True,  # deleting of rows
                sort_by=[]),

                dcc.Graph(id='fig4_1',figure={}),


])
        ]))

    elif pathname == "/ENR4_4":
        return html.P(html.Div(children=[html.Div([
          html.H1("NAME-CODE DESIGNATIONS FOR SIGNIFICANT POINTS", style={'text-align': 'center','fontSize': 30}),

            dash_table.DataTable(
                id='table4_4',
                columns=[{"name": i, "id": i,
                          'deletable': False,  # enable to delete the column
                          'renamable': True  # enable to rename the column
                          } for i in df4_4.columns],
                data=df4_4.to_dict('records'),
                page_current=0,
                page_size=15,
                page_action='native',
                sort_action='native',
                column_selectable="single",
                sort_mode='multi',
                style_table={'overflowX': '',
                             'maxHeight': '600px'},
                # 'width': '50%'},
                style_header={'backgroundColor': 'rgb(110, 184, 199)'},
                style_cell={'backgroundColor': 'rgb(207,227,232)',
                            'color': 'black',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'textAlign': 'left',
                            },
                export_format='xlsx',  # export the table in csv
                export_headers='display',
                merge_duplicate_headers=True,
                filter_action='native',  # filtering function
                editable=True,  # allow editing in the table
                row_deletable=True,  # deleting of rows
                sort_by=[]),
                dcc.Graph(id='fig4_4',figure={}),
    ])
        ]))

    elif pathname == "/ENR4_5":
        return html.P(html.Div(children=[html.Div([
          html.H1("AERONAUTICAL GROUND LIGHTS - ENROUTE", style={'text-align': 'center','fontSize': 30}),

            dash_table.DataTable(
                id='table4_5',
                columns=[{"name": i, "id": i,
                          'deletable': False,  # enable to delete the column
                          'renamable': True  # enable to rename the column
                          } for i in df4_5.columns],
                data=df4_5.to_dict('records'),
                page_current=0,
                page_size=15,
                page_action='native',
                sort_action='native',
                column_selectable="single",
                sort_mode='multi',
                style_table={'overflowX': '',
                             'maxHeight': '600px'},
                # 'width': '50%'},
                style_header={'backgroundColor': 'rgb(110, 184, 199)'},
                style_cell={'backgroundColor': 'rgb(207,227,232)',
                            'color': 'black',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'textAlign': 'left',
                            },
                export_format='xlsx',  # export the table in csv
                export_headers='display',
                merge_duplicate_headers=True,
                filter_action='native',  # filtering function
                editable=True,  # allow editing in the table
                row_deletable=True,  # deleting of rows
                sort_by=[]),
                dcc.Graph(id='fig4_5',figure={}),
        ])
        ]))

    elif pathname == "/ENR5_1":
        return html.P(html.Div(children=[html.Div([
            html.H1("NAVIGATION WARNINGS", style={'text-align': 'center', 'fontSize': 30}),

            dash_table.DataTable(
                id='adding-rows-table_5_1',
                columns=[{"name": i, "id": i,
                          'deletable': False,  # enable to delete the column
                          'renamable': True  # enable to rename the column
                          } for i in df5_1.columns],
                data=df5_1.to_dict('records'),
                page_current=0,
                page_size=15,
                page_action='native',
                sort_action='native',
                column_selectable="single",
                sort_mode='multi',
                style_table={'overflowX': '',
                             'maxHeight': '1700px'},
                # 'width': '50%'},
                style_header={'backgroundColor': 'rgb(110, 184, 199)'},
                style_cell={'backgroundColor': 'rgb(207,227,232)',
                            'color': 'black',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'textAlign': 'left',
                            },
                export_format='xlsx',  # export the table in csv
                export_headers='display',
                merge_duplicate_headers=True,
                filter_action='native',  # filtering function
                editable=True,  # allow editing in the table
                row_deletable=True,  # deleting of rows
                sort_by=[]),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id='fig5_1', figure={})),
                    dbc.Col(dbc.DropdownMenu(
                        color='info',
                        label="Select",
                        id='5_1_dropdown',
                        children=[
                            dbc.DropdownMenuItem("RESTRICTED AREAS WMR104", id='RAWMR104'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD11 PASIR LABA", id='DAWSD11'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD11A PASIR LABA", id='DAWSD11A'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD11B PASIR LABA", id='DAWSD11B'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD13 AREA KILO", id='DAWSD13'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD14 AREA LIMA", id='DAWSD14'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD15 AREA MIKE", id='DAWSD15'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD20 AREA HOTEL", id='DAWSD20'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD34 PULAU TEKONG", id='DAWSD34'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD44", id='DAWSD44'),
                            dbc.DropdownMenuItem("DANGER AREAS WSD45", id='DAWSD45'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD8 CHINA SEA NORTH RANGE", id='DAWMD8'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD12 AREA JULIET", id='DAWMD12'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD21 AREA GOLF", id='DAWMD21'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD224 MALAYSIAN NAVAL EXERCISE AREA", id='DAWMD224'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD227 PULAU YU", id='DAWMD227'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD230 ULU TIRAM (SOUTH)", id='DAWMD230'),
                            dbc.DropdownMenuItem("DANGER AREAS WMD231 ULU TIRAM (NORTH)", id='DAWMD231'),

                        ]
                    )),
                    (html.P(id='fig5_1_output'))
                ])])
        ]))
    elif pathname == "/ENR5_2" :
        return html.P(
            html.Div(children=[html.Div([
                html.H1("MILITARY EXERCISE AND TRAINING AREAS", style={'text-align': 'center', 'fontSize': 30}),

                dash_table.DataTable(
                    id='adding-rows-table_5_2',
                    columns=[{"name": i, "id": i,
                              'deletable': False,  # enable to delete the column
                              'renamable': True  # enable to rename the column
                              } for i in df5_2.columns],

                    data=df5_2.to_dict('records'),  # design of the table
                    page_current=0,
                    page_size=20,
                    page_action='native',
                    sort_action='native',
                    column_selectable="single",
                    sort_mode='multi',
                    style_table={'overflowX': '',
                                 'maxHeight': '8000px'},
                    style_header={'backgroundColor': 'rgb(119, 184, 199)'},
                    style_cell={'backgroundColor': 'rgb(207,227,232)',
                                'color': 'black',
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'textAlign': 'left',
                                },
                    export_format='xlsx',  # export the table in csv
                    export_headers='display',
                    merge_duplicate_headers=True,
                    filter_action='native',  # filtering function
                    editable=True,  # allow editing in the table
                    row_deletable=True,  # deleting of rows
                    sort_by=[]),
                #html.Button('Add Row', id='editing-rows-button_5_2', n_clicks=0),
                html.Button('LIGHT AIRCRAFT TRAINING AREA A', id='buttonA', n_clicks=0),
                html.Button('LIGHT AIRCRAFT TRAINING AREA A (EAST)', id='buttonAE', n_clicks=0),
                html.Button('LIGHT AIRCRAFT TRAINING AREA A (WEST)', id='buttonAW', n_clicks=0),
                html.Button('LIGHT AIRCRAFT TRAINING AREA B', id='buttonB', n_clicks=0),
                html.Button('LIGHT AIRCRAFT TRAINING AREA C', id='buttonC', n_clicks=0),
                dcc.Graph(id='graph5_2', figure={})

            ])
            ]))

    elif pathname == "/Query1":
        return html.P(
            html.Div(children=[html.Div([
          html.H1("Query1", style={'text-align': 'center','fontSize': 30}),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="graphQ", figure=figQ1), md=8),
                    dbc.Col(
                        children=[
                            dbc.Row(
                                [
                                    dbc.Col(custom_input("Lat1",id="input1")),
                                    dbc.Col(custom_input("Long1",id="input2")),
                                ],
                                style={"paddingBottom": 30},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(custom_input("Lat2",id="input3")),
                                    dbc.Col(custom_input("Long2",id="input4")),
                                ],
                                style={"paddingBottom": 30},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(custom_input("Lat3",id="input5")),
                                    dbc.Col(custom_input("Long3",id="input6")),
                                ],
                                style={"paddingBottom": 30},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(custom_input("Lat4",id="input7")),
                                    dbc.Col(custom_input("Long4",id="input8")),
                                ],
                                style={"paddingBottom": 30},
                            ),
                            html.Div(id="output"),
                            html.Button('Submit', id='submit_button', n_clicks=0),
                        ],
                        md=4,
                    ),
                ]
            ),

        ])]))

    elif pathname == "/Section_Area":
        return html.P(
            html.Div(children=[html.Div([
          html.H1("SECTION AREA AIR ROUTES QUERY", style={'text-align': 'center','fontSize': 30}),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='graphQ2', figure={})),
                        dbc.Col(dbc.DropdownMenu(
                            color='info',
                            label="Select",
                            id='2_1_dropdown',
                            children=[
                                dbc.DropdownMenuItem("Singapore FIR", id='Singapore_FIR'),
                                dbc.DropdownMenuItem("Section 1B", id='Section_1B'),
                                dbc.DropdownMenuItem("Section 1D", id='Section_1D'),
                                dbc.DropdownMenuItem("Section 1F", id='Section_1F'),
                                dbc.DropdownMenuItem("Section 2A", id='Section_2A'),
                                dbc.DropdownMenuItem("Section 2C", id='Section_2C'),
                                dbc.DropdownMenuItem("Section 2E", id='Section_2E'),
                                dbc.DropdownMenuItem("Section 2H", id='Section_2H'),
                                dbc.DropdownMenuItem("Combine", id='Combine'),
                            ]
                        )),
                        (html.P(id='Q2_output'))
                        ])
            ])]))
    elif pathname == "/Danger_Area":
        return html.P(
            html.Div(children=[html.Div([
          html.H1("DANGER AREA AIR ROUTE QUERY", style={'text-align': 'center','fontSize': 30}),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='graphQ3', figure={})),
                        dbc.Col(dbc.DropdownMenu(
                            color='info',
                            label="Select",
                            id='3_1_dropdown',
                            children=[
                                dbc.DropdownMenuItem("RESTRICTED AREAS WMR104", id='Q3_RAWMR104'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD11 PASIR LABA", id='Q3_DAWSD11'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD11A PASIR LABA", id='Q3_DAWSD11A'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD11B PASIR LABA", id='Q3_DAWSD11B'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD13 AREA KILO", id='Q3_DAWSD13'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD14 AREA LIMA", id='Q3_DAWSD14'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD15 AREA MIKE", id='Q3_DAWSD15'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD20 AREA HOTEL", id='Q3_DAWSD20'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD34 PULAU TEKONG", id='Q3_DAWSD34'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD44", id='Q3_DAWSD44'),
                                dbc.DropdownMenuItem("DANGER AREAS WSD45", id='Q3_DAWSD45'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD8 CHINA SEA NORTH RANGE", id='Q3_DAWMD8'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD12 AREA JULIET", id='Q3_DAWMD12'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD21 AREA GOLF", id='Q3_DAWMD21'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD224 MALAYSIAN NAVAL EXERCISE AREA", id='Q3_DAWMD224'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD227 PULAU YU", id='Q3_DAWMD227'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD230 ULU TIRAM (SOUTH)", id='Q3_DAWMD230'),
                                dbc.DropdownMenuItem("DANGER AREAS WMD231 ULU TIRAM (NORTH)", id='Q3_DAWMD231'),

                            ]
                        )),
                        (html.P(id='Q3_output'))
                        ])
            ])]))

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


#CALLBACK FOR ENR2_1 MAP CALLBACK#-------------------------------------------------------------------------------------
@app.callback(
    Output('graph', 'figure'),
    Input('button', 'n_clicks'),
    Input('button2', 'n_clicks'),
    Input('button3', 'n_clicks'),
    Input('button4', 'n_clicks'),
    Input('button5', 'n_clicks'),
    Input('button6', 'n_clicks'),
    Input('button7', 'n_clicks'),
    Input('button8', 'n_clicks'),
    Input('button9', 'n_clicks'))

def clicked_output(button,button2,button3,button4,button5,button6,button7,button8,button9):
    ctx = dash.callback_context

    if (button==None)&(button2==None)&(button3==None)&(button4==None)&(button5==None)&(button6==None)&(button7==None)&(button8==None)&(button9==None):
        return ''
    else:
        pie = ctx.triggered[0]['prop_id'].split('.')[0]
        if pie == 'button':
            return fig1_1
        elif pie == 'button2':
            return fig1_2
        elif pie == 'button3':
            return fig1_3
        elif pie == 'button4':
            return fig1_4
        elif pie == 'button5':
            return fig1_5
        elif pie == 'button6':
            return fig1_6
        elif pie == 'button7':
            return fig1_7
        elif pie == 'button8':
            return fig1_8
        else :
            return fig1_9


#CALLBACK FOR TABLE 3#-------------------------------------------------------------------------------------------------
@app.callback(
        [Output('ATS_table', 'data'),
         Output('ATS_table', 'columns'),
         Output('ATS_table', 'page_size'),
         Output('ATS_map', 'figure' )],
        [Input('ATS_ROUTES_BUTTON', 'n_clicks'),
         Input('AREA_RNAV_BUTTON', 'n_clicks')]
)

def clicked_output(ATS_ROUTES_BUTTON,AREA_RNAV_BUTTON):
    ctx = dash.callback_context

    if (ATS_ROUTES_BUTTON==None)&(AREA_RNAV_BUTTON==None):
        return '','','',''
    else:
        pie = ctx.triggered[0]['prop_id'].split('.')[0]
        if pie == 'ATS_ROUTES_BUTTON':
            [data, columns, page_size,figure] = df3_1.to_dict('records'), [{'name': str(i), 'id': str(i),
                                                                     'deletable': False,  # enable to delete the column
                                                                     'renamable': True  # enable to rename the column
                                                                     } for i in df3_1.columns], 20,fig3_1

            return [data, columns, page_size,figure]

        else :
            [data, columns, page_size,figure] = df3_3.to_dict('records'), [{'name': str(i), 'id': str(i),
                                                                     'deletable': False,  # enable to delete the column
                                                                     'renamable': True  # enable to rename the column
                                                                     } for i in df3_3.columns], 20,fig3_3

            return [data, columns, page_size,figure]

#CALLBACK FOR TABLE 3_6#-------------------------------------------------------------------------------------------------
@app.callback(
    Output('fig3_6', 'figure'),
    Input('table3_6', 'derived_virtual_row_ids'),
    Input('table3_6', 'selected_row_ids'),
    Input('table3_6', 'active_cell'))
def update_graphs(row_ids, selected_row_ids, active_cell):

    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df3_6
        row_ids = df3_6['id']
    else:
        dff = df3_6.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['Selected' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else 'Not Selected'
              for id in row_ids]

    fig3_6b = px.scatter_mapbox(dff.to_dict('records'), lat="WPT_Coordinates_latitude",
                                lon="WPT_Coordinates_longitude",
                                hover_name="Id",
                                hover_data=["FIX"],
                                color=colors, zoom=9, height=650, width=950)
    fig3_6b.update_layout(mapbox_style="open-street-map")
    fig3_6b.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig3_6b

#CALLBACK FOR TABLE 4_1#-------------------------------------------------------------------------------------------------
@app.callback(
    Output('fig4_1', 'figure'),
    Input('table4_1', 'derived_virtual_row_ids'),
    Input('table4_1', 'selected_row_ids'),
    Input('table4_1', 'active_cell'))
def update_graphs(row_ids, selected_row_ids, active_cell):

    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df4_1
        row_ids = df4_1['id']
    else:
        dff = df4_1.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['Selected' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else 'Not Selected'
              for id in row_ids]

    fig4_1b = px.scatter_mapbox(dff.to_dict('records'), lat="Latitude", lon="Longitude",
                                hover_name="Name_of_station",
                                hover_data=["Id"],
                                color=colors, zoom=9, height=650, width=950)
    fig4_1b.update_layout(mapbox_style="open-street-map")
    fig4_1b.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig4_1b


#CALLBACK FOR TABLE 4_4#-------------------------------------------------------------------------------------------------
@app.callback(
    Output('fig4_4', 'figure'),
    Input('table4_4', 'derived_virtual_row_ids'),
    Input('table4_4', 'selected_row_ids'),
    Input('table4_4', 'active_cell'))
def update_graphs(row_ids, selected_row_ids, active_cell):

    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df4_4
        row_ids = df4_4['id']
    else:
        dff = df4_4.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['Selected' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else 'Not Selected'
              for id in row_ids]

    fig4_4b = px.scatter_mapbox(dff.to_dict('records'), lat="Latitude", lon="Longitude",
                                hover_name="Name_Code_designator",
                                hover_data=["Terminal_Area"],
                                color=colors, zoom=9, height=650, width=950)
    fig4_4b.update_layout(mapbox_style="open-street-map")
    fig4_4b.update_layout(
        mapbox={
            'style': "open-street-map",
            'center': {'lon': 104.002, 'lat': 1.37},
            'zoom': 8},
        height=650, width=950,
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0})
    return fig4_4b

#CALLBACK FOR TABLE 4_5#-------------------------------------------------------------------------------------------------
@app.callback(
    Output('fig4_5', 'figure'),
    Input('table4_5', 'derived_virtual_row_ids'),
    Input('table4_5', 'selected_row_ids'),
    Input('table4_5', 'active_cell'))
def update_graphs(row_ids, selected_row_ids, active_cell):

    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df4_5
        row_ids = df4_5['id']
    else:
        dff = df4_5.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['Selected' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else 'Not Selected'
              for id in row_ids]

    fig4_5b = px.scatter_mapbox(df4_5.to_dict('records'), lat="Latitude", lon="Longitude",
                               hover_name="Name_Ident_coordinates", hover_data=["Characteristics"],
                               color = colors, zoom=9, height=650, width=950)
    fig4_5b.update_layout(mapbox_style="open-street-map")
    fig4_5b.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig4_5b

#CALLBACK FOR TABLE 5_1#-----------------------------------------------------------------------------------------------
@app.callback(
          [Output('fig5_1', 'figure'),
           Output('fig5_1_output','children')],
         [Input('RAWMR104', 'n_clicks'),
          Input('DAWSD11', 'n_clicks'),
          Input('DAWSD11A', 'n_clicks'),
          Input('DAWSD11B', 'n_clicks'),
          Input('DAWSD13', 'n_clicks'),
          Input('DAWSD14', 'n_clicks'),
          Input('DAWSD15', 'n_clicks'),
          Input('DAWSD20', 'n_clicks'),
          Input('DAWSD34', 'n_clicks'),
          Input('DAWSD44', 'n_clicks'),
          Input('DAWSD45', 'n_clicks'),
          Input('DAWMD8', 'n_clicks'),
          Input('DAWMD12', 'n_clicks'),
          Input('DAWMD21', 'n_clicks'),
          Input('DAWMD224', 'n_clicks'),
          Input('DAWMD227', 'n_clicks'),
          Input('DAWMD230', 'n_clicks'),
          Input('DAWMD231', 'n_clicks')])

def dropdowntable(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        dropdown = "all"
    else:
        dropdown = ctx.triggered[0]['prop_id'].split('.')[0]
        if dropdown in ["RAWMR104"]:
            return fig5_1_RA,"You have select RESTRICTED AREA"
        elif dropdown in ["DAWSD11"]:
            return fig5_1_WSD11,"You have selected DANGER AREA WSD11 PASIR LABA"
        elif dropdown in ["DAWSD11A"]:
            return fig5_1_WSD11A, "You have selected DANGER AREA WSD11A PASIR LABA"
        elif dropdown in ["DAWSD11B"]:
            return fig5_1_WSD11B, "You have selected DANGER AREA WSD11B PASIR LABA"
        elif dropdown in ["DAWSD13"]:
            return fig5_1_WSD13, "You have selected DANGER AREA WSD13 AREA KILO"
        elif dropdown in ["DAWSD14"]:
            return fig5_1_WSD14, "You have selected DANGER AREA WSD13 AREA LIMA"
        elif dropdown in ["DAWSD15"]:
            return fig5_1_WSD15, "You have selected DANGER AREA WSD13 AREA MIKE"
        elif dropdown in ["DAWSD20"]:
            return fig5_1_WSD15, "You have selected DANGER AREA WSD13 AREA HOTEL"
        elif dropdown in ["DAWSD34"]:
            return fig5_1_WSD34,"You have select DANGER AREA WSD34 PULAU TEKONG"
        elif dropdown in ["DAWSD44"]:
            return fig5_1_WSD44, "You have select DANGER AREA WSD44"
        elif dropdown in ["DAWSD45"]:
            return fig5_1_WSD45, "You have select DANGER AREA WSD45"
        elif dropdown in ["DAWMD8"]:
            return fig5_1_WMD8, "You have select DANGER AREA WMD8 CHINA SEA NORTH RANGE"
        elif dropdown in ["DAWMD12"]:
            return fig5_1_WMD12, "You have select DANGER AREA WMD12 AREA JULIET"
        elif dropdown in ["DAWMD21"]:
            return fig5_1_WMD21, "You have select DANGER AREA WMD21 AREA GOLF"
        elif dropdown in ["DAWMD224"]:
            return fig5_1_WMD224, "You have select DANGER AREA MALAYSIAN NAVAL EXERCISE AREA"
        elif dropdown in ["DAWMD227"]:
            return fig5_1_WMD227, "You have select DANGER AREA WMD227 PULAU YU"
        elif dropdown in ["DAWMD230"]:
            return fig5_1_WMD230, "You have select DANGER AREA WMD230 ULU TIRAM (SOUTH)"
        else:
            return fig5_1_WMD231, "You have select DANGER AREA WMD230 ULU TIRAM (NORTH)"
    raise PreventUpdate

#CALLBACK FOR ENR5_2 MAP CALLBACK#------------------------------------------------------------------------------------
@app.callback(
    Output('graph5_2', 'figure'),
    Input('buttonA', 'n_clicks'),
    Input('buttonAE', 'n_clicks'),
    Input('buttonAW', 'n_clicks'),
    Input('buttonB', 'n_clicks'),
    Input('buttonC', 'n_clicks'),)

def clicked_output(buttonA,buttonAE,buttonAW,buttonB,buttonC):
    ctx = dash.callback_context

    if (buttonA==None)&(buttonAE==None)&(buttonAW==None)&(buttonB==None)&(buttonC==None):
        return ''
    else:
        pie = ctx.triggered[0]['prop_id'].split('.')[0]
        if pie == 'buttonA':
            return fig5_2_1
        elif pie == 'buttonAE':
            return fig5_2_2
        elif pie == 'buttonAW':
            return fig5_2_3
        elif pie == 'buttonB':
            return fig5_2_4
        else :
            return fig5_2_5

#Qurey1 callacbk -------------------------------------------------------------------------------------------------------
@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value"),
    Input("input4", "value"),
    Input("input5", "value"),
    Input("input6", "value"),
    Input("input7", "value"),
    Input("input8", "value"),
)
def update_output(input1,input2,input3,input4,input5,input6,input7,input8):
    latitude[0]=input1
    latitude[1]=input3
    latitude[2]=input5
    latitude[3]=input7
    longitude[0]=input2
    longitude[1]=input4
    longitude[2]=input6
    longitude[3]=input8
    return 'Lat1: {} and Long1: {}\nLat2: {} and Long2: {}\nLat3: {} and Long3: {}\nLat4: {} and Long4: {}'.format(input1, input2, input3, input4,input5,input6,input7,input8)

@app.callback(
    Output('graphQ','figure'),
    Input('submit_button','n_clicks'))
def update_graphQ(n_clicks):
    figQ1 = go.Figure(go.Scattermapbox(
        fill = "toself",
        lon = longitude,
        lat = latitude,
        marker = { 'size': 10, 'color': "orange" }))

    figQ1.update_layout(
        mapbox = {
            'style': "stamen-terrain",
            'center': {'lon': 105, 'lat': 1.56 },
            'zoom': 5},
        height=650, width=850,
        showlegend = True)

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.872],
        lat=[1.664, 2.388],
        name='A224',
        marker={'size': 5}, ))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.287, 102.881],
        lat=[1.664, 1.848, 2.047],
        name='A457',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.12, 103.34, 103.414, 103.629, 103.856, 104.514],
        lat=[1.615, 1.498, 1.458, 1.344, 1.222, 0.904],
        name='A464',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.089, 103.336, 103.619, 103.856],
        lat=[1.552, 1.447, 1.324, 1.222],
        name='A576',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.872, 103.97, 104.022, 104.313, 104.735, 104.867],
        lat=[2.388, 1.758, 1.415, 0.817, -0.023, -0.283],
        name='B338',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.211],
        lat=[1.664, 2.018],
        name='B466',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.423, 103.526, 103.643, 103.719, 103.872, 103.901, 103.912, 103.923, 103.933, 103.856, 104.045, 104.407,
             104.576],
        lat=[3.383, 3.155, 2.895, 2.727, 2.388, 1.922, 1.756, 1.59, 1.423, 1.222, 0.755, -0.208, -0.483, ],
        name='B469',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.856, 104.135, 104.701, 104.867],
        lat=[1.222, 0.805, -0.04, -0.283],
        name='B470',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.041, 104.033, 104.022],
        lat=[2.614, 1.915, 1.415],
        name='G219',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.111, 104.468, 105.998, 108.927],
        lat=[2.916, 2.875, 2.669, 2.578],
        name='G334',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.712, 103.743, 103.79, 103.856, 103.96, 104.05, 104.155, 104.217],
        lat=[1.664, 1.5, 1.439, 1.348, 1.222, 0.728, 0.273, -0.268, -0.567, ],
        name='G579',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.856, 104.405, 105.788, 106.759, 107.991, 108.5],
        lat=[1.222, 1.33, 1.363, 1.385, 1.414, 1.428],
        name='G580',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.585, 103.223],
        lat=[6.937, 5.753],
        name='R208',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.083, 103.661],
        lat=[2.332, 1.664],
        name='R325',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[102.269, 103.165, 103.498, 103.882],
        lat=[0.7, 0.997, 1.042, 1.092],
        name='R469',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.405, 103.99, 103.828, 103.712, 103.414, 103.336],
        lat=[1.33, 1.522, 1.509, 1.5, 1.458, 1.447],
        name='W401',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.022, 103.882],
        lat=[1.415, 1.092],
        name='W407',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[102.892, 103.661],
        lat=[1.737, 1.664],
        name='W534',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.99],
        lat=[1.664, 1.522],
        name='W651',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[106.931, 109],
        lat=[0.418, 0],
        name='L504',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[109.582, 111.109],
        lat=[4.256, 4.287],
        name='L517',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[110.218, 106.926, 106.407, 105.788],
        lat=[8.215, 3.561, 2.559, 1.363],
        name='L625',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[105.38, 104.799, 104.095, 103.728, 103.423],
        lat=[4.811, 4.387, 3.873, 3.606, 3.383],
        name='L629',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[106.213, 105.263, 104.761, 104.131, 103.823, 103.423],
        lat=[4.288, 3.98, 3.817, 3.613, 3.513, 3.383],
        name='L635',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[105.555, 104.245, 104.095, 104.013, 103.95, 103.872],
        lat=[7, 4.873, 3.873, 3.326, 2.911, 2.388],
        name='L642',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[106.81, 106.213, 106.355, 106.388, 106.47, 106.545, 106.64, 106.6963, 106.759, 107.09],
        lat=[7, 4.288, 3.532, 3.354, 2.92, 2.521, 2.016, 1.7155, 1.385, -0.379],
        name='L644',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[114.808, 114.833, 114.848],
        lat=[9.827, 8.192, 7.148],
        name='L649',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.165, 102.138],
        lat=[0.997, 1.397],
        name='L762',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[116.23, 116.195],
        lat=[8.642, 8.183],
        name='M522',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[102.984, 103.498, 104.514],
        lat=[1.385, 1.042, 0.904],
        name='M630',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.022, 104.514, 105.354, 106.522],
        lat=[1.415, 0.904, 0.407, -0.616],
        name='M635',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[108.927, 107.846, 107.44, 106.696, 105.788],
        lat=[2.578, 2.161, 2.003, 1.716, 1.363],
        name='M646',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.132, 104.245],
        lat=[7, 4.873],
        name='M753',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[116.23, 116.015],
        lat=[8.642, 8.045],
        name='M754',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.423, 103.929, 104.113, 104.526, 105.21, 105.805, 106.926, 109.582, 111.855],
        lat=[3.383, 3.409, 3.418, 3.439, 3.474, 3.504, 3.561, 4.256, 4.836],
        name='M758',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.423, 104.162, 104.335, 104.673, 105.191, 107.099, 107.846, 108.5],
        lat=[3.383, 3.178, 3.131, 3.038, 2.895, 2.368, 2.161, 1.978],
        name='M761',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.585, 102.817],
        lat=[6.937, 6.48],
        name='M765',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[115.862, 112.593, 109.582, 107.099, 105.788],
        lat=[8.949, 6.527, 4.256, 2.368, 1.363],
        name='M767',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[110.218, 111.545, 112.593, 113.346],
        lat=[8.215, 7.276, 6.527, 5.985, ],
        name='M768',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[106.81, 105.38, 105.004, 104.761, 104.526, 104.335, 104.287, 103.872],
        lat=[7, 4.811, 4.207, 3.817, 3.439, 3.131, 3.055, 2.388],
        name='M771',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[114.808, 113.929, 113.346],
        lat=[9.827, 7.517, 5.985],
        name='M772',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.514, 106.931, 107.728],
        lat=[0.904, 0.418, -0.113],
        name='M774',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[102.833, 103.025, 103.344, 104.245],
        lat=[6.875, 6.604, 6.151, 4.873],
        name='M904',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.498, 104.217],
        lat=[1.042, -0.567],
        name='N502',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.245, 104.799, 105.004, 105.263, 105.537, 105.805, 106.101, 107.099, 107.44, 107.991, 108.813],
        lat=[4.873, 4.387, 4.207, 3.98, 3.739, 3.504, 3.244, 2.368, 2.003, 1.414, 0.528],
        name='N875',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[114.808, 111.545, 106.926, 106.101, 105.191, 104.659, 103.872],
        lat=[9.827, 7.276, 3.561, 3.244, 2.895, 2.69, 2.388],
        name='N884',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.585, 103.919, 104.245, 104.131, 104.113, 104.098, 104.094, 103.933],
        lat=[6.937, 5.894, 4.873, 3.613, 3.418, 3.242, 3.198, 1.423],
        name='N891',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[108.153, 106.213, 105.537, 105.21, 104.673, 104.468, 104.105, 103.872],
        lat=[7.089, 4.288, 3.739, 3.474, 3.038, 2.875, 2.577, 2.388],
        name='N892',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.12, 103.351, 103.498, 104.867],
        lat=[1.615, 1.266, 1.042, -0.283],
        name='P501',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[105.555, 104.475],
        lat=[7, 4.869],
        name='Q801',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.132, 104.475, 104.558],
        lat=[7, 4.869, 4.211],
        name='Q802',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.344, 103.989, 104.162, 104.558],
        lat=[6.151, 4.853, 4.658, 4.211],
        name='Q803',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.132, 103.989, 103.929],
        lat=[7, 4.853, 3.409],
        name='T611',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[105.38, 103.929],
        lat=[4.811, 3.409],
        name='T612',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.677, 103.526],
        lat=[3.843, 3.155],
        name='Y332',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.728, 103.526],
        lat=[3.606, 3.155],
        name='Y333',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.823, 103.526],
        lat=[3.513, 3.155],
        name='Y334',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.929, 103.526],
        lat=[3.409, 3.155],
        name='Y335',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[104.162, 103.526],
        lat=[3.178, 3.155],
        name='Y336',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.912, 103.406],
        lat=[1.756, 2.146],
        name='Y339',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.661, 103.406],
        lat=[1.664, 2.146],
        name='Y342',
        marker={'size': 5}))

    figQ1.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=[103.222, 103.642],
        lat=[3.291, 2.895],
        name='Y514',
        marker={'size': 5}))

    return figQ1

#callback for Query2 sector area-----------------------------------------------------------------------------------

@app.callback(
          [Output('graphQ2', 'figure'),
          Output('Q2_output','children')],
         [Input('Singapore_FIR', 'n_clicks'),
          Input('Section_1B', 'n_clicks'),
          Input('Section_1D', 'n_clicks'),
          Input('Section_1F', 'n_clicks'),
          Input('Section_2A', 'n_clicks'),
          Input('Section_2C', 'n_clicks'),
          Input('Section_2E', 'n_clicks'),
          Input('Section_2H','n_clicks'),
          Input('Combine', 'n_clicks')])

def dropdowntable(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        dropdown = "all"
    else:
        dropdown = ctx.triggered[0]['prop_id'].split('.')[0]
        if dropdown in ["Singapore_FIR"]:
            return fig1_1SA,"You have select SINGAPORE FIR"
        elif dropdown in ["Section_1B"] :
            return fig1_2SA,"You have select SECTION 1B"
        elif dropdown in ["Section_1D"] :
            return fig1_3SA,"You have select SECTION 1D"
        elif dropdown in ["Section_1F"] :
            return fig1_4SA,"You have select SECTION 1F"
        elif dropdown in ["Section_2A"] :
            return fig1_5SA,"You have select SECTION 2A"
        elif dropdown in ["Section_2C"] :
            return fig1_6SA,"You have select SECTION 2C"
        elif dropdown in ["Section_2E"] :
            return fig1_7SA,"You have select SECTION 2E"
        elif dropdown in ["Section_2H"]:
            return fig1_8SA,"You have select SECTION 2H"
        else:
            return fig1_9SA,"You have select COMBINE"
    raise PreventUpdate

#callback for Query3 danger area-----------------------------------------------------------------------------------

@app.callback(
          [Output('graphQ3', 'figure'),
           Output('Q3_output','children')],
         [Input('Q3_RAWMR104', 'n_clicks'),
          Input('Q3_DAWSD11', 'n_clicks'),
          Input('Q3_DAWSD11A', 'n_clicks'),
          Input('Q3_DAWSD11B', 'n_clicks'),
          Input('Q3_DAWSD13', 'n_clicks'),
          Input('Q3_DAWSD14', 'n_clicks'),
          Input('Q3_DAWSD15', 'n_clicks'),
          Input('Q3_DAWSD20', 'n_clicks'),
          Input('Q3_DAWSD34', 'n_clicks'),
          Input('Q3_DAWSD44', 'n_clicks'),
          Input('Q3_DAWSD45', 'n_clicks'),
          Input('Q3_DAWMD8', 'n_clicks'),
          Input('Q3_DAWMD12', 'n_clicks'),
          Input('Q3_DAWMD21', 'n_clicks'),
          Input('Q3_DAWMD224', 'n_clicks'),
          Input('Q3_DAWMD227', 'n_clicks'),
          Input('Q3_DAWMD230', 'n_clicks'),
          Input('Q3_DAWMD231', 'n_clicks')])

def dropdowntable(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        dropdown = "all"
    else:
        dropdown = ctx.triggered[0]['prop_id'].split('.')[0]
        if dropdown in ["Q3_RAWMR104"]:
            return fig5_1_1SA,"You have select RESTRICTED AREA"
        elif dropdown in ["Q3_DAWSD11"]:
            return fig5_1_WSD11,"You have selected DANGER AREA WSD11 PASIR LABA"
        elif dropdown in ["Q3_DAWSD11A"]:
            return fig5_1_WSD11A, "You have selected DANGER AREA WSD11A PASIR LABA"
        elif dropdown in ["Q3_DAWSD11B"]:
            return fig5_1_WSD11B, "You have selected DANGER AREA WSD11B PASIR LABA"
        elif dropdown in ["Q3_DAWSD13"]:
            return fig5_1_WSD13, "You have selected DANGER AREA WSD13 AREA KILO"
        elif dropdown in ["Q3_DAWSD14"]:
            return fig5_1_WSD14, "You have selected DANGER AREA WSD13 AREA LIMA"
        elif dropdown in ["Q3_DAWSD15"]:
            return fig5_1_WSD15, "You have selected DANGER AREA WSD13 AREA MIKE"
        elif dropdown in ["Q3_DAWSD20"]:
            return fig5_1_WSD15, "You have selected DANGER AREA WSD13 AREA HOTEL"
        elif dropdown in ["Q3_DAWSD34"]:
            return fig5_1_WSD34Q3,"You have select DANGER AREA WSD34 PULAU TEKONG"
        elif dropdown in ["Q3_DAWSD44"]:
            return fig5_1_WSD44, "You have select DANGER AREA WSD44"
        elif dropdown in ["Q3_DAWSD45"]:
            return fig5_1_WSD45, "You have select DANGER AREA WSD45"
        elif dropdown in ["Q3_DAWMD8"]:
            return fig5_1_WMD8, "You have select DANGER AREA WMD8 CHINA SEA NORTH RANGE"
        elif dropdown in ["Q3_DAWMD12"]:
            return fig5_1_WMD12, "You have select DANGER AREA WMD12 AREA JULIET"
        elif dropdown in ["Q3_DAWMD21"]:
            return fig5_1_WMD21, "You have select DANGER AREA WMD21 AREA GOLF"
        elif dropdown in ["Q3_DAWMD224"]:
            return fig5_1_WMD224, "You have select DANGER AREA MALAYSIAN NAVAL EXERCISE AREA"
        elif dropdown in ["Q3_DAWMD227"]:
            return fig5_1_WMD227, "You have select DANGER AREA WMD227 PULAU YU"
        elif dropdown in ["Q3_DAWMD230"]:
            return fig5_1_WMD230, "You have select DANGER AREA WMD230 ULU TIRAM (SOUTH)"
        else:
            return fig5_1_WMD231, "You have select DANGER AREA WMD230 ULU TIRAM (NORTH)"
    raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)