import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Define a function to load models
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        return pickle.load(model_file)

# Load the models without specifying the encoding
diabetes_model = load_model("C:/Users/DIVYA/Downloads/multiple disease prediction system/saved models-20230622T140541Z-001/saved models/Diabetes_finalmodel.sav")
heart_disease_model = load_model("C:/Users/DIVYA/Downloads/multiple disease prediction system/saved models-20230622T140541Z-001/saved models/heart_disease_model (1).sav")
parkinsons_model = load_model("C:/Users/DIVYA/Downloads/multiple disease prediction system/saved models-20230622T140541Z-001/saved models/parkinsons_model (1).sav")

# Define a function to validate positive numbers
def validate_positive_number(input_string):
    try:
        number = float(input_string)
        return number >= 0
    except ValueError:
        return False

# Main menu function
def main_menu():
    selected = option_menu('Prediction of Chronic diseases using ML Algorithms',
                           ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Disease Prediction"],
                           icons=['house', 'activity', 'heart', 'person'],
                           
                           default_index=0)
    return selected

selected = main_menu()

# Home page
if selected == 'Home':
    st.title('project')
    members = [
        ("Divya Sree", "122010318027"),
        
    ]
    for name, reg_no in members:
        st.write(f"Name: {name}")
        st.write(f"Reg NO: {reg_no}")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    # Input fields
    gender = st.selectbox('Gender', ('0', '1', '2'), placeholder="Select")
    age = st.text_input('Age', '0')
    hypertension = st.selectbox('Hypertension', ('0', '1'), placeholder="Select")
    heart_disease = st.selectbox('Heart Disease', ('0', '1'), placeholder="Select")
    bmivalue = st.text_input('BMI Value')
    hba1clevel = st.text_input('HBA1C Level')
    blood_glucose_level = st.text_input('Blood Glucose Level')

    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[gender, age, hypertension, heart_disease, bmivalue, hba1clevel, blood_glucose_level]])
        diab_diagnosis = 'The person is prone to diabetes' if diab_prediction[0] == 1 else 'The person is not prone to diabetes'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    bmivalue = st.text_input('BMI')
    smoking = st.selectbox('Smoking', ('0', '1'), placeholder="Select")
    alcoholdrinking = st.selectbox('Alcohol Drinking', ('0', '1'), placeholder="Select")
    stroke = st.selectbox('Stroke', ('0', '1'), placeholder="Select")
    physicalhealth = st.text_input('Physical Health')
    mentalhealth = st.text_input('Mental Health')
    diffwalking = st.text_input('Difficulty in Walking')
    sex = st.selectbox('Sex', ('0', '1'), placeholder="Select")
    physicalactivity = st.text_input('Physical Activity')
    genhealth = st.text_input('General Health')
    sleeptime = st.text_input('Sleep Time')

    # Code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[
            float(bmivalue), float(smoking), float(alcoholdrinking), float(stroke),
            float(physicalhealth), float(mentalhealth), float(diffwalking),
            float(sex), float(physicalactivity), float(genhealth), float(sleeptime)
        ]])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinson's Disease Prediction":
    st.title("Parkinson's Disease Prediction")

    # Input fields
    fo = st.text_input('MDVP: Fo (Hz)')
    fhi = st.text_input('MDVP: Fhi (Hz)')
    flo = st.text_input('MDVP: Flo (Hz)')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    dfa = st.text_input('DFA')
    rpde = st.text_input('RPDE')
    spread1 = st.text_input('Spread1')
    spread2 = st.text_input('Spread2')

    # Code for Prediction
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[
            fo, fhi, flo, nhr, hnr, dfa, rpde, spread1, spread2
        ]])
        parkinsons_diagnosis = "The person is prone to Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person is not prone to Parkinson's disease"
    st.success(parkinsons_diagnosis)