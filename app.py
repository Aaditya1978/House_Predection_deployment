import numpy as np
import pickle
from flask import Flask, render_template,request, jsonify

app = Flask(__name__)
lin_reg = pickle.load(open('lin_reg.pkl', 'rb'))
poly_reg = pickle.load(open('poly_reg.pkl', 'rb'))
pca = pickle.load(open('pca.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features= [int(x) for x in request.form.values()]
    features = [np.array(features)]
    prediction = lin_reg.predict(poly_reg.fit_transform(pca.transform(features)))
    prediction = round(prediction[0], 2)
    prediction = abs(prediction)
    
    return render_template('index.html', text = 'The Predicted Price Of House Is :--- ${}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
