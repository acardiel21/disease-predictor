import json
import pandas as pd

def load_clusters(filepath):
    """
    Load clusters from a JSON file.
    """
    with open(filepath, "r") as f:
        clusters = json.load(f)
    return clusters

def apply_cluster_transformations(df, clusters, drop_original=True):
    """
    Apply cluster transformations to dataframe
    
    Parameters:
        df (pd.DataFrame): The DataFrame to transform.
        clusters (dict): A dictionary of clusters where keys are cluster names and values are symptom lists.
        drop_original (bool): Whether to drop the original symptom columns after transformation.
    
    Returns:
        pd.DataFrame: Transformed DataFrame with new cluster-based features.
    """
    transformed_df = df.copy()
    
    # Apply transformations for each cluster
    for cluster_name, symptoms in clusters.items():
        new_feature_name = "_or_".join(symptom.lower().replace(" ", "_") for symptom in symptoms)
        transformed_df[new_feature_name] = transformed_df[symptoms].sum(axis=1).clip(upper=1)  
    
    if drop_original:
        all_clustered_symptoms = [symptom for symptoms in clusters.values() for symptom in symptoms]
        transformed_df = transformed_df.drop(columns=all_clustered_symptoms)
    
    return transformed_df
