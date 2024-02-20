import json  

def openq(df):
    """
    Parse the JSON strings in the 'form_data' column of the DataFrame where 'form_data' contains 'whatTested'.
    :param df: DataFrame containing all responses from the participants.
    :returns: A list of parsed JSON objects from the 'form_data' column.
    """
    # Filter out rows with missing 'form_data' and rows where 'form_data' does not contain 'whatTested'
    openq_data = df.dropna(subset=['form_data'])
    openq_data = openq_data[openq_data['form_data'].str.contains('whatTested')]

    # Parse JSON strings and store in a list
    openq_answers = []
    for json_str in openq_data['form_data']:
        parsed_json = json.loads(json_str)  # Parse each JSON string
        openq_answers.append(parsed_json)  # Add the parsed JSON object to the list

    return openq_answers  # Return the list of parsed JSON objects
