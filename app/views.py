from app import app
from flask import request
from flask import render_template

from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

import urllib.parse
import urllib.request
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/codehighlighter', methods=['GET', 'POST'])
def highlite(formatted=None):
    lexers_all = sorted(get_all_lexers(), key=lambda lexer: lexer[0])
    if request.method == 'POST':
        code, lexer = request.form['code'], request.form['lexer']
        lexer = get_lexer_by_name(lexer.strip())
        formatter = HtmlFormatter(
            linenos=True, style='xcode', cssclass="highlight", full=True)
        formatted = highlight(code, lexer, formatter)
        return render_template('highlighter.html', formatted=formatted, lexers=lexers_all)

    return render_template('highlighter.html', lexers=lexers_all)


@app.route('/geosearch', methods=['GET', 'POST'])
def geosearch():
    if request.method == 'POST':
        baseurl = 'https://maps.googleapis.com/maps/api/geocode/json?language=ru&'
        url = baseurl + \
            urllib.parse.urlencode({'address': request.form['address']})
        urlhandler = urllib.request.urlopen(url)
        response = urlhandler.read()
        geojson = json.loads(response.decode('utf-8'))
        return render_template('geo.html', geodata=geojson)
    return render_template('geo.html', geodata='[]')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')
