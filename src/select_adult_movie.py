
import json
from pandas import json_normalize
from typing import Dict,Any


def check_adult_limit(json_data: str) -> str:
    """
    Select the adult or not information attached to each film's name

    Args:
        json_data (str): A JSON string representation of movie data.

    Returns:
        str: A JSON string containing filtered data with columns 'adult', 'original_title',
        and 'overview'.


    """
    # Parse the JSON string into a DataFrame
    df = json_normalize(json.loads(json_data))

    # Select the relevant columns
    df = df[['adult', 'original_title']]

    # Convert the DataFrame to a JSON string and return
    return df.to_json(orient='records')
