from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
	result = 'hello world'
	return result
