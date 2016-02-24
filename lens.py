from flask import Flask
from flask import request
from flask import render_template

from pygments import highlight
from pygments.lexers import Python3Lexer, PhpLexer
from pygments.formatters import HtmlFormatter

import urllib.parse
import urllib.request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(formatted=None):
    if request.method == 'POST':
        code = request.form['code']
        lexer = Python3Lexer(stripall=True)
        if request.form['lexer'] == 'PHP':
            lexer = PhpLexer()
        formatter = HtmlFormatter(
            linenos=True, style='xcode', cssclass="highlight", full=True)
        formatted = highlight(code, lexer, formatter)
        return render_template('pygments.html', formatted=formatted)

    return render_template('index.html')


@app.route('/search')
def search():
    baseurl = 'https://maps.googleapis.com/maps/api/geocode/json?language=ru&'
    url = baseurl + \
        urllib.parse.urlencode({'address': request.args.get('address')})
    urlhandler = urllib.request.urlopen(url)
    response = urlhandler.read()
    geojson = json.loads(response.decode('utf-8'))
    return render_template('geo.html', geodata=geojson)

if __name__ == '__main__':
    app.run(debug=True)
