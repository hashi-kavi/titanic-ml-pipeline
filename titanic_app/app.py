import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


#load the saved pipeline

MODEL_PATH = Path(__file__).resolve().parent / 'models' / 'titanic_rf_model.pkl'
model = joblib.load(MODEL_PATH)

#set up the UI
st.title("Titanic Survival Predictor")
st.write("Enter passenger details to see if they would have survived.")

# create inputs
col1,col2 = st.columns(2)

with col1:
    pclass = st.selectbox('Ticket Class',[1,2,3])
    sex = st.selectbox('Sex',["male","female"])
    age = st.slider("Age",0,80,25)
    sibsp = st.number_input("Siblings/Spouses",0,8,0)
    parch = st.number_input("Parents/Children",0,6,0)

with col2:
    fare = st.number_input("Fare Paid", value=32.0)
    embarked = st.selectbox("Port of Embarkation",["S","C","Q"])

#predict button 
if st.button("Predict Survival"):
    # calculate features
    
    family_size = sibsp + parch + 1
    IsAlone = 1 if family_size == 1 else 0
    sex_encoded = 0 if sex == "male" else 1
    Embarked_Q =1 if embarked == "Q" else 0
    Embarked_S = 1 if embarked == "S" else 0

    #create a dataframe for the model
    input_data = pd.DataFrame(
        [[pclass, sex_encoded, age, fare, family_size, IsAlone,Embarked_Q,Embarked_S]], 
                              columns=['Pclass' ,'Sex', 'Age', 'Fare', 'FamilySize', 'IsAlone', 'Embarked_Q','Embarked_S'])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    #get the probability of died and survived  probs of a one passanger,so from that get the survided prob [[0.18, 0.82]] then by calling this only gives second number"""
    st.progress(probability)

    if prediction[0] == 1:
        st.success(f"Survived ! (Probability:{probability:.2%})")
    else:
        st.error(f"Perished. (Probability:{1-probability:.2%})")
    if probability> 0.5:
        st.write("The model is leaning towards survival.")
    else:
        st.write("The model is leaning towards fatality.")