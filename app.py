import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

# Load the saved model
model = load_model('model.keras', compile=False)

# Load the datasets
df_creditcard = pd.read_csv('./data/creditcard.csv')
df_filtered_creditcard = pd.read_csv('./data/filtered_creditcard.csv')

# Streamlit application
st.title('Credit Card Fraud Detection')

# Dropdown menu to select the dataset
dataset_option = st.selectbox('Select dataset', ('creditcard.csv', 'filtered_creditcard.csv'))

# Load the selected dataset
if dataset_option == 'creditcard.csv':
    df = df_creditcard
else:
    df = df_filtered_creditcard

# Number input to select a sample index
sample_index = st.number_input('Select sample index', min_value=0, max_value=len(df)-1, value=0)
sample_input = df.iloc[sample_index]

# Display the sample input
# st.write('Sample Input:', sample_input)

# Input fields for user to enter data
input_data = []
input_data.append(st.number_input('Enter transaction time', value=sample_input['Time']))
input_data.append(st.number_input('Enter transaction amount', value=sample_input['Amount']))
input_data.append(st.number_input('Enter V1', value=sample_input['V1']))
input_data.append(st.number_input('Enter V2', value=sample_input['V2']))
input_data.append(st.number_input('Enter V3', value=sample_input['V3']))
input_data.append(st.number_input('Enter V4', value=sample_input['V4']))
input_data.append(st.number_input('Enter V5', value=sample_input['V5']))
input_data.append(st.number_input('Enter V6', value=sample_input['V6']))
input_data.append(st.number_input('Enter V7', value=sample_input['V7']))
input_data.append(st.number_input('Enter V8', value=sample_input['V8']))
input_data.append(st.number_input('Enter V9', value=sample_input['V9']))
input_data.append(st.number_input('Enter V10', value=sample_input['V10']))
input_data.append(st.number_input('Enter V11', value=sample_input['V11']))
input_data.append(st.number_input('Enter V12', value=sample_input['V12']))
input_data.append(st.number_input('Enter V13', value=sample_input['V13']))
input_data.append(st.number_input('Enter V14', value=sample_input['V14']))
input_data.append(st.number_input('Enter V15', value=sample_input['V15']))
input_data.append(st.number_input('Enter V16', value=sample_input['V16']))
input_data.append(st.number_input('Enter V17', value=sample_input['V17']))
input_data.append(st.number_input('Enter V18', value=sample_input['V18']))
input_data.append(st.number_input('Enter V19', value=sample_input['V19']))
input_data.append(st.number_input('Enter V20', value=sample_input['V20']))
input_data.append(st.number_input('Enter V21', value=sample_input['V21']))
input_data.append(st.number_input('Enter V22', value=sample_input['V22']))
input_data.append(st.number_input('Enter V23', value=sample_input['V23']))
input_data.append(st.number_input('Enter V24', value=sample_input['V24']))
input_data.append(st.number_input('Enter V25', value=sample_input['V25']))
input_data.append(st.number_input('Enter V26', value=sample_input['V26']))
input_data.append(st.number_input('Enter V27', value=sample_input['V27']))

# Define a function to make predictions
def predict(input_data):
    input_data = np.array(input_data).reshape(1, -1)  # Reshape input data as needed
    prediction = model.predict(input_data)
    return prediction

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_data)
    st.write('Prediction:', prediction)
    
    # Assuming the model output is a probability score
    threshold = 2.9
    if prediction[0][0] > threshold:
        st.write('Class: Fraudulent')
    else:
        st.write('Class: Not Fraudulent')