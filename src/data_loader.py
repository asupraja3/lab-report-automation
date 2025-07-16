import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Drop rows with too many missing values
    df.dropna(thresh=15, inplace=True)

    # Fill numeric missing values with median
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical with mode
    for col in df.select_dtypes(include='object').columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Convert target variable
    df['classification'] = df['classification'].replace({'ckd': 1, 'notckd': 0})

    # Encode other object columns
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df, label_encoders

