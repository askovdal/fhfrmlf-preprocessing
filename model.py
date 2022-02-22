import os
import shutil

import pandas as pd

pd.set_option('display.max_colwidth', 255)  # Increases column width to examine un-truncated strings

data = pd.read_csv('train.csv')

# Pneumothorax positive filter
data_thorax = data.loc[data['Pneumothorax'] == 1.0]


# Make a list of the file paths
# Copy each one into a dir
def create_subset(df: pd.DataFrame, subset_name: str, length: int = 100):
    # Remove folder, if it exists, then create new
    subset_folder_name = 'subsets/' + subset_name

    if os.path.exists(subset_folder_name):
        shutil.rmtree(subset_folder_name)

    os.mkdir(subset_folder_name)

    df = df[df['Path'].str.contains('frontal')]  # Filter to only include frontal x-rays

    for file_path in df['Path'].sample(n=length):  # Create random sample of size n
        print(file_path)
        # Create file name from last 3 parts of the file path
        file_name = file_path.split('/')[-3:]
        file_name = '-'.join(file_name)
        shutil.copy2('../' + file_path, subset_folder_name + '/' + file_name)


create_subset(data_thorax, 'pneumothorax_positive')
