import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    new_df=patients['conditions'].str.contains(r'(^|\s)DIAB1', na=False)
    return patients.loc[new_df,['patient_id','patient_name' ,'conditions']].sort_values('patient_id')