import os
import pandas as pd


def filter_suffix(filenames: list[str], suffix: str, negate: bool):
    filtered_files = []
    for filename in filenames:
        # Remove the file extension from the filename
        name_wo_extension = '.'.join(filename.split('.')[:-1])

        if negate:
            if not name_wo_extension.endswith(suffix):
                # Remove the suffix from the filename
                filtered_files.append(filename.replace(suffix, ''))
        else:
            if name_wo_extension.endswith(suffix):
                # Remove the suffix from the filename
                filtered_files.append(filename.replace(suffix, ''))

    return filtered_files


def create_csv_from_dir(dir_name: str, csv_name: str, suffix='', length: int = None, negate=False):
    """
    Creates a CSV from a directory of files.
    :param dir_name: Name of directory with the files that go into the CSV.
    :param csv_name: Name to use for the created CSV.
    :param suffix: Optional suffix to filter the filenames on. Only files with this suffix wil be used.
    :param length: The length of the CSV. Random files from the directory will be used.
    :param negate: If True, only uses files without the suffix.
    """
    filenames = os.listdir(dir_name)

    if suffix:
        filenames = filter_suffix(filenames, suffix, negate)

    main_df = pd.read_csv('train.csv')

    # Create a mask of the file paths that match `filenames`
    mask = main_df['Path'].str.removeprefix('CheXpert-v1.0/train/').str.replace('/', '-').isin(filenames)
    dir_df = main_df.loc[mask]

    if length and length < len(dir_df.index):
        dir_df = dir_df.sample(n=length)

    # Shuffle rows
    dir_df = dir_df.sample(frac=1)

    dir_df.to_csv(csv_name, index=False)


create_csv_from_dir('subsets/pneumothorax-positive', 'subsets/pneumothorax-positive-w-tube.csv', '_TUBE', 200, False)
create_csv_from_dir('subsets/pneumothorax-positive', 'subsets/pneumothorax-positive-wo-tube.csv', '_TUBE', 200, True)
