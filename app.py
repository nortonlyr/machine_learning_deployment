import flask
import numpy as np
import pickle

app = flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', method=['POST'])
def predict():
    """
    Rendering results on the HTML GUI
    """
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(finale_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text = 'Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.tun(debug=True)