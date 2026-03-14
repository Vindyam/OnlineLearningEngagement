import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'online_learning_engagement_dataset.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'online_learning_engagement_dataset_clean.csv')

df = pd.read_csv(DATA_PATH)

# Basic data quality checks
df = df.drop_duplicates().copy()

# Example type enforcement
categorical_cols = ['gender', 'country', 'device_type']
for col in categorical_cols:
    df[col] = df[col].astype('category')

# Save a cleaned version for downstream analysis
df.to_csv(OUTPUT_PATH, index=False)
print('Saved cleaned dataset to:', OUTPUT_PATH)
