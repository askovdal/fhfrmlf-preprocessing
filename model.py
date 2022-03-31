import os
import shutil

import pandas as pd

pd.set_option('display.max_colwidth', 255)  # Increases column width to examine un-truncated strings

data = pd.read_csv('train.csv')
# Filter to include only frontal x-rays
data = data[data['Path'].str.contains('frontal')]


# Make a list of the file paths
# Copy each one into a dir
def create_subset(df: pd.DataFrame, subset_name: str, length: int = 100):
    subset_folder_name = 'subsets/' + subset_name

    # Remove folder if it exists, then create new
    if os.path.exists(subset_folder_name):
        shutil.rmtree(subset_folder_name)

    os.mkdir(subset_folder_name)

    for file_path in df['Path'].sample(n=length):  # Create random sample of size n
        print(file_path)
        # Create file name from last 3 parts of the file path
        file_name = file_path.split('/')[-3:]
        file_name = '-'.join(file_name)
        shutil.copy2('../' + file_path, subset_folder_name + '/' + file_name)


# Make a list of the file paths
# Copy each one into a dir
def create_subset_csv(df: pd.DataFrame, subset_name: str, length: int = 100):
    subset_name = 'subsets/' + subset_name + '.csv'

    # Create random sample
    df = df.sample(n=length)

    df.to_csv(subset_name, index=False)


# create_subset_csv(data, '20k', 20000)

# Pneumothorax positive filter
data_thorax_positive = data.loc[data['Pneumothorax'] == 1.0]

# create_subset(data_thorax_positive, 'pneumothorax-positive', len(data_thorax_positive.index))

data_thorax_negative = data.loc[data['Pneumothorax'] == 0.0]

# create_subset_csv(data_thorax_negative, 'pneumothorax-negative', 500)

df_both = pd.concat([data_thorax_positive.sample(n=10000), data_thorax_negative.sample(n=10000)])
create_subset_csv(df_both, '20k-50-50', 20000)
#
# df_both = pd.concat([data_thorax_positive.sample(n=50), data_thorax_negative.sample(n=50)])
# create_subset_csv(df_both, 'pneumothorax-dev-100-both')
