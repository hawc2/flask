from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return 'Index Page'

@app.route('/sf/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/hello/')
def hello_world():
    return 'Hello, World!'

app.run()
