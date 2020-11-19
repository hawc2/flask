from flask import Flask, render_template

def create_app(test_config=None):
	app = Flask(__name__)
	
	@app.route('/')
	def index():
	    return render_template('index.html')

	@app.route('/hello')
	def hello():
	    return render_template('hello.html')

	return app
