import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df
