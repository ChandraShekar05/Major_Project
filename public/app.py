from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load the saved model
model = load_model('../model.keras', compile=False)

# Load the datasets
df_creditcard = pd.read_csv('../data/creditcard.csv')
df_filtered_creditcard = pd.read_csv('../data/filtered_creditcard.csv')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/columns', methods=['GET'])
def get_columns():
    # Assuming the columns are the same for both datasets
    columns = df_creditcard.columns.tolist()
    # Exclude the 'Class' column if it exists
    if 'Class' in columns:
        columns.remove('Class')
    return jsonify(columns)

@app.route('/transaction/<dataset>/<int:index>', methods=['GET'])
def get_transaction(dataset, index):
    if dataset == 'creditcard.csv':
        df = df_creditcard
    elif dataset == 'filtered_creditcard.csv':
        df = df_filtered_creditcard
    else:
        return jsonify({'error': 'Invalid dataset'}), 400

    if index < 0 or index >= len(df):
        return jsonify({'error': 'Index out of range'}), 400
    transaction = df.iloc[index].to_dict()
    # Exclude the 'Class' column if it exists
    if 'Class' in transaction:
        del transaction['Class']
    return jsonify(transaction)

@app.route('/statistics/<dataset>', methods=['GET'])
def get_statistics(dataset):
    if dataset == 'creditcard.csv':
        df = df_creditcard
    elif dataset == 'filtered_creditcard.csv':
        df = df_filtered_creditcard
    else:
        return jsonify({'error': 'Invalid dataset'}), 400

    fraudulent = df[df['Class'] == 1].shape[0]
    non_fraudulent = df[df['Class'] == 0].shape[0]
    average_values = df.drop(columns=['Class']).mean().tolist()

    return jsonify({
        'fraudulent': fraudulent,
        'nonFraudulent': non_fraudulent,
        'averageValues': average_values
    })


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Ensure only the required features are included
    input_data = [
        data['Amount'], data['V1'], data['V2'], data['V3'], data['V4'],
        data['V5'], data['V6'], data['V7'], data['V8'], data['V9'], data['V10'],
        data['V11'], data['V12'], data['V13'], data['V14'], data['V15'], data['V16'],
        data['V17'], data['V18'], data['V19'], data['V20'], data['V21'], data['V22'],
        data['V23'], data['V24'], data['V25'], data['V26'], data['V27'], data['V28']
    ]
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    threshold = 2.9
    prediction_class = 'Fraudulent' if prediction[0][0] > threshold else 'Not Fraudulent'
    return jsonify({'prediction': prediction_class})

if __name__ == '__main__':
    app.run(debug=True)