from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('diabetes-prediction-rfc-model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            int(request.form['pregnancies']),
            int(request.form['glucose']),
            int(request.form['bloodpressure']),
            int(request.form['skinthickness']),
            int(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            int(request.form['age'])
        ]
        data = np.array([features])
        prediction = model.predict(data)
        result = 'Positive (Diabetic)' if prediction[0] == 1 else 'Negative (Not Diabetic)'
        return render_template('result.html', prediction=result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
