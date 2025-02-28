import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file into a Pandas DataFrame and sets column names."""

    column_names = ["category", "job_count", "applications"]  # Replace with your actual column names
    df = pd.read_csv(file_path, names=column_names, header=None)
    df["ratio"] = df["job_count"] / df["applications"]  # Create a new column 'ratio' = job_count/applications
    df = df.sort_values(by=["ratio"], ascending=[False])  # Sort by 'ratio' to see the demand-to-supply balance
    # Adjust the table by cleaning the unnecessary data by removing the "Other" category
    df = df[df["category"] != "Other"]
    df = df[df['job_count'] >= 2]
    return df
