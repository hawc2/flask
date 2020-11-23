from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components
import requests

api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json'
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)

plot = figure(tools='pan,wheel_zoom,box_zoom,save,reset,help',
			  title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

script, div = components(plot)

def create_app(test_config=None):
	app = Flask(__name__)

	@app.route('/')
	def index():
	    return render_template('index.html')

	@app.route('/hello')
	def hello():
	    return render_template('hello.html')

	@app.route('/graph')
	def graph():
		return render_template('graph.html', script=script, div=div)

	return app
