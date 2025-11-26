import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

N = 5000  # Number of synthetic patients

def random_year():
    return np.random.choice([2020, 2021, 2022, 2023], p=[0.2, 0.3, 0.3, 0.2])

def random_gender():
    return np.random.choice(['Male', 'Female', 'Other'], p=[0.48, 0.5, 0.02])

def random_indigenous():
    return np.random.choice(['Aboriginal', 'Torres Strait Islander', 'Both', 'Neither'], p=[0.03, 0.01, 0.01, 0.95])

def random_remoteness():
    return np.random.choice(['Major City', 'Inner Regional', 'Outer Regional', 'Remote', 'Very Remote'], p=[0.7, 0.15, 0.1, 0.03, 0.02])

def random_diagnosis():
    return np.random.choice(['Hypertension', 'Diabetes', 'Heart Disease', 'Influenza', 'Cancer'])

def random_medication():
    return np.random.choice(['Aspirin', 'Insulin', 'Statins', 'Chemotherapy', 'Antibiotics'])

def random_surgery():
    return np.random.choice(['Appendectomy', 'Knee Replacement', 'Gallbladder Removal', 'Cataract Surgery', 'Angioplasty'])

def random_hospital():
    return np.random.choice(['Royal Melbourne Hospital', 'St Vincent\'s Hospital', 'Royal Brisbane Hospital', 'Fiona Stanley Hospital', 'Royal Adelaide Hospital', 'Children\'s Hospital', 'Healthcare Clinic', 'City Medical Center', 'Regional Hospital', 'General Hospital'])

def random_doctor():
    return np.random.choice(['Dr. Smith', 'Dr. Johnson', 'Dr. Lee', 'Dr. Brown', 'Dr. Wang'])

def random_insurance():
    return np.random.choice(['Private', 'Medicare', 'Medicaid', 'Uninsured'])

def random_lab():
    return round(np.random.normal(100, 20), 2)

def random_xray():
    return np.random.choice(['Normal', 'Abnormal'], p=[0.8, 0.2])

def random_allergy():
    return np.random.choice(['None', 'Peanuts', 'Shellfish', 'Penicillin', 'Latex'])

def random_family_history():
    return np.random.choice(['Diabetes', 'Heart Disease', 'Cancer', 'Alzheimer\'s', 'Hypertension'])

def random_satisfaction():
    return np.random.randint(1, 6)

def random_ai_confidence():
    return round(np.random.uniform(0.7, 1.0), 3)

def random_adverse():
    return np.random.choice([0, 1], p=[0.85, 0.15])

def random_missing(val, prob=0.05):
    return val if np.random.rand() > prob else np.nan

def random_vitals():
    return round(np.random.normal(120, 15), 2)

def random_temp():
    return round(np.random.normal(98.6, 1.2), 2)

def random_duration():
    return np.random.randint(1, 31)

def random_recovery():
    return np.random.randint(1, 10)

def random_social():
    return np.random.choice(['Lives Alone', 'With Family', 'Aged Care', 'Homeless', 'Supported Housing'])

rows = []
for i in range(1, N+1):
    row = {
        'Patient_ID': i,
        'Age': np.random.randint(18, 90),
        'Gender': random_gender(),
        'Blood_Pressure': random_vitals(),
        'Heart_Rate': round(np.random.normal(75, 12), 2),
        'Temperature': random_temp(),
        'Diagnosis': random_diagnosis(),
        'Medication': random_medication(),
        'Treatment_Duration': random_duration(),
        'Insurance_Type': random_insurance(),
        'Doctor_Name': random_doctor(),
        'Hospital_Name': random_hospital(),
        'Lab_Test_Results': random_lab(),
        'X-ray_Results': random_xray(),
        'Surgery_Type': random_surgery(),
        'Recovery_Time': random_recovery(),
        'Allergies': random_allergy(),
        'Family_History': random_family_history(),
        'Patient_Satisfaction': random_satisfaction(),
        'AI_Diagnosis_Confidence': random_ai_confidence(),
        'Indigenous_Status': random_indigenous(),
        'Remoteness_Category': random_remoteness(),
        'Adverse_Outcome': random_adverse(),
        'Year': random_year(),
        'Pathology_Results': random_missing(random_lab(), 0.1),
        'Vital_Signs': random_missing(random_vitals(), 0.1),
        'Social_History': random_missing(random_social(), 0.15)
    }
    rows.append(row)

cols = ['Patient_ID','Age','Gender','Blood_Pressure','Heart_Rate','Temperature','Diagnosis','Medication','Treatment_Duration','Insurance_Type','Doctor_Name','Hospital_Name','Lab_Test_Results','X-ray_Results','Surgery_Type','Recovery_Time','Allergies','Family_History','Patient_Satisfaction','AI_Diagnosis_Confidence','Indigenous_Status','Remoteness_Category','Adverse_Outcome','Year','Pathology_Results','Vital_Signs','Social_History']
df = pd.DataFrame(rows, columns=cols)
df.to_csv('data/AI_in_HealthCare_Dataset.csv', index=False)
print('Synthetic dataset created: data/AI_in_HealthCare_Dataset.csv')
