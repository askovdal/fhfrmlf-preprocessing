from sklearn.model_selection import train_test_split
import pandas as pd


def create_train_test_split(csv_name):
    """
    Creates a train and test csv from input csv
    """
    df = pd.read_csv(csv_name)

    train, test = train_test_split(df, train_size=0.8)

    train.to_csv(csv_name.replace('.csv', '') + '-train.csv')
    test.to_csv(csv_name.replace('.csv', '') + '-test.csv')


create_train_test_split('subsets/pneumothorax-positive-tube-split.csv')
