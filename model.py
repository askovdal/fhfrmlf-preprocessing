import pandas as pd

data = pd.read_csv('train.csv')

data_p = data.loc[data['Pneumothorax'] == 1.0]

print(data_p.index)
