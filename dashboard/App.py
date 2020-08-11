import joblib
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/hasil', methods=['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        Model = joblib.load('model.sav')
        input = request.form
        age = float(input['age'])
        sex = float(input['sex'])
        cp = float(input['cp'])
        trestbps = float(input['trestbps'])
        chol = float(input['chol'])
        fbs = float(input['fbs'])
        restecg = float(input['restecg'])
        thalach = float(input['thalach'])
        exang = float(input['exang'])
        oldpeak = float(input['oldpeak'])
        slope = float(input['slope'])
        ca = float(input['ca'])
        thal = float(input['thal'])
        pred = Model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])[0]

        return render_template('hasil.html', data = input, prediksi = pred)

@app.route('/data')
def data():
    return render_template('data.html')


if __name__ == "__main__":
    app.run(debug = True, port=5000)