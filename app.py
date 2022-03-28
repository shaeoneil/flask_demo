from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

@app.route('/mike')
def mike():
    return render_template('mike.html', pageTitle='About Mike')

@app.route('/shae')
def shae():
    return render_template('shae.html', pageTitle='About Shae')

if __name__ == '__main__':
    app.run(debug=True)
