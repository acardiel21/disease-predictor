# Symptom-Based Diagnosis and ICD-11 Recommendation Tool (in progress)
## Description 
This program is designed to streamline the diagnostic process by allowing healthcare providers to input patient symptoms and receive recommended diagnoses along with their corresponding ICD-11 codes. 

Key Features:
- **Symptom Input:** Enter one or multiple symptoms into the interface. 
- **Diagnosis Recommendations:** The tool provides a ranked (top 3) list of potential diagnoses based on the entered symptoms, paired with their probability based on the model. 
- **ICD-11 Code Integration:** Each recommended diagnosis is accompanied by its corresponding ICD-11 code for seamless documentation.
- **Efficient Workflow:** Designed to save time and improve diagnostic accuracy, this tool is meant to represent a sort of rudimentary version of what a lot of EMR and EHR systems do. 

## Datasets
Used the Symptom-Disease Prediction Dataset (SDPD) from Tucker, Jay (2024), “SymbiPredict”, Mendeley Data, V1, doi: 10.17632/dv5z3v2xyd.1 (https://data.mendeley.com/datasets/dv5z3v2xyd/1), which links symptoms to various conditions. 

I also accessed the World Health Organization (WHO) International Classification of Diseases (https://icd.who.int/en) to match the various prognoses to their relevant ICD code. 
ICD codes represent a standardized system of coding diseases and medical conditions, used by both public health officials and healthcare providers when diagnosing patients. 


