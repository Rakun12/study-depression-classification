import pickle
from flask import Flask, request, jsonify

model_file = 'dv n model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('study depression')

@app.route('/predict', methods=['POST'])
def predict():
    user = request.get_json()

    X = dv.transform([user])
    y_pred = (model.predict_proba(X)).round(3)
    depression = model.predict(X)

    result = {
        'depression_probability [0]': float(y_pred[0][0]),
        'depression_probability [1]': float(y_pred[0][1]),
        'depression': int(depression)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1212)
