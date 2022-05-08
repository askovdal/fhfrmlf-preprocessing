import pandas as pd

data = pd.read_csv("ensemble-test.csv", usecols=["best1", "best2", "best3"])
print(data.corr())
