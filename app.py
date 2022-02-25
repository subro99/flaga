from flask import Flask, render_template, request
import os
from haslo import generator_hasla

app=Flask(__name__)

@app.route('/gen_haslo') 
def haslo(): 
    return render_template("gen_haslo.html")

@app.route('/wygen_haslo', methods = ["POST"])
def genhaslo():
    if request.method == "POST":
        liczba_znakow=int(request.form["liczba_znakow"])
        haslo=generator_hasla(liczba_znakow)
        return render_template("wygen_haslo.html", genhaslo=haslo)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

@app.route('/xd')
def xd():
    return render_template("xd.html")

if __name__=="__main__":
    app.run()
