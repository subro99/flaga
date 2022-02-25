from flask import Flask, render_template, request
import os
import random
import string

app=Flask(__name__)

@app.route('/gen_haslo') 
def haslo(): 
    return render_template("gen_haslo.html")

@app.route('/wygen_haslo', methods = ["POST", "GET"])
def genhaslo():
    if request.method == "GET":
        return f"co jest kurwa"
    if request.method == "POST":
        liczba_znakow=int(request.form["liczba_znakow"])
        # liczba_punct=2
        # liczba_dig=2
        # liczba_upper=2
        # liczba_lower=2
        znaki=[2,2,2,2]
        while sum(znaki)<liczba_znakow:
            i=random.randint(0,3)
            znaki[i]+=1
        punct=string.punctuation
        dig=string.digits
        uppercase=string.ascii_uppercase
        lowercase=string.ascii_lowercase
        haslo=random.sample(punct,znaki[0])+random.sample(dig,znaki[1])+random.sample(uppercase,znaki[2])+random.sample(lowercase,znaki[3])
        haslo=random.sample(haslo,len(haslo))
        haslo="".join(haslo)
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
