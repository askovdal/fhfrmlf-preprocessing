import pandas as pd


def concat_csvs(name1, name2, out_name, frac=1.0):
    """
    Takes 2 csv files as input and concats each into an output csv.
    :param name1:
    :param name2:
    :param out_name:
    :param frac: What fraction to use of each csv. If frac = 0.5, 50% of each will be used.
    """
    df1 = pd.read_csv(name1)
    df2 = pd.read_csv(name2)

    # Use the smallest df to dictate the split amount
    split_amount = int(min([len(df1.index), len(df2.index)]) / (1 / frac))

    split_df = pd.concat([df1.sample(n=split_amount), df2.sample(n=split_amount)])

    split_df.to_csv(out_name, index=False)


concat_csvs('subsets/pneumothorax-positive-w-tube.csv', 'subsets/pneumothorax-negative.csv',
            'subsets/pneumothorax-mixed-p-w-tube.csv', 0.5)

concat_csvs('subsets/pneumothorax-positive-wo-tube.csv', 'subsets/pneumothorax-negative.csv',
            'subsets/pneumothorax-mixed-p-wo-tube.csv', 0.5)

concat_csvs('subsets/pneumothorax-positive-w-tube.csv', 'subsets/pneumothorax-positive-wo-tube.csv',
            'subsets/pneumothorax-positive-tube-split.csv', 0.25)

concat_csvs('subsets/pneumothorax-positive-tube-split.csv', 'subsets/pneumothorax-negative.csv',
            'subsets/pneumothorax-mixed-p-tube-split.csv')
