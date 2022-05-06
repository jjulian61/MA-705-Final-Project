# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:10:10 2022

@author: jjuli
"""
#Run the one Line below by itself, if there is an issue Loading the Dashboard
#env FLASK_ENV=development FLASK_APP=hello.py flask run

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

#Unorganized Pickle Data
bf = pd.read_pickle('listings.pkl')
print(bf)

#Pickle Data Organized into usable Dataframe
df = pd.DataFrame({
"Price":	[169000000,135000000,79000000,68000000,66000000,65000000,63815000,63500000,62000000,58500000,57500000,55000000,53000000,49900000,49500000,46505000,45000000,45000000,42000000,41000000,40000000,39999999,39950000,39000000,38500000,38000000,38000000,35950000,35000000,35000000,35000000,35000000,35000000,35000000,34995000,34500000,34000000,33500000,33000000,32000000],
"Listers":	["SERHANT", "ENGEL & VÖLKERS NEW YORK REAL ESTATE", "SOTHEBY'S INTERNATIONAL REALTY", "CORCORAN", "CORCORAN", "CORCORAN", "DOUGLAS ELLIMAN", "EXTELL MARKETING GROUP LLC", "CORCORAN", "DOUGLAS ELLIMAN", "CORCORAN", "DOLLY LENZ REAL ESTATE LLC", "BROWN HARRIS STEVENS", "MODLIN GROUP", "CORCORAN", "DOUGLAS ELLIMAN", "DOUGLAS ELLIMAN", "COMPASS", "SOTHEBY'S INTERNATIONAL REALTY", "COMPASS", "DOUGLAS ELLIMAN", "SOTHEBY'S INTERNATIONAL REALTY", "ZECKENDORF MARKETING", "BROWN HARRIS STEVENS", "SOTHEBY'S INTERNATIONAL REALTY", "BROWN HARRIS STEVENS", "DOLLY LENZ REAL ESTATE LLC", "DOUGLAS ELLIMAN", "BROWN HARRIS STEVENS", "COMPASS", "DOUGLAS ELLIMAN", "DOUGLAS ELLIMAN", "CORCORAN", "CORCORAN", "CORCORAN", "DOUGLAS ELLIMAN", "DOUGLAS ELLIMAN", "DOUGLAS ELLIMAN", "CORCORAN", "RESERV"],
"Address":	["432 Park Ave #PENTHOUSE New York NY 10022432", "Park Ave APT 79 New York NY 100222", "Park Pl New York NY 10007432", "Park Ave APT 71 New York NY 10022111", "W 57th St PENTHOUSE 72 New York NY 1001970", "Vestry St #S New York NY 1001353", "W 53rd St PENTHOUSE 76 New York NY 10019217", "W 57th St #114 New York NY 1001923", "E 22nd St New York NY 10010151", "E 58th St PENTHOUSE 50 New York NY 1002215", "Central Park W PENTHOUSE 43 New York NY 100232", "E 67th St #5FULLFLOOR New York NY 10065165", "Charles St New York NY 1001425", "Columbus Cir FLOOR 80 New York NY 1001935", "Hudson Yards PENTHOUSE 90 New York NY 1000153", "W 53rd St #64 New York NY 1001915", "Central Park W PENTHOUSE 41 New York NY 1002330", "Park Pl #81 New York NY 10007555", "W End Ave #PENTHOUSE New York NY 1002433", "E 74th St New York NY 10021111", "Murray St PENTHOUSE 2 New York NY 1000725", "Columbus Cir #75CE New York NY 1001950", "United Nations Plz #DPH42 New York NY 10017820", "5th Ave FLOOR 3 New York NY 10065781", "5th Ave FLOOR 18 New York NY 10022200", "Amsterdam Ave PENTHOUSE 2 New York NY 100231", "E 62nd St New York NY 1006524", "Leonard St New York NY 100131045", "Madison Ave #DPLX1011 New York NY 10075730", "Park Ave #10/11C New York NY 10021100", "Vandam St #20/21 New York NY 10013443", "Greenwich St PENTHOUSE G New York NY 10013432", "Park Ave APT 71A New York NY 10022432", "Park Ave APT 71B New York NY 10022944", "5th Ave FLOOR 3 New York NY 10021224", "Mulberry St New York NY 10012217", "W 57th St APT 91E New York NY 1001911", "E 68th St PENTHOUSE W New York NY 10065180", "88th St New York NY 10128383", "W Broadway #PENTHOUSE New York NY 10012"],
"Beds":	[6,5,1,6,4,5,4,5,5,5,3,6,6,5,5,4,4,4,6,5,5,5,5,6,6,4,5,6,10,7,6,4,3,3,4,4,4,5,5,4],
"Baths":	[9,7,1,8,10,8,4,6,7,6,6,8,9,7,7,5,4,5,7,7,7,7,8,7,9,5,5,7,10,11,7,6,5,5,5,5,5,6,6,6],
"Sq. Ft.":	[8255, 8055, 9680, 8108, 7130, 7808, 7973, 7074, 6850, 9675, 4739, 0, 9607, 8274, 10171, 6617, 4024, 5443, 8429, 10088, 7488, 4540, 9704, 0, 0, 6347, 5100, 7300, 0, 0, 6569, 5375, 4019, 4019, 0, 5646, 4296, 6189, 5508, 7500]

})

fig = px.bar(df, x="Price", y="Sq. Ft.", color="Listers")



app.layout = html.Div([
    html.H1('The 40 Most Expensive NY Condos on Zillow',
            style={'textAlign' : 'center'}),
    html.H1(
        children='By John Julian',
        style={
            'textAlign': 'center'
        }),
    html.Div(children='This DashBoard should be used as a tool compare some of the most expensive properties in New York City', style={
        'textAlign': 'left'
    }),
    html.Div(children='----------', style={
        'textAlign': 'left',
    }),

    html.Div(children='How to use this Dash Board:', style={
        'textAlign': 'left',

    }),
    html.Div(children='Highlight a Company on the right to see the properties listed under them.', style={
        'textAlign': 'left',
       
    }),
    html.Div(children='----------', style={
        'textAlign': 'left',
        
    }),
    html.Div(children='The bar graph compares relevant properties by price and square feet', style={
        'textAlign': 'left',
      
    }),
    html.Div(children='The table below gives an output corresponding to selected Addresses', style={
        'textAlign': 'left',
        
    }),
    html.Div(children='----------', style={
        'textAlign': 'left',
        
    }),
    html.Div(children='Both the table and bar graph are sorted by price in ascending order', style={
        'textAlign': 'left',
        
    }),
    html.Div(children='----------', style={
        'textAlign': 'left',
        
    }),
    html.Div(children='Properties listed with square footage of 0 were listed on Zillow as having square footage of --', style={
        'textAlign': 'left',
        
    }),
    dcc.Graph(figure=fig, id='plot'),
    html.Div([html.H4('Filter Out Addresses'),
              dcc.Checklist(
                  options=[{'label': '432 Park Ave #PENTHOUSE New York NY 10022432', 'value': '432 Park Ave #PENTHOUSE New York NY 10022432'},
                           {'label': 'Park Ave APT 79 New York NY 100222', 'value': 'Park Ave APT 79 New York NY 100222'},
                           {'label': 'Park Pl New York NY 10007432', 'value': 'Park Pl New York NY 10007432'},
                           {'label': 'Park Ave APT 71 New York NY 10022111', 'value': 'Park Ave APT 71 New York NY 10022111'},
                           {'label': 'W 57th St PENTHOUSE 72 New York NY 1001970', 'value': 'W 57th St PENTHOUSE 72 New York NY 1001970'},
                           {'label': 'Vestry St #S New York NY 1001353', 'value': 'Vestry St #S New York NY 1001353'},
                           {'label': 'W 53rd St PENTHOUSE 76 New York NY 10019217', 'value': 'W 53rd St PENTHOUSE 76 New York NY 10019217'},
                           {'label': 'W 57th St #114 New York NY 1001923', 'value': 'W 57th St #114 New York NY 1001923'},
                           {'label': 'E 22nd St New York NY 10010151', 'value': 'E 22nd St New York NY 10010151'},
                           {'label': 'E 58th St PENTHOUSE 50 New York NY 1002215', 'value': 'E 58th St PENTHOUSE 50 New York NY 1002215'},
                           {'label': 'Central Park W PENTHOUSE 43 New York NY 100232', 'value': 'Central Park W PENTHOUSE 43 New York NY 100232'},
                           {'label': 'E 67th St #5FULLFLOOR New York NY 10065165', 'value': 'E 67th St #5FULLFLOOR New York NY 10065165'},
                           {'label': 'Charles St New York NY 1001425', 'value': 'Charles St New York NY 1001425'},
                           {'label': 'Columbus Cir FLOOR 80 New York NY 1001935', 'value': 'Columbus Cir FLOOR 80 New York NY 1001935'},
                           {'label': 'Hudson Yards PENTHOUSE 90 New York NY 1000153', 'value': 'Hudson Yards PENTHOUSE 90 New York NY 1000153'},
                           {'label': 'W 53rd St #64 New York NY 1001915', 'value': 'W 53rd St #64 New York NY 1001915'},
                           {'label': 'Central Park W PENTHOUSE 41 New York NY 1002330', 'value': 'Central Park W PENTHOUSE 41 New York NY 1002330'},
                           {'label': 'Park Pl #81 New York NY 10007555', 'value': 'Park Pl #81 New York NY 10007555'},
                           {'label': 'W End Ave #PENTHOUSE New York NY 1002433', 'value': 'W End Ave #PENTHOUSE New York NY 1002433'},
                           {'label': 'E 74th St New York NY 10021111', 'value': 'E 74th St New York NY 10021111'},
                           {'label': 'Murray St PENTHOUSE 2 New York NY 1000725', 'value': 'Murray St PENTHOUSE 2 New York NY 1000725'},
                           {'label': 'Columbus Cir #75CE New York NY 1001950', 'value': 'Columbus Cir #75CE New York NY 1001950'},
                           {'label': 'United Nations Plz #DPH42 New York NY 10017820', 'value': 'United Nations Plz #DPH42 New York NY 10017820'},
                           {'label': '5th Ave FLOOR 3 New York NY 10065781', 'value': '5th Ave FLOOR 3 New York NY 10065781'},
                           {'label': '5th Ave FLOOR 18 New York NY 10022200', 'value': '5th Ave FLOOR 18 New York NY 10022200'},
                           {'label': 'Amsterdam Ave PENTHOUSE 2 New York NY 100231', 'value': 'Amsterdam Ave PENTHOUSE 2 New York NY 100231'},
                           {'label': 'E 62nd St New York NY 1006524', 'value': 'E 62nd St New York NY 1006524'},
                           {'label': 'Leonard St New York NY 100131045', 'value': 'Leonard St New York NY 100131045'},
                           {'label': 'Madison Ave #DPLX1011 New York NY 10075730', 'value': 'Madison Ave #DPLX1011 New York NY 10075730'},
                           {'label': 'Park Ave #10/11C New York NY 10021100', 'value': 'Park Ave #10/11C New York NY 10021100'},
                           {'label': 'Vandam St #20/21 New York NY 10013443', 'value': 'Vandam St #20/21 New York NY 10013443'},
                           {'label': 'Greenwich St PENTHOUSE G New York NY 10013432', 'value': 'Greenwich St PENTHOUSE G New York NY 10013432'},
                           {'label': 'Park Ave APT 71A New York NY 10022432', 'value': 'Park Ave APT 71A New York NY 10022432'},
                           {'label': 'Park Ave APT 71B New York NY 10022944', 'value': 'Park Ave APT 71B New York NY 10022944'},
                           {'label': '5th Ave FLOOR 3 New York NY 10021224', 'value': '5th Ave FLOOR 3 New York NY 10021224'},
                           {'label': 'Mulberry St New York NY 10012217', 'value': 'Mulberry St New York NY 10012217'},
                           {'label': 'W 57th St APT 91E New York NY 1001911', 'value': 'W 57th St APT 91E New York NY 1001911'},
                           {'label': 'E 68th St PENTHOUSE W New York NY 10065180', 'value': 'E 68th St PENTHOUSE W New York NY 10065180'},
                           {'label': '88th St New York NY 10128383', 'value': '88th St New York NY 10128383'},
                           {'label': 'W Broadway #PENTHOUSE New York NY 10012', 'value': 'W Broadway #PENTHOUSE New York NY 10012'}],
                           
                  value=['432 Park Ave #PENTHOUSE New York NY 10022432', 'Park Ave APT 79 New York NY 100222', 'Park Pl New York NY 10007432', 'Park Ave APT 71 New York NY 10022111', 'W 57th St PENTHOUSE 72 New York NY 1001970', 'Vestry St #S New York NY 1001353', 'W 53rd St PENTHOUSE 76 New York NY 10019217', 'W 57th St #114 New York NY 1001923', 'E 22nd St New York NY 10010151', 'E 58th St PENTHOUSE 50 New York NY 1002215', 'Central Park W PENTHOUSE 43 New York NY 100232', 'E 67th St #5FULLFLOOR New York NY 10065165', 'Charles St New York NY 1001425', 'Columbus Cir FLOOR 80 New York NY 1001935', 'Hudson Yards PENTHOUSE 90 New York NY 1000153', 'W 53rd St #64 New York NY 1001915', 'Central Park W PENTHOUSE 41 New York NY 1002330', 'Park Pl #81 New York NY 10007555', 'W End Ave #PENTHOUSE New York NY 1002433', 'E 74th St New York NY 10021111', 'Murray St PENTHOUSE 2 New York NY 1000725', 'Columbus Cir #75CE New York NY 1001950', 'United Nations Plz #DPH42 New York NY 10017820', '5th Ave FLOOR 3 New York NY 10065781', '5th Ave FLOOR 18 New York NY 10022200', 'Amsterdam Ave PENTHOUSE 2 New York NY 100231', 'E 62nd St New York NY 1006524', 'Leonard St New York NY 100131045', 'Madison Ave #DPLX1011 New York NY 10075730', 'Park Ave #10/11C New York NY 10021100', 'Vandam St #20/21 New York NY 10013443', 'Greenwich St PENTHOUSE G New York NY 10013432', 'Park Ave APT 71A New York NY 10022432', 'Park Ave APT 71B New York NY 10022944', '5th Ave FLOOR 3 New York NY 10021224', 'Mulberry St New York NY 10012217', 'W 57th St APT 91E New York NY 1001911', 'E 68th St PENTHOUSE W New York NY 10065180', '88th St New York NY 10128383', 'W Broadway #PENTHOUSE New York NY 10012'],
                  id = 'checklist')],
             style={'width' : '50%', 'float' : 'right'}),
    html.Div(id='table')
    ])



@app.callback(
    Output("table", "children"),
    Input("checklist", "value")
)
def update_table(cities):
    x = df[df.Address.isin(cities)].sort_values('Price')
    return generate_table(x)

@app.callback(
    Output("plot", "figure"),
    Input("checklist", "value")
)
def update_plot(cities):
    df2 = df[df.Address.isin(cities)].sort_values('Price', ascending=False)
    fig = px.bar(df2, x="Price", y="Sq. Ft", color="Listers")
    return fig



if __name__ == '__main__':
    app.run_server(debug=False)
    