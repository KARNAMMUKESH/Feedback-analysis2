import os
import pickle
from types import ClassMethodDescriptorType
import pandas as pd
from flask import Flask, request, render_template,flash,redirect,session,abort,jsonify
from datetime import datetime
from analytics import write_to_csv_departments
from analytics2 import write_to_csv_departments2
from analytics3 import write_to_csv_departments3
from model import StemmedCountVectorizer
from analytics import get_counts,get_tables,get_titles


app = Flask(__name__, template_folder='template') 

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin-mode.html")

@app.route("/pass")
def pas():
    return render_template("pass.html")

@app.route("/adminwel")
def adwel():
    return render_template("admin-wel.html")

@app.route("/analy")
def analy():
    return render_template("analysis.html")

@app.route("/first")
def stage1():
    return render_template("stagei.html")
    
@app.route("/", methods=['POST'])
def predict():

        program = request.form['program']
        teaching = request.form['teaching']
        enjoy = request.form['enjoy']
        presentation = request.form['presentation']
        job = request.form['job']
        clarity = request.form['clarity']
        recommend = request.form['recommend']
        questions = request.form['questions']
        goal = request.form['goal']
        choice = request.form['choice']
        aware = request.form['aware']
        part = request.form['part']
        
        model = pickle.load(open('SVM classifier.pkl', 'rb'))
        programscore = model.predict(pd.array([program]))
        teachingscore = model.predict(pd.array([teaching]))
        enjoyscore = model.predict(pd.array([enjoy]))
        presentationscore = model.predict(pd.array([presentation]))
        jobscore = model.predict(pd.array([job]))
        clarityscore = model.predict(pd.array([clarity]))
        recommendscore = model.predict(pd.array([recommend]))
        questionscore = model.predict(pd.array([questions]))
        goalscore = model.predict(pd.array([goal]))
        choicescore = model.predict(pd.array([choice]))
        awarescore = model.predict(pd.array([aware]))
        partscore = model.predict(pd.array([part]))
        time = datetime.now().strftime("%m/%d/%Y (%H:%M:%S)")

    

        write_to_csv_departments(time,program,programscore[0],teaching,teachingscore[0],enjoy,enjoyscore[0],
                                    presentation,presentationscore[0],job,jobscore[0],clarity,clarityscore[0],recommend,recommendscore[0],questions,questionscore[0],
                                goal,goalscore[0],choice,choicescore[0],aware,awarescore[0],part,partscore[0])
    
        return render_template('index.html')

@app.route("/second")
def stage2():
    return render_template("stage2.html")

@app.route("/sub", methods=['POST'])
def predict2():

    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
   
    model = pickle.load(open('SVM classifier.pkl', 'rb'))
    q1s = model.predict(pd.array([q1]))
    q2s = model.predict(pd.array([q2]))
    q3s = model.predict(pd.array([q3]))
    q4s = model.predict(pd.array([q4]))
    q5s = model.predict(pd.array([q5]))
    q6s = model.predict(pd.array([q6]))
    q7s = model.predict(pd.array([q7]))
    q8s = model.predict(pd.array([q8]))
    time = datetime.now().strftime("%m/%d/%Y (%H:%M:%S)")

   

    write_to_csv_departments2(time,q1,q1s[0],q2,q2s[0],q3,q3s[0],q4,q4s[0],q5,q5s[0],q6[0],q6s[0],q7,q7s[0],q8,q8s[0])
   
    return render_template('index.html')

@app.route("/third")
def stage3():
    return render_template("stage3.html")

@app.route("/submit", methods=['POST'])
def predict3():

    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
   
    model = pickle.load(open('SVM classifier.pkl', 'rb'))
    q1s = model.predict(pd.array([q1]))
    q2s = model.predict(pd.array([q2]))
    q3s = model.predict(pd.array([q3]))
    q4s = model.predict(pd.array([q4]))
    q5s = model.predict(pd.array([q5]))
    q6s = model.predict(pd.array([q6]))
    q7s = model.predict(pd.array([q7]))
    q8s = model.predict(pd.array([q8]))
    time = datetime.now().strftime("%m/%d/%Y (%H:%M:%S)")

   

    write_to_csv_departments3(time,q1,q1s[0],q2,q2s[0],q3,q3s[0],q4,q4s[0],q5,q5s[0],q6[0],q6s[0],q7,q7s[0],q8,q8s[0])
   
    return render_template('index.html')

app.run(debug=True)
