
def response(df):
    """
    Get responses scores from each participant and form a tidy DataFrame.
    
    :param df: DataFrame containing the full dataset.
    :return: A pivoted DataFrame with 'PROLIFIC_PID' as rows, 'stimulus_num' as columns, and 'response' as values.
    """
    # Filter and drop missing values
    response_data = df[['PROLIFIC_PID', 'stimulus', 'response']].dropna()

    # Extract stimulus number from the 'stimulus' column and convert to int
    response_data['stimulus_num'] = response_data['stimulus'].str.extract(r'(\d+)\.jpeg').astype(int)

    # Pivot the table to organize responses by 'PROLIFIC_PID' and 'stimulus_num'
    pivoted_data = response_data.pivot_table(index='PROLIFIC_PID', columns='stimulus_num', values='response', aggfunc='first')

    return pivoted_data

