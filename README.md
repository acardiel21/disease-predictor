# Symptom-Based Diagnosis and ICD-11 Recommendation Tool
## Description 
This program is designed to streamline the diagnostic process by allowing healthcare providers to input patient symptoms and receive recommended diagnoses along with their corresponding ICD-11 codes. The program leverages a symptom-to-diagnosis mapping system, integrating medical databases to ensure accurate and reliable suggestions. 

Key Features:
- **Symptom Input:** Enter one or multiple symptoms into the interface. 
- **Diagnosis Recommendations:** The tool provides a ranked (top 3) list of potential diagnoses based on the entered symptoms, paired with their probability based on the model. 
- **ICD-11 Code Integration:** Each recommended diagnosis is accompanied by its corresponding ICD-11 code for seamless documentation.
- **Notes Section:** Physicians can add customized notes, observations, or additional details for each case, supporting comprehensive patient records.
- **Efficient Workflow:** Designed to save time and improve diagnostic accuracy, the idea would be for this tool to be used for busy clinical settings or telemedicine consultations.

This program empowers healthcare professionals to make informed decisions while reducing the cognitive load of remembering extensive diagnostic criteria and coding systems necessary for insurance purposes or healthcare records systems. 

## Motivation 
As I have developed my abilities in data science and programming, I have worked to more deeply explore the connections between this field and healthcare. Since the COVID-19 pandemic, it has become abundantly clear just how important health surveillance is-- but collecting all of this data doesn't matter if we can't do anything with it. This project represents my personal introduction and exploration to the utilization of health data in analytics and disease prediction.

## Datasets
Used the Symptom-Disease Prediction Dataset (SDPD) from Tucker, Jay (2024), “SymbiPredict”, Mendeley Data, V1, doi: 10.17632/dv5z3v2xyd.1 (https://data.mendeley.com/datasets/dv5z3v2xyd/1), which links symptoms to various conditions. 

I also accessed the World Health Organization (WHO) International Classification of Diseases (https://icd.who.int/en) to match the various prognoses to their relevant ICD code. 
ICD codes represent a standardized system of coding diseases and medical conditions, used by both public health officials and healthcare providers when diagnosing patients. 


