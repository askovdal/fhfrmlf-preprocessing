import pandas as pd


def shuffle_csv(name):
    df = pd.read_csv(name)

    df = df.sample(frac=1)

    df.to_csv(name, index=False)


shuffle_csv('subsets/pneumothorax-mixed-p-tube-split.csv')
shuffle_csv('subsets/pneumothorax-mixed-p-w-tube.csv')
shuffle_csv('subsets/pneumothorax-mixed-p-wo-tube.csv')
