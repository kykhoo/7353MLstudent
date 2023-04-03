from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        studentgender = request.form['Gender']
        studentiq = request.form['IQ']
        studentparentincome = request.form['ParentIncome']
        studentparentencouragement = request.form['ParentEncouragement']

        if str(studentgender) =='' or str(studentiq) =='' or str(studentparentincome) =='' or str(studentparentencouragement) =='':
            return render_template('index.html', href2='Please insert student information.')
        else:
            model = load('app/pre.joblib')
            np_arr = np.array([studentgender, studentiq, studentparentincome, studentparentencouragement])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            #return predictions_to_str
            return render_template('index.html', href2='The probability of this student (gender:'+str(studentgender)+', IQ:'+str(studentiq)+', parentincome:'+str(studentparentincome)+', parentencouragement:'+str(studentparentencouragement)+') going to university is: '+predictions_to_str())


