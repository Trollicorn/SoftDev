#Mohammed Uddin
#SoftDev1 pd6
#K26 -- Getting More REST
#2018-11-15

import json
from urllib import request,parse

from flask import Flask, render_template


app = Flask(__name__)

api0 = "https://www.alphavantage.co/query?"
stuff0 = "function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD"
apikey0 = "&apikey=22RF5B4FAHT5XUQH"
url1 = "https://xkcd.com/42/info.0.json" #remove comic number for current

@app.route("/")
def show():
    #cancer
    url0 = api0 + stuff0 + apikey0
    book = request.urlopen(url0)
    stuff = book.read()
    things0 = json.loads(stuff)
    ugly = things0['Realtime Currency Exchange Rate']
    fr=ugly['1. From_Currency Code']
    frm=ugly['2. From_Currency Name']
    t=ugly['3. To_Currency Code']
    to=ugly['4. To_Currency Name']
    rate=ugly['5. Exchange Rate']
    time=ugly['6. Last Refreshed']
    zone=ugly['7. Time Zone']

    #fun
    book = request.urlopen(url1)
    stuff = book.read()
    things1= json.loads(stuff)
    num = things1['num']
    title = things1['title']
    img = things1['img']
    alt = things1['alt']

    return render_template("demo.html",frm=frm,fr=fr,to=to,t=t,rate=rate,time=time,zone=zone,
                            num=num,title=title,img=img,alt=alt)


if __name__== "__main__":
    app.debug = True
    app.run()
