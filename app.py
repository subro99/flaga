from flask import Flask, render_template, request, session, redirect, url_for
import os
from moje_programy.gen_data import data
from moje_programy.haslo import generator_hasla
from moje_programy.bohaterowie import bohater
import random
from moje_programy.postac_wiki import description_wiki
from moje_programy.quiz_questions import capitals
from moje_programy.quiz_questions import english
from moje_programy.quiz import quiz_generator
from moje_programy.session_data import session_storage
import datetime

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import wtforms.validators
app=Flask(__name__)
app.secret_key = "lodoherbataultrasecretkey"
# app.config.from_object("config.DevelopmentConfig")
# app.config.from_object("config.Config")
@app.route('/gen_haslo', methods = ["GET","POST"])
def genhaslo():
    if request.method == "GET":
        return render_template("gen_haslo.html")
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
    heroes=["Kopernik","Tusk","Bruce Lee","Barack Obama"]
    hero=description_wiki(random.choice(heroes))
    return render_template("brudnopis.html", hero=hero, heroes=heroes)

@app.route('/ciekawe-postacie')
def int_characters():
    c_characters=["Kopernik","Trump","Bruce Lee","Barack Obama", "Batman", "Joker"]
    characters=random.sample(c_characters,4)
    int_characters=[]
    for character in characters:
        description=description_wiki(character)
        words=description.split()
        int_characters.append([character,description,len(words)])
    int_characters.sort(reverse=True,key=lambda x:x[2])
    return render_template("ciekawe_postacie.html",int_characters=int_characters)


@app.route('/quiz', methods = ["GET","POST"])
def quiz():
    if request.method == "GET":
        my_date1 = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        d_quiz_1, correct_answers = quiz_generator(capitals)
        session["answers"] = correct_answers
        session["stime"]=str(my_date1) #dlaczego bez str() jest +00:00 na koncu? oto jest pytanie
        # session_storage(d_quiz_1, correct_answers)
        return render_template("quiz.html",d_quiz_1=d_quiz_1)
    if request.method == "POST":
        my_date2 = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        session["ftime"]=str(my_date2)
        result=0

        odpowiedzi=session["answers"]
        answers=request.form
        answers_dict=answers.to_dict()
        # print(answers_dict)
        # qq=[]
        # aa=[]
        # cc=[]
        for question, user_answer in answers.items():
            # print(question, user_answer)
            if odpowiedzi.get(question)==user_answer:
                result+=1
        session_storage(answers_dict, result,session["stime"],session["ftime"])
        # for q,a in odpowiedzi.items():
        #     if q=="answers":
        #         continue
        #     qq.append(q)
        #     aa.append(a)
        return render_template("quiz_wynik.html",result=result,answers=answers)


def save_data(string):
    
    if not 'dane' in os.listdir():
        os.mkdir('dane')
        if not 'notatnik.txt' in os.listdir('dane'):
             os.system('touch notatnik.txt')
            
    with open('dane/notatnik.txt', "a+") as f:
        f.write(string)

@app.route('/form_b', methods = ["GET","POST"])
def form_b():
    form = music_form()
    feedback=""
    # if request.method == 'POST':
    #     return redirect(url_for('form_result'))
    if form.validate_on_submit():
        message=form.mess_box.data
        music_type=form.music_type.data
        # session["message"]=message
        string = '{} - {}\n'.format(music_type, message)
        save_data(string)
        return redirect( url_for('form_result',music_type=music_type))
  
    return render_template("form_b.html",form=form)

@app.route('/form_result')
def form_result():
    # message=session["message"]
    music_type=request.args["music_type"]
    return render_template("form_result.html", music_type=music_type)


@app.route('/result')
def res():
    return render_template("session_result.html",s=session.items())

    
class music_form(FlaskForm):
    m_types=[
        ("Rock", "Rock"),
        ("POP", "POP"),
        ("Heavy metal", "Heavy metal"),
        ("Hip hop", "Hip hop"),
        ("Disco", "Disco")
    ]

    mess_box = StringField('Link do muzyki: ', validators=[wtforms.validators.URL(message="Niepoprawny link!")])
    # mess_box = StringField('Link do muzyki: ', validators=[DataRequired(message="wrong")])
    music_type= SelectField(label="Typ muzyki", choices=m_types)
    button = SubmitField('Wyślij')

if __name__=="__main__":
    app.run()