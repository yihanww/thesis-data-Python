# Data loading modules
import pandas as pd


def load_data(fname):
    """
    Loads data from .csv file.
    :param fname: full path of file
    :return: dataframe
    """
    df_loaded = pd.read_csv(fname)
    print(f'Loaded {fname}')
    return df_loaded


def save_data(fname, df_in):
    """
    Saves data to .csv file.
    :param fname: full path of file
    :param df_in: dataframe to be saved
    :return: None
    """
    df_saved = df_in.to_csv(fname)

    print(f'Saved to {fname}')
    return df_saved