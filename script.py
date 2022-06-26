#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_list):
    if(len(to_predict_list)!= 12):
        return -1
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Income more than 50K'
        else:
            prediction='Income less that 50K'
            
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
# 	app.run(debug=True)
    # list_for_testing_ValuePredictor_0 = ['50', 2, 14, 0, 4, 0, 2, 1, '2174', '0', '40', 38]
    list_for_testing_ValuePredictor_0 = ['50', 2, 14, 0, 4, 0, 2, 1, '2174', '0', '40', 38]
    print(ValuePredictor(list_for_testing_ValuePredictor_0));
    