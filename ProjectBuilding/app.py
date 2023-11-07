import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('fraud.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def home1():
    return render_template('predict.html')


@app.route('/pred', methods=['POST', 'GET'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        return render_template('predict.html',
                            prediction_text='Low chances of transaction being fraud'.format(
                                prediction),
                                )
    else:
        return render_template('predict.html',
                            prediction_text='High chances of transaction being fraud'.format(
                                prediction),
                                )


