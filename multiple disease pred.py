
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_model = pickle.load(open('heart_model.sav','rb'))
parkinson_model = pickle.load(open('parkinson_model.sav','rb'))




with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                        
                          default_index=2)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    
    # page title
    st.title('Diabetes Prediction using ML')

if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")



if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    
    
