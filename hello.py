from flask import Flask
import os


PORT = 8080
name = os.environ.get('NAME')
app = Flask(__name__)

if name == None or len(name) == 0:
	name = 'world 2'

MESSAGE = f'Hello, {name}!'
print(f'Message: {MESSAGE}')


@app.route('/')
def root():
	result = MESSAGE.encode('utf-8')
	return result


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=PORT)
