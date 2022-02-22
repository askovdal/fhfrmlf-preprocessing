import pandas as pd
import shutil

pd.set_option('display.max_colwidth', 255)  # Increases column width to examine un-truncated strings

data = pd.read_csv('train.csv')

# Pneumothorax positive, support device negative
data_thorax = data.loc[(data['Pneumothorax'] == 1.0) & (data['Support Devices'] == 0.0)]

# Pneumothorax positive, support device uncertain
data_thorax_uncertainSP = data.loc[(data['Pneumothorax'] == 1.0) & (data['Support Devices'] == -1.0)]

# Pneumothorax positive, support device positive
data_thoraxSP = data.loc[(data['Pneumothorax'] == 1.0) & (data['Support Devices'] == 1.0)]


# Make a list of the file paths
# Copy each one into a dir

def create_subset(df: pd.DataFrame, subset_name: str):
    length = 100
    if len(df) < length:
        length = len(df['Path'])

    for file_path in df['Path'].sample(n=length):
        print(file_path)
        # Create file name from last 3 parts of the file path
        file_name = file_path.split('/')[-3:]
        file_name = '-'.join(file_name)
        shutil.copy2('../' + file_path, 'subsets/' + subset_name + '/' + file_name)


create_subset(data_thorax, 'pneumothorax-no-support-devices')
create_subset(data_thorax_uncertainSP, 'pneumothorax-uncertain-support-devices')
create_subset(data_thoraxSP, 'pneumothorax-support-devices')
