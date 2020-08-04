"""
Layout file for the server.
Contains HTML for rendering.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

column_labels = {"product_weight_g":'Weight (in gms)',"price":'Price (in R$)',"distance":'Distance (in kms)', "volume":'Volume (in cm3)'}
column_locs = {"product_weight_g":5,"price":9,"distance":11, "volume":12}
columns = ['product_weight_g','price','distance','volume']
types = ['number'] * 4

homepage= html.Div(children= [
	html.Br(),

	html.Div(children= [
		html.Center(children= [
			html.Div(children= [
					html.H3('OLIST'),
					html.H6('Freight value calculator')
			]),

			html.Div(children= [
				html.Div(children= [
					html.Br(),
					html.P(column_labels[col]),
					dcc.Input(
						id= 'input_{}'.format(col),
						type= typ
					),
				])
				for typ,col in zip(types,columns)
			]),

			html.Br(),
			html.Br(),

			html.Button(
				'Submit', 
				id= 'submit_btn',
				 n_clicks= 0
			),

			html.Br(),
			html.Br(),

			html.Div(
				html.H5(id= 'output', style= {
					'border':'thin lightgrey solid',
					 'width':'70%',
					 'border-radius':'50px',
					 'background-color': 'rgb(153, 187, 255)',
					 })
			),

			html.Br()
		])
	],style= {
			'width':'35%',
			'border':'thin lightgrey solid',
			'border-radius':'50px',
			'margin-left':'25px',
			'box-shadow': '2px 2px 2px lightgrey',
			'background-color': 'rgb(230, 230, 255)'
		}
	)
], style={
	'background-image': 'url("https://www.ecomcrew.com/wp-content/uploads/2019/06/hero-sea-freight.png")',
	'height':'120vh'
})