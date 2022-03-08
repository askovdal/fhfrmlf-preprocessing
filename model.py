import os
import shutil

import pandas as pd

pd.set_option('display.max_colwidth', 255)  # Increases column width to examine un-truncated strings

data = pd.read_csv('train.csv')
data = data[data['Path'].str.contains('frontal')]


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


# Make a list of the file paths
# Copy each one into a dir
def create_subset_csv(df: pd.DataFrame, subset_name: str, length: int = 100):
    # Remove folder, if it exists, then create new
    subset_name = 'subsets/' + subset_name + '.csv'

    # Filter to only include frontal x-rays
    df = df[df['Path'].str.contains('frontal')]

    # Create random sample
    df = df.sample(n=length)

    df.to_csv(subset_name, index=False)


# Pneumothorax positive filter
data_thorax_positive = data.loc[data['Pneumothorax'] == 1.0]

create_subset(data_thorax_positive, 'pneumothorax-positive', len(data_thorax_positive.index))

# data_thorax_negative = data.loc[data['Pneumothorax'] == 0.0]
#
# df_both = pd.concat([data_thorax_positive.sample(n=50), data_thorax_negative.sample(n=50)])
# create_subset_csv(df_both, 'pneumothorax-train-100-both')
#
# df_both = pd.concat([data_thorax_positive.sample(n=50), data_thorax_negative.sample(n=50)])
# create_subset_csv(df_both, 'pneumothorax-dev-100-both')
