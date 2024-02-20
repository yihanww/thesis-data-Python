# Import packages
import pandas as pd
from data_pipeline import In_Out as IO
from data_pipeline import calculate_correlation as cor

# Data Read In
fulldata = IO.load_data("./fulldata.csv")


# Data Cleaning Step 1 - Access
# Responses Scores from Each Participant
response = fulldata[['PROLIFIC_PID', 'stimulus', 'response']].dropna()
response['stimulus_num'] = response['stimulus'].str.extract(r'(\d+)\.jpeg').astype(int)
response = response.pivot_table(index='PROLIFIC_PID', columns='stimulus_num', values='response')

# Drop specific rows
rows_to_drop = [1, 12, 15, 94, 98, 106] 
response.drop(response.index[rows_to_drop], inplace=True)


# Answers of the Open-ended Questions from Each Participant
openq_data = openq(fulldata)

# Convert the list of dictionaries to a DataFrame
openq_answer_df = pd.DataFrame(openq_answers)

# If you need to add the PROLIFIC_PID to the new DataFrame
openq_answer_df['PROLIFIC_PID'] = openq_data['PROLIFIC_PID'].values


first_presentation_indices = [7, 62, 32, 55, 43, 24, 92, 86, 95, 76, 71, 88, 33, 45, 79, 49, 10, 14, 65, 34, 59, 4, 23, 56]
first_all = response.iloc[:, first_presentation_indices]
second_presentation_indices = list(range(126, 150))
second_all = response.iloc[:, second_presentation_indices]


column_to_melt1 = first_all.iloc[0].to_frame()  
long_df1 = column_to_melt1.melt(var_name='pid', value_name='first_rating')
column_to_melt2 = second_all.iloc[0].to_frame()  # Convert the Series to DataFrame
long_df2 = column_to_melt2.melt(var_name='pid', value_name='second_rating')
combined_df = pd.concat([long_df1, long_df2], axis = 1)

# calculate correlation
correlation_result = []
for i in range(len(first_all)):
    correlation_result.append(cor(first_all,second_all,i))
correlation_result

unreliable = [index for index, result in enumerate(correlation_result) if result.correlation <= 0]
response.drop(response.index[unreliable], inplace=True)