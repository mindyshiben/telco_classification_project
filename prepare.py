import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import acquire

def prep_telco(df):
    df = df.drop(['Unnamed: 0',	'customer_id'], axis=1)
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
    df.dropna(subset=['total_charges'], inplace=True)
    df['online_security'] = df['online_security'].replace({'No internet service':'No'})
    df['online_backup'] = df['online_backup'].replace({'No internet service':'No'})
    df['device_protection'] = df['device_protection'].replace({'No internet service':'No'})
    df['tech_support'] = df['tech_support'].replace({'No internet service':'No'})
    df['streaming_tv'] = df['streaming_tv'].replace({'No internet service':'No'})
    df['streaming_movies'] = df['streaming_movies'].replace({'No internet service':'No'})
    df['multiple_lines'] = df['multiple_lines'].replace({'No phone service':'No'})
    dummy = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'payment_type', 'contract_type']],
    dummy_na=False, drop_first=[True, True, True, True, True, True, True, True, True, True, True, True, True])
    dummy.rename(columns = {'gender_Male': 'e_gender_male', 'partner_Yes':'e_partner',
                                    'dependents_Yes':'e_dependents',
            'phone_service_Yes': 'e_phone_service', 'multiple_lines_Yes': 'e_multiple_lines',
            'tech_support_Yes': 'e_tech_support', 'streaming_tv_Yes': 'e_tv_stream',
            'streaming_movies_Yes': 'e_movies_stream',
            'paperless_billing_Yes': 'e_paperless_bill', 'churn_Yes': 'e_churn',
            'internet_service_type_Fiber optic' : 'e_fiber_optic', 'internet_service_type_None': 'e_no_internet',
            'payment_type_Credit card (automatic)': 'e_cc_auto', 'payment_type_Electronic check': 'e_check_electric',
            'payment_type_Mailed check': 'e_check_mail', 'contract_type_One year': 'e_oneyr',
            'contract_type_Two year': 'e_twoyr'}, inplace = True)
    df = pd.concat([dummy, df], axis=1)
    return df

    
    

