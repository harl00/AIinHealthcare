"""
Synthetic Healthcare Dataset Generator for AI in Healthcare Curriculum
Generates realistic Australian hospital data suitable for ML training exercises

Focus areas:
- Deterioration prediction (24-hour outcomes)
- Aeromedical transport suitability
- Australian healthcare context (remoteness, Indigenous health, insurance types)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

class HealthcareDatasetGenerator:
    def __init__(self, n_records=5000):
        self.n_records = n_records
        self.australian_hospitals = [
            'Royal Brisbane Hospital', 'Royal Melbourne Hospital', 
            'Royal Adelaide Hospital', 'Royal Perth Hospital',
            'Fiona Stanley Hospital', 'Royal Children\'s Hospital',
            'St Vincent\'s Hospital', 'Alfred Hospital', 'Prince Charles Hospital',
            'Lady Cilento Children\'s Hospital', 'Princess Alexandra Hospital',
            'Regional Hospital', 'City Medical Center', 'Healthcare Clinic',
            'District Hospital', 'Community Health Centre'
        ]
        
        self.doctors = [
            'Dr. Johnson', 'Dr. Smith', 'Dr. Brown', 'Dr. Lee', 'Dr. Wang',
            'Dr. Williams', 'Dr. Jones', 'Dr. Garcia', 'Dr. Miller', 'Dr. Davis',
            'Dr. Rodriguez', 'Dr. Martinez', 'Dr. Patel', 'Dr. Kumar', 'Dr. Chen'
        ]
        
        self.diagnoses = [
            'Heart Disease', 'Hypertension', 'Diabetes', 'Influenza',
            'Pneumonia', 'Cancer', 'Asthma', 'COPD', 'Sepsis', 'Stroke',
            'Acute Coronary Syndrome', 'Pulmonary Embolism', 'Renal Failure',
            'Acute Pancreatitis', 'Gastrointestinal Bleed'
        ]
        
        self.medications = [
            'Aspirin', 'Statins', 'Antibiotics', 'Insulin', 'Chemotherapy',
            'ACE Inhibitors', 'Beta Blockers', 'Diuretics', 'Anticoagulants',
            'Corticosteroids', 'Bronchodilators', 'NSAIDs'
        ]
        
        self.surgeries = [
            'Angioplasty', 'Bypass Surgery', 'Appendectomy', 'Gallbladder Removal',
            'Knee Replacement', 'Hip Replacement', 'Cataract Surgery',
            'Hernia Repair', 'Emergency Laparotomy', 'Craniotomy',
            'None', 'None', 'None'  # Most patients don't have surgery
        ]
        
        self.allergies = [
            'None', 'Penicillin', 'Sulfonamides', 'Cephalosporins',
            'NSAIDs', 'ACE Inhibitors', 'Latex', 'Peanuts', 'Shellfish',
            'Aspirin', 'Codeine'
        ]
        
        self.family_history = [
            'None', 'Heart Disease', 'Hypertension', 'Diabetes',
            'Cancer', 'Stroke', 'Alzheimer\'s', 'Mental Illness'
        ]
        
        self.insurance_types = [
            'Medicare', 'Private', 'Uninsured', 'Medicaid', 'Workers Comp'
        ]
        
        self.remoteness = [
            'Major City', 'Inner Regional', 'Outer Regional',
            'Remote', 'Very Remote'
        ]
        
        self.indigenous_status = [
            'Neither', 'Aboriginal', 'Torres Strait Islander', 'Both'
        ]
        
        self.social_history = [
            '', 'Lives Alone', 'With Family', 'Aged Care', 'Supported Housing', 'Homeless'
        ]

    def _generate_vital_signs(self, age, diagnosis):
        """Generate realistic vital signs based on age and diagnosis"""
        
        # Base values by age
        base_hr = 70 + (age - 50) * 0.2 + np.random.normal(0, 5)
        base_sbp = 120 + (age - 50) * 0.4 + np.random.normal(0, 8)
        base_dbp = 75 + (age - 50) * 0.15 + np.random.normal(0, 5)
        base_temp = 37.0 + np.random.normal(0, 0.3)
        base_rr = 16 + np.random.normal(0, 2)
        base_spo2 = 96 + np.random.normal(0, 2)
        
        # Adjustments by diagnosis
        diagnosis_adjustments = {
            'Heart Disease': {'hr': 15, 'sbp': -10, 'rr': 2},
            'Hypertension': {'sbp': 20, 'dbp': 12},
            'Pneumonia': {'rr': 6, 'temp': 1.5, 'spo2': -5},
            'Sepsis': {'hr': 20, 'rr': 8, 'temp': 2.0, 'spo2': -8},
            'COPD': {'rr': 4, 'spo2': -8},
            'Acute Coronary Syndrome': {'hr': 12, 'sbp': -15},
            'Pulmonary Embolism': {'hr': 18, 'rr': 6, 'spo2': -10},
        }
        
        adj = diagnosis_adjustments.get(diagnosis, {})
        base_hr += adj.get('hr', 0)
        base_sbp += adj.get('sbp', 0)
        base_dbp += adj.get('dbp', 0)
        base_temp += adj.get('temp', 0)
        base_rr += adj.get('rr', 0)
        base_spo2 += adj.get('spo2', 0)
        
        return {
            'heart_rate': max(40, min(180, base_hr)),
            'systolic_bp': max(70, min(200, base_sbp)),
            'diastolic_bp': max(40, min(120, base_dbp)),
            'temperature': max(35.0, min(40.0, base_temp)),
            'respiratory_rate': max(8, min(40, base_rr)),
            'oxygen_saturation': max(80, min(100, base_spo2))
        }

    def _calculate_deterioration_risk(self, vitals, age, diagnosis):
        """Calculate whether patient will deteriorate in 24 hours"""
        
        # Risk scoring based on vitals
        risk_score = 0
        
        # Heart rate risk
        if vitals['heart_rate'] > 120:
            risk_score += 3
        elif vitals['heart_rate'] > 100:
            risk_score += 1
        elif vitals['heart_rate'] < 50:
            risk_score += 2
            
        # Respiratory rate risk
        if vitals['respiratory_rate'] > 25:
            risk_score += 3
        elif vitals['respiratory_rate'] > 20:
            risk_score += 1
        elif vitals['respiratory_rate'] < 10:
            risk_score += 2
            
        # Blood pressure risk
        if vitals['systolic_bp'] < 90:
            risk_score += 4
        elif vitals['systolic_bp'] < 100:
            risk_score += 2
        elif vitals['systolic_bp'] > 180:
            risk_score += 1
            
        # Oxygen saturation risk
        if vitals['oxygen_saturation'] < 90:
            risk_score += 4
        elif vitals['oxygen_saturation'] < 94:
            risk_score += 2
            
        # Temperature risk
        if vitals['temperature'] > 38.5:
            risk_score += 2
        elif vitals['temperature'] < 36.0:
            risk_score += 2
            
        # Age risk
        if age > 75:
            risk_score += 2
        elif age > 85:
            risk_score += 1
            
        # Diagnosis-specific high-risk conditions
        high_risk_diagnoses = ['Sepsis', 'Acute Coronary Syndrome', 
                               'Pulmonary Embolism', 'Stroke']
        if diagnosis in high_risk_diagnoses:
            risk_score += 3
            
        # Add some randomness (clinical unpredictability)
        risk_score += np.random.normal(0, 1)
        
        # Threshold for deterioration
        return 1 if risk_score > 5 else 0

    def generate(self):
        """Generate the complete synthetic dataset"""
        
        data = {
            'Patient_ID': [],
            'Age': [],
            'Gender': [],
            'Blood_Pressure': [],
            'Heart_Rate': [],
            'Temperature': [],
            'Respiratory_Rate': [],
            'Oxygen_Saturation': [],
            'Diagnosis': [],
            'Medication': [],
            'Treatment_Duration': [],
            'Insurance_Type': [],
            'Doctor_Name': [],
            'Hospital_Name': [],
            'Lab_Test_Results': [],
            'X_ray_Results': [],
            'Surgery_Type': [],
            'Recovery_Time': [],
            'Allergies': [],
            'Family_History': [],
            'Patient_Satisfaction': [],
            'AI_Diagnosis_Confidence': [],
            'Indigenous_Status': [],
            'Remoteness_Category': [],
            'Adverse_Outcome': [],
            'Deterioration_24h': [],
            'Year': [],
            'Pathology_Results': [],
            'Vital_Signs_Score': [],
            'Social_History': [],
            'Aeromedical_Transport_Suitable': [],
            'Lactate': [],
            'NEWS_Score': [],
        }
        
        print(f"Generating {self.n_records} synthetic healthcare records...")
        
        for i in range(self.n_records):
            if (i + 1) % 500 == 0:
                print(f"  {i + 1}/{self.n_records} records generated...")
            
            # Basic demographics
            patient_id = i + 1
            age = int(np.clip(np.random.normal(60, 18), 18, 95))
            gender = np.random.choice(['Male', 'Female'])
            
            # Clinical data
            diagnosis = np.random.choice(self.diagnoses)
            vitals = self._generate_vital_signs(age, diagnosis)
            
            # Calculate deterioration outcome
            deterioration = self._calculate_deterioration_risk(vitals, age, diagnosis)
            
            # NEWS score calculation (National Early Warning Score)
            news_score = self._calculate_news_score(vitals)
            
            # Aeromedical suitability (relevant for Australian context)
            aero_suitable = 1 if (deterioration == 0 and vitals['oxygen_saturation'] > 90 
                                  and vitals['heart_rate'] < 130) else 0
            
            # Fill in data
            data['Patient_ID'].append(f'P{patient_id:05d}')
            data['Age'].append(age)
            data['Gender'].append(gender)
            data['Blood_Pressure'].append(round(vitals['systolic_bp'], 2))
            data['Heart_Rate'].append(round(vitals['heart_rate'], 2))
            data['Temperature'].append(round(vitals['temperature'], 2))
            data['Respiratory_Rate'].append(round(vitals['respiratory_rate'], 2))
            data['Oxygen_Saturation'].append(round(vitals['oxygen_saturation'], 2))
            data['Diagnosis'].append(diagnosis)
            data['Medication'].append(np.random.choice(self.medications))
            data['Treatment_Duration'].append(np.random.randint(1, 30))
            data['Insurance_Type'].append(np.random.choice(self.insurance_types))
            data['Doctor_Name'].append(np.random.choice(self.doctors))
            data['Hospital_Name'].append(np.random.choice(self.australian_hospitals))
            data['Lab_Test_Results'].append(round(np.random.uniform(60, 180), 2))
            data['X_ray_Results'].append(np.random.choice(['Normal', 'Abnormal']))
            data['Surgery_Type'].append(np.random.choice(self.surgeries))
            data['Recovery_Time'].append(np.random.randint(1, 30) if np.random.choice(self.surgeries) != 'None' else 0)
            data['Allergies'].append(np.random.choice(self.allergies))
            data['Family_History'].append(np.random.choice(self.family_history))
            data['Patient_Satisfaction'].append(np.random.randint(1, 5))
            data['AI_Diagnosis_Confidence'].append(round(np.random.uniform(0.7, 0.99), 3))
            data['Indigenous_Status'].append(np.random.choice(self.indigenous_status))
            data['Remoteness_Category'].append(np.random.choice(self.remoteness))
            data['Adverse_Outcome'].append(deterioration)
            data['Deterioration_24h'].append(deterioration)
            data['Year'].append(np.random.choice([2021, 2022, 2023, 2024]))
            data['Pathology_Results'].append(round(np.random.uniform(50, 150), 2))
            
            # Vital signs composite score
            vitals_score = (vitals['heart_rate']/100 + vitals['systolic_bp']/150 + 
                           vitals['respiratory_rate']/20 + vitals['temperature']/37)
            data['Vital_Signs_Score'].append(round(vitals_score, 2))
            
            data['Social_History'].append(np.random.choice(self.social_history))
            data['Aeromedical_Transport_Suitable'].append(aero_suitable)
            data['Lactate'].append(round(np.random.uniform(1, 4 + (deterioration * 3)), 2))
            data['NEWS_Score'].append(news_score)
        
        # Create DataFrame
        df = pd.DataFrame(data)
        
        print(f"✅ Dataset generation complete!")
        print(f"\nDataset Summary:")
        print(f"  Total records: {len(df)}")
        print(f"  Deterioration events: {df['Deterioration_24h'].sum()} ({df['Deterioration_24h'].mean()*100:.1f}%)")
        print(f"  Age range: {df['Age'].min()}-{df['Age'].max()} years")
        print(f"  Date range: {df['Year'].min()}-{df['Year'].max()}")
        
        return df

    def _calculate_news_score(self, vitals):
        """Calculate NEWS (National Early Warning Score) - simplified version"""
        score = 0
        
        # Respiratory rate
        if vitals['respiratory_rate'] <= 8 or vitals['respiratory_rate'] >= 25:
            score += 3
        elif vitals['respiratory_rate'] >= 21:
            score += 2
        elif vitals['respiratory_rate'] >= 9 and vitals['respiratory_rate'] <= 11:
            score += 1
            
        # Oxygen saturation
        if vitals['oxygen_saturation'] <= 91:
            score += 3
        elif vitals['oxygen_saturation'] <= 93:
            score += 2
        elif vitals['oxygen_saturation'] <= 94:
            score += 1
            
        # Systolic BP
        if vitals['systolic_bp'] <= 90 or vitals['systolic_bp'] >= 220:
            score += 3
        elif vitals['systolic_bp'] >= 200:
            score += 2
        elif vitals['systolic_bp'] <= 100 or vitals['systolic_bp'] >= 180:
            score += 1
            
        # Heart rate
        if vitals['heart_rate'] <= 40 or vitals['heart_rate'] >= 131:
            score += 3
        elif vitals['heart_rate'] >= 111:
            score += 2
        elif vitals['heart_rate'] >= 101 or vitals['heart_rate'] <= 50:
            score += 1
            
        # Temperature
        if vitals['temperature'] <= 35.0 or vitals['temperature'] >= 39.1:
            score += 2
        elif vitals['temperature'] >= 38.1:
            score += 1
            
        return score


if __name__ == "__main__":
    # Generate the dataset
    generator = HealthcareDatasetGenerator(n_records=5000)
    df = generator.generate()
    
    # Save to CSV
    output_path = '/Users/amo/local_dev/Dev-Vault/ai-healthcare-curriculum/data/AI_in_HealthCare_Dataset.csv'
    df.to_csv(output_path, index=False)
    print(f"\n✅ Dataset saved to: {output_path}")
    
    # Display sample
    print("\nSample records:")
    print(df.head(10))
    
    # Display statistics
    print("\nDataset Statistics:")
    print(df[['Age', 'Heart_Rate', 'Temperature', 'Respiratory_Rate', 
              'Oxygen_Saturation', 'NEWS_Score', 'Deterioration_24h']].describe())