# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:45:05 2020

@author: sampa
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)*100
    
    if(output>100):
        return render_template('index.html', prediction_text='Chance of Admission: 100%')
    if(output<0):
        return render_template('index.html', prediction_text='Chance of Admission: 0%')

    return render_template('index.html', prediction_text='Chance of Admission: {}%'.format(output))


if __name__ == "__main__":
    app.run(port=5001,debug=True)