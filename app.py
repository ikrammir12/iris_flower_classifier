import streamlit as st 
import requests

API_URL='http://127.0.0.1:8000/prediction'

st.title("Iris Flower Predictor")
st.markdown("Enter the flower samples below")

sepal_length = st.number_input('Sepal_length',min_value=0.1,max_value=10.0,value=4.0)
sepal_width =st.number_input('sepal_width',min_value=0.1,max_value=10.1,value=5.0)
petal_length = st.number_input('Petal_legth',max_value=10.1,min_value=0.1,value=5.0)
petal_width = st.number_input('petal_width',max_value=10.1,min_value=0.1,value=4.0)

if st.button('predict Flower class'):
    input_data ={
        'sepal_length':sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code==200:
            predicition =response.json()
            st.success(f"prediction: {predicition['Predicted Class']}")

        else:
            st.error(f"Error: {response.status_code}-{response.txt}") 


    except Exception as e:
        st.error(f'An error occcurred:{e}')                     