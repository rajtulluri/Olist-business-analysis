"""
The main app file that deploys the server on 127.0.0.1:5000
Renders all layouts and executes callback functions.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import urllib
import json
import base64
import datetime
from dash.dependencies import Input, Output, State
from layout import homepage, columns, column_locs

"""
Server initialization and Stylesheets
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets= external_stylesheets)
server = app.server
app.layout = homepage

"""
Utility functions
"""

def build_packet(features):
	"""
	Builds packet and requests with data passed using assigned URL and API key.

	parameters:
		features: List, input list of data

	returns:
		req: Request object
	"""

	data= {
		"Inputs":{
			"input1":{
				"ColumnNames":[
					"Column 0", "cust_lat", "cust_lng", "seller_lat",
        			"seller_lng", "product_weight_g", "product_length_cm",
        			"product_height_cm", "product_width_cm", "price",
        			"freight_value", "distance", "volume"
				],
				"Values":[features]
			}
		},
		"GlobalParameters":{}
	}
	body = str.encode(json.dumps(data))

	url = open('./Resources/URL','r').read().strip()
	api_key = open('./Resources/API_key','r').read().strip()
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

	req = urllib.request.Request(url, body, headers)

	return req


def post_request(request):
	"""
	Post request created earlier.

	parameters:
		request: Request object

	returns:
		result: result from request
	"""

	try:
		response = urllib.request.urlopen(request)
		result = response.read()
		result = json.loads(result)["Results"]["output1"]["value"]["Values"]
		return round(float(result[0][5]),2)

	except urllib.error.HTTPError as error:
		print("The request failed with status code: " + str(error.code))
		print(error.info())
		print(json.loads(error.read()))
		return json.loads(error.read())


def correct_input(features):
	"""
	Builds entire data row as per the dataset by filling in
	some columns.

	parameter:
		features: List, input list of data

	returns:
		features: List, output list with insertions
	"""

	dummy = [0] * 13
	for col,ftr in zip(columns,features):
		dummy[column_locs[col]] = ftr

	return dummy

"""
Callback functions.
"""

@app.callback(
	Output('output','children'),
	[Input('submit_btn', 'n_clicks')],
	[State('input_{}'.format(col), 'value') for col in columns]

)
def model_prediction(clicks, *features):
	"""
	Requests API for single predictions and reverts with predicted output.

	paramters:
		n_clicks: int, number of clicks on button

		*features: List of arguments, input data from html components
	"""

	features = correct_input([x for x in features])
	request = build_packet(features)

	response = post_request(request)

	return "Freight value  R$ {}".format(response)


if __name__ == '__main__':

	app.title = 'Olist: Freight value'
	app.config.suppress_callback_exceptions = True
	app.run_server(debug= False, host= '127.0.0.1', port= 5000)

