# Synthetic Data Downloads

This page provides access to all synthetic datasets created for the AI in Healthcare curriculum. Each dataset is described below, with a download link and a summary of its fields and intended use.

| Dataset | Description | Download | Key Fields |
|---------|-------------|----------|------------|
| **AI_in_HealthCare_Dataset.csv** | A comprehensive synthetic dataset simulating Australian hospital patient records. Useful for ML tasks such as deterioration prediction, risk scoring, and exploring healthcare data in an Australian context. | [Download CSV](../../data/AI_in_HealthCare_Dataset.csv) | Patient_ID, Age, Gender, Blood_Pressure, Heart_Rate, Temperature, Respiratory_Rate, Oxygen_Saturation, Diagnosis, Medication, Treatment_Duration, Insurance_Type, Doctor_Name, Hospital_Name, Lab_Test_Results, X_ray_Results, Surgery_Type, Recovery_Time, Allergies, Family_History, Patient_Satisfaction, AI_Diagnosis_Confidence, Indigenous_Status, Remoteness_Category, Adverse_Outcome, Deterioration_24h, Year, Pathology_Results, Vital_Signs_Score, Social_History, Aeromedical_Transport_Suitable, Lactate, NEWS_Score |
| **aihw_injcat213_suppdatatables_bystate_v2_25112025.xlsx** | Supplementary synthetic tables based on Australian Institute of Health and Welfare injury data, by state. Useful for epidemiological analysis and public health exercises. | [Download Excel](../../data/aihw_injcat213_suppdatatables_bystate_v2_25112025.xlsx) | Multiple sheets: Each sheet contains columns such as State, Year, Injury Type, Age Group, Sex, Hospitalisations, Deaths, Rates, etc. |

## Dataset Details

### AI_in_HealthCare_Dataset.csv
- **Purpose:** Simulates realistic patient records for Australian hospitals, supporting exercises in ML, risk prediction, and healthcare analytics.
- **Fields:**
    - Patient_ID, Age, Gender, Blood_Pressure, Heart_Rate, Temperature, Respiratory_Rate, Oxygen_Saturation
    - Diagnosis, Medication, Treatment_Duration, Insurance_Type, Doctor_Name, Hospital_Name
    - Lab_Test_Results, X_ray_Results, Surgery_Type, Recovery_Time, Allergies, Family_History
    - Patient_Satisfaction, AI_Diagnosis_Confidence, Indigenous_Status, Remoteness_Category
    - Adverse_Outcome, Deterioration_24h, Year, Pathology_Results, Vital_Signs_Score, Social_History
    - Aeromedical_Transport_Suitable, Lactate, NEWS_Score
- **Example Use Cases:**
    - Predicting patient deterioration
    - Exploring social and demographic health factors
    - Simulating clinical decision support

### aihw_injcat213_suppdatatables_bystate_v2_25112025.xlsx
- **Purpose:** Provides synthetic injury and hospitalisation data by state, for public health and epidemiology exercises.
- **Fields:**
    - Vary by sheet, but typically include: State, Year, Injury Type, Age Group, Sex, Hospitalisations, Deaths, Rates, etc.
- **Example Use Cases:**
    - Analyzing injury trends by state
    - Comparing hospitalisation rates across demographics
    - Public health planning and resource allocation

---

*For more information on how these datasets were generated, see the scripts in the [scripts/](../../scripts/) directory.*
