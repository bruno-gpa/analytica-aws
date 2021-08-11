from flask import Flask


@app.route('/')
def root():
	result = 'hello world'
	return result
