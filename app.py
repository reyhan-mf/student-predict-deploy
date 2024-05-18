import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
rf_model = joblib.load('rf_model2.joblib')

# Function to make predictions
def predict_status(input_data):
    input_df = pd.DataFrame([input_data])
    input_X = input_df.drop('Status', axis=1, errors='ignore')
    prediction = rf_model.predict(input_X)
    return prediction[0]

# Streamlit app
def app():
    st.title("Status Prediction")

    # Input form
    marital_status = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced', 'Widowed'])
    course = st.selectbox("Course", [
        "Biofuel Production Technologies",
        "Animation and Multimedia Design",
        "Social Service (evening attendance)",
        "Agronomy",
        "Communication Design",
        "Veterinary Nursing",
        "Informatics Engineering",
        "Equinculture",
        "Management",
        "Social Service",
        "Tourism",
        "Nursing",
        "Oral Hygiene",
        "Advertising and Marketing Management",
        "Journalism and Communication",
        "Basic Education",
        "Management (evening attendance)"
    ])
    attendance = st.selectbox("Daytime/Evening Attendance", ['Daytime', 'Evening'])
    prev_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, step=1.0)
    nationality = st.selectbox("Nationality", [
        "Portuguese",
        "German",
        "Spanish",
        "Italian",
        "Dutch",
        "English",
        "Lithuanian",
        "Angolan",
        "Cape Verdean",
        "Guinean",
        "Mozambican",
        "Santomean",
        "Turkish",
        "Brazilian",
        "Romanian",
        "Moldova (Republic of)",
        "Mexican",
        "Ukrainian",
        "Russian",
        "Cuban",
        "Colombian"
    ])
    father_qualification = st.selectbox("Father's Qualification", [
        "Can't read or write",
        "Can read without having a 4th year of schooling",
        "Basic Education 1st Cycle (4th/5th year) or Equiv.",
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        "7th Year (Old)",
        "7th year of schooling",
        "8th year of schooling",
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        "9th Year of Schooling - Not Completed",
        "10th Year of Schooling",
        "11th Year of Schooling - Not Completed",
        "12th Year of Schooling - Not Completed",
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Other - 11th Year of Schooling",
        "2nd year complementary high school course",
        "Complementary High School Course",
        "Complementary High School Course - not concluded",
        "2nd cycle of the general high school course",
        "General commerce course",
        "General Course of Administration and Commerce",
        "Supplementary Accounting and Administration",
        "Technical-professional course",
        "Technological specialization course",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher education - degree (1st cycle)",
        "Specialized higher studies course",
        "Professional higher technical course",
        "Higher Education - Master's",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate",
        "Higher Education - Doctorate (3rd cycle)",
        "Frequency of Higher Education",
        "Unknown"
    ])

    mother_qualification = st.selectbox("Mother's Qualification", [
        "Can't read or write",
        "Can read without having a 4th year of schooling",
        "Basic Education 1st Cycle (4th/5th year) or Equiv.",
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        "7th Year (Old)",
        "7th year of schooling",
        "8th year of schooling",
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        "9th Year of Schooling - Not Completed",
        "10th Year of Schooling",
        "11th Year of Schooling - Not Completed",
        "12th Year of Schooling - Not Completed",
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Other - 11th Year of Schooling",
        "2nd year complementary high school course",
        "Complementary High School Course",
        "Complementary High School Course - not concluded",
        "2nd cycle of the general high school course",
        "General commerce course",
        "General Course of Administration and Commerce",
        "Supplementary Accounting and Administration",
        "Technical-professional course",
        "Technological specialization course",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher education - degree (1st cycle)",
        "Specialized higher studies course",
        "Professional higher technical course",
        "Higher Education - Master's",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate",
        "Higher Education - Doctorate (3rd cycle)",
        "Frequency of Higher Education",
        "Unknown"
    ])
    admission_grade = st.number_input("Admission Grade", min_value=0.0, step=1.0)
    displaced = st.selectbox("Displaced", ['Yes', 'No'])
    debtor = st.selectbox("Debtor", ['Yes', 'No'])
    tuition_fees_up_to_date = st.selectbox("Tuition Fees Up-to-date", ['Yes', 'No'])
    gender = st.selectbox("Gender", ['Male', 'Female'])

    col1, col2, col3 = st.columns(3)
    with col1:
        curricular_units_1st_sem_enrolled = st.number_input("1st Sem Enrolled", min_value=0, step=1)
    with col2:
        curricular_units_1st_sem_evaluations = st.number_input("1st Sem Evaluations", min_value=0, step=1)
    with col3:
        curricular_units_1st_sem_grade = st.number_input("1st Sem Grade", min_value=0.0, step=0.1)

    col4, col5, col6 = st.columns(3)
    with col4:
        curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled", min_value=0, step=1)
    with col5:
        curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Evaluations", min_value=0, step=1)
    with col6:
        curricular_units_2nd_sem_grade = st.number_input("2nd Sem Grade", min_value=0.0, step=0.1)

    input_data = {
        'Marital_status': marital_status,
        'Course': course,
        'Daytime_evening_attendance': attendance,
        'Previous_qualification_grade': prev_qualification_grade,
        'Nacionality': nationality,
        "Mothers_qualification": mother_qualification,
        "Fathers_qualification": father_qualification,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade
    }

    # Make prediction
    if st.button("Predict Status"):
        predicted_status = predict_status(input_data)
        if predicted_status == 0:
            status_text = "Dropout"
        elif predicted_status == 1:
            status_text = "Enrolled"
        else:
            status_text = "Graduate"
        st.write(f"Predicted Status: {status_text}")

if __name__ == "__main__":
    app()
