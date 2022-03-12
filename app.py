from flask import Flask, render_template, request
import os
from moje_programy.gen_data import data
from moje_programy.haslo import generator_hasla
from moje_programy.bohaterowie import bohater
import random
app=Flask(__name__)

@app.route('/gen_haslo') 
def haslo(): 
    return render_template("gen_haslo.html")

@app.route('/wygen_haslo', methods = ["POST"])
def genhaslo():
    if request.method == "POST":
        liczba_znakow=int(request.form["liczba_znakow"])
        # gen_data.data(liczba_znakow)
        haslo=generator_hasla(liczba_znakow)
        data(liczba_znakow,haslo)
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

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_ukraina.html")


@app.route('/brudnopis')
def brudnopis():
    hero=bohater("ukasz")
    heroes=["kubus","tygrysek","królik","krzyś"]
    hero=random.choice(heroes).title()
    return render_template("brudnopis.html", hero=hero, heroes=heroes)

if __name__=="__main__":
    app.run()