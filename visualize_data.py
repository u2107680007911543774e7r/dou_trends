import matplotlib.pyplot as plt
import pandas as pd

def visualize_single(df):
    """Visualizes the job trends data from single month."""

    # Plotting the data
    plt.figure(figsize=(14, 8))
    bars = plt.barh(df["category"], df["ratio"], color="green")

    # Add text labels (ratio values) to bars
    plt.bar_label(bars, fmt="%.2f", padding=5)

    plt.xlabel("Job Openings per Application (Ratio)")
    plt.ylabel("Job Category")
    plt.title("Job Market Demand by Category")
    plt.gca().invert_yaxis()  # Flip the order for better readability
    plt.show()

def visualize_comparison(df1, df2):
    """Visualizes the comparison of job trends data for two months."""

    # Rename columns for easier reference (if necessary, adjust this step based on your file)
    df1.columns = ['category', 'job_count_2024', 'applications_2024', 'ratio_2024']
    df2.columns = ['category', 'job_count_2025', 'applications_2025', 'ratio_2025']

    # Merge the data on 'category' using an inner join
    df_merged = pd.merge(df1, df2, on="category", how="inner")

    # Calculate the ratios for 2024 and 2025
    df_merged["ratio_2024"] = df_merged["job_count_2024"] / df_merged["applications_2024"]
    df_merged["ratio_2025"] = df_merged["job_count_2025"] / df_merged["applications_2025"]

    # Plotting the comparison
    plt.figure(figsize=(14, 8))

    # Plot 2024 ratios
    bars_2024 = plt.barh(df_merged["category"], df_merged["ratio_2024"], color="green", label="2024")

    # Plot 2025 ratios
    bars_2025 = plt.barh(df_merged["category"], df_merged["ratio_2025"], color="blue", label="2025", alpha=0.6)

    # Add text labels (ratio values) to bars
    plt.bar_label(bars_2024, fmt="%.2f", padding=5, color="white")
    plt.bar_label(bars_2025, fmt="%.2f", padding=5, color="white")

    # Labels and title
    plt.xlabel("Job Openings per Application (Ratio)")
    plt.ylabel("Job Category")
    plt.title("Job Market Demand Comparison: January 2024 vs. January 2025")
    plt.gca().invert_yaxis()  # Flip the order for better readability

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()
