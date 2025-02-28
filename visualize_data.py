import matplotlib.pyplot as plt
import pandas as pd


def visualize_single(df):
    """Visualizes the job trends data from single month."""

    # Filter the data to analyze only the categories which had 100 or more job openings for that month
    df = df[df["job_count"] >= 30]

    # Plotting the data
    plt.figure(figsize=(14, 8))
    bars = plt.barh(df["category"], df["ratio"], color="lightgreen")

    # Add text labels (ratio values) to bars
    plt.bar_label(bars, fmt="%.2f", padding=5)

    # Highlight a specific bar (for example, the "Analyst" category)
    highlight_category = "Analyst"
    highlight_color = "lightblue"

    # Loop through the bars and change the color of the specified category
    for i, bar in enumerate(bars):
        if df["category"].iloc[i] == highlight_category:
            bar.set_color(highlight_color)

    plt.xlabel("Job Openings per Application (Ratio)")
    plt.ylabel("Job Category")
    plt.title("Job Market Demand by Category")
    plt.gca().invert_yaxis()  # Flip the order for better readability
    plt.show()


def visualize_comparison(df1, df2):
    """Visualizes the comparison of job trends data for two months."""

    # Filter the data to analyze only the categories which had 100 or more job openings for that month
    df1 = df1[df1["job_count"] >= 50]
    df2 = df2[df2["job_count"] >= 50]

    # Rename columns for easier reference
    df1.columns = ['category', 'job_count_2024', 'applications_2024', 'ratio_2024']
    df2.columns = ['category', 'job_count_2025', 'applications_2025', 'ratio_2025']

    # Merge the data on 'category' using an inner join
    df_merged = pd.merge(df1, df2, on="category", how="inner")

    # Calculate the ratios and difference
    df_merged["ratio_2024"] = df_merged["job_count_2024"] / df_merged["applications_2024"]
    df_merged["ratio_2025"] = df_merged["job_count_2025"] / df_merged["applications_2025"]
    df_merged["ratio_diff"] = df_merged["ratio_2025"] - df_merged["ratio_2024"]

    # Sort by ratio_diff to make the chart more readable
    df_merged = df_merged.sort_values(by="ratio_diff")

    # Choose colors: green for positive change, red for negative change
    colors = ['lightgreen' if val > 0 else 'lightcoral' for val in df_merged["ratio_diff"]]

    # Plot the differences
    plt.figure(figsize=(14, 8))
    bars = plt.barh(df_merged["category"], df_merged["ratio_diff"], color=colors)

    # Add text labels (ratio values) to bars
    plt.bar_label(bars, fmt="%.2f", padding=5)

    # Highlight a specific bar (for example, the "Analyst" category)
    highlight_category = "Analyst"
    highlight_color = "lightblue"

    # Loop through the bars and change the color of the specified category
    for i, bar in enumerate(bars):
        if df_merged["category"].iloc[i] == highlight_category:
            bar.set_color(highlight_color)

    # Labels and title
    plt.xlabel("Job Openings per Application Ratio Change")
    plt.ylabel("Job Category")
    plt.title("Job Market Demand Change by Ratio: Jan 2024 vs. Jan 2025")
    plt.axvline(0, color="black", linestyle="--", linewidth=1)  # Add vertical line at 0 for reference

    # Show the plot
    plt.show()


def visualize_experience_trends(list_of_dfs):
    """
    Visualizes job market demand trends across experience levels using a diverging bar chart.

    Parameters:
    - list_of_dfs: List of DataFrames (each for a different experience level)
    """

    # Rename the ratio column for each experience level
    df1, df2, df3, df4 = list_of_dfs
    df1 = df1.rename(columns={"ratio": "ratio_1"})
    df2 = df2.rename(columns={"ratio": "ratio_2"})
    df3 = df3.rename(columns={"ratio": "ratio_3"})
    df4 = df4.rename(columns={"ratio": "ratio_4"})

    # Merge dataframes on "category" using OUTER JOIN to avoid empty results
    df_merged = df1[["category", "ratio_1"]].merge(
        df2[["category", "ratio_2"]], on="category", how="inner"
    ).merge(
        df3[["category", "ratio_3"]], on="category", how="inner"
    ).merge(
        df4[["category", "ratio_4"]], on="category", how="inner"
    )

    # Compute ratio sum change
    df_merged["ratio_sum_change"] = (df_merged["ratio_2"] - df_merged["ratio_1"]) + \
                                    (df_merged["ratio_3"] - df_merged["ratio_2"]) + \
                                    (df_merged["ratio_4"] - df_merged["ratio_3"])

    # Keep only category and ratio_sum_change
    df_final = df_merged[["category", "ratio_sum_change"]]
    # Group by category name in case we have duplicates
    df_final = df_final.groupby('category').agg({
        'ratio_sum_change': 'sum'
    }).reset_index()
    # Sort the values to show the most gained category on top
    df_final = df_final.sort_values(by="ratio_sum_change", ascending=True)

    # Plot diverging bar chart
    plt.figure(figsize=(14, 8))
    bars = plt.barh(df_final["category"], df_final["ratio_sum_change"],
                    color=df_final["ratio_sum_change"].apply(lambda x: "lightgreen" if x > 0 else "lightcoral"))

    highlight_categories = ["Analyst", "Data Science"]
    highlight_color = "lightblue"

    # Loop through the bars and change the color of the specified categories
    for i, bar in enumerate(bars):
        if df_final["category"].iloc[i] in highlight_categories:
            bar.set_color(highlight_color)

    plt.xlabel("Total Change in Job Openings per Application (The Sum of Ratio Change)")
    plt.ylabel("Job Category")
    plt.title("Job Market Trend by Experience Level (<1 year, 1-3 years, 3-5 years, 5+ years)")
    plt.axvline(0, color="black", linestyle="--")  # Reference line at 0
    plt.bar_label(bars, fmt="%.2f", padding=5)

    plt.show()


