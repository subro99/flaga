from flask import Flask, render_template, request, session
import os
from moje_programy.gen_data import data
from moje_programy.haslo import generator_hasla
from moje_programy.bohaterowie import bohater
import random
from moje_programy.postac_wiki import description_wiki
from moje_programy.quiz_questions import capitals
from moje_programy.quiz import quiz_generator
from moje_programy.session_data import session_storage

app=Flask(__name__)
app.secret_key = "lodoherbataultrasecretkey"
# app.config.from_object("config.DevelopmentConfig")
app.config.from_object("config.Config")
print(app.config)
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
    # d_quiz_1, correct_answers = quiz_generator(capitals)
    if request.method == "GET":
        d_quiz_1, correct_answers = quiz_generator(capitals)
        session["answers"] = correct_answers
        # session_storage(d_quiz_1, correct_answers)
        return render_template("quiz.html",d_quiz_1=d_quiz_1)
    if request.method == "POST":
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
        session_storage(answers_dict, result)
        # for q,a in odpowiedzi.items():
        #     if q=="answers":
        #         continue
        #     qq.append(q)
        #     aa.append(a)
        return render_template("quiz_wynik.html",result=result,answers=answers)

if __name__=="__main__":
    app.run()