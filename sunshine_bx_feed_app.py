import streamlit as st
import pandas as pd
import joblib
import sklearn
# load the models and scaler saved 
model=joblib.load('regression_model2.pkl')
#App title
st.title('☀Broiler feed quantity estimator app🐥')
st.write('Enter the feautures of the flock to estimate feed')
# input the feautures value
Age_in_days=st.number_input(
    'Input the age of broilers in days',
    min_value=2, max_value=36, step=1)
Body_weight_g=st.number_input(
    'Input Average weight of chicken or flock in (g)',
    min_value=79, max_value=2500, step=1)
#predict quantity of feed intake
if st.button('predict feed quantity per bird(g)'):
    #input data
    input_data=pd.DataFrame({
        'Age in days':[Age_in_days],
        'Body weight':[Body_weight_g]})
    #predictio
    prediction=model.predict(input_data)
    #display prediction
    st.success(f'Predicted feed quantity quantity(g) is:{prediction[0]:.2f}')

