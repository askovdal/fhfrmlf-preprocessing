import pandas as pd


def concat_half_csv(name1, name2, out_name):
    """
    Takes 2 csv files as input and concats half of each into an output csv
    """
    df1 = pd.read_csv(name1)
    df2 = pd.read_csv(name2)

    # Use the smallest df to dictate the split amount
    split_amount = min([len(df1.index), len(df2.index)]) // 2

    split_df = pd.concat([df1.sample(n=split_amount), df2.sample(n=split_amount)])

    split_df.to_csv(out_name, index=False)


concat_half_csv('subsets/pneumothorax-positive-w-tube.csv', 'subsets/pneumothorax-positive-wo-tube.csv',
                'subsets/pneumothorax-positive-tube-split.csv')
