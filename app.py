import flask
import numpy as np
import pickle

app = flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')