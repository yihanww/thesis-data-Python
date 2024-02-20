import pandas as pd
from scipy.stats import pearsonr

def calculate_correlation(first_all,second_all,nrow):
    """
    Calculate the Pearson correlation score for each participant.
    :prm nrow: DataFrame containing all responses from the participants.
    returns:The specific Pearson correlation score for each participant.
    """
    column_to_melt1 = first_all.iloc[nrow].to_frame()  
    long_df1 = column_to_melt1.melt(var_name='pid', value_name='first_rating')
    column_to_melt2 = second_all.iloc[nrow].to_frame()  
    long_df2 = column_to_melt2.melt(var_name='pid', value_name='second_rating')

    # Combining the data
    combined_df = pd.concat([long_df1, long_df2], axis = 1)

    # Calculating the Pearson correlation
    correlation = pearsonr(combined_df['first_rating'], combined_df['second_rating'])
    return correlation