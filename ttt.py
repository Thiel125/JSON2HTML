import urllib2
import urllib
import json
import os
from datetime import datetime
from flask import render_template, Flask,jsonify,make_response, Response
os.environ['no_proxy']='*'

app = Flask(__name__)


def wpjson():
    r = urllib2.urlopen('http://192.168.10.1/test.json')
    data=json.load(r)
    return data

@app.route('/')
def index():
    data = wpjson()
    print data['datum']
    print data['deti']
    print data['cars']
    cisla=data['data']
    cislo1 = int(cisla[0])*10
    cislo2 = int(cisla[1])*10
    cislo3 = int(cisla[2])*10
    data['nasobeni']=cislo1,cislo2,cislo3
    datum = float(data['datum'])
    data['datum'] = datetime.utcfromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S')

    return render_template('index.html',data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
app.run(host='0.0.0.0',port = port)