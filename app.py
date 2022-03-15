from audioop import reverse
from flask import Flask, render_template, request
import os
from moje_programy.gen_data import data
from moje_programy.haslo import generator_hasla
from moje_programy.bohaterowie import bohater
import random
from moje_programy.postac_wiki import description_wiki, sort_description

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


@app.route('/brudndescription')
def brudndescription():
    hero=bohater("ukasz")
    heroes=["Kopernik","Tusk","Bruce Lee","Barack Obama"]
    hero=description_wiki(random.choice(heroes))
    return render_template("brudndescription.html", hero=hero, heroes=heroes)

@app.route('/ciekawe-postacie')
def int_characters():
    c_characters=["Kopernik","Trump","Bruce Lee","Barack Obama", "Batman", "Joker"]
    characters=random.sample(c_characters,4)
    int_characters=[]
    for character in characters:
        description=description_wiki(character)
        words=description.split()
        counter=0
        for word in words:
            counter+=1
        int_characters.append([character,description,counter])
    int_characters.sort(reverse=True,key=sort_description)
    return render_template("ciekawe_postacie.html",int_characters=int_characters)

if __name__=="__main__":
    app.run()