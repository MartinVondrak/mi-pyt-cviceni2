from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'MI-PYT je nejlepsi! A MARTA TAKY!!!'


@app.route('/hello')
@app.route('/hello/<user>')
def hello(user=None):
    return render_template('hello.html', name=user)


@app.route('/date_example')
def date_example():
    return render_template(
        'date_example.html',
        created_at='Tue Mar 21 15:50:59 +0000 2017',
    )


@app.template_filter('time')
def convert_time(text):
    dt = datetime.strptime(text, '%a %b %d %H:%M:%S %z %Y')
    return dt.strftime('%c')
