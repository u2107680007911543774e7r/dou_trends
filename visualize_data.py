import matplotlib.pyplot as plt

def visualize_data(df):
    """Visualizes the job trends data."""
    category_counts = df['Category'].value_counts()

    # Plotting the data
    category_counts.plot(kind='bar', figsize=(10, 6))
    plt.title('Number of Jobs per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Jobs')
    plt.show()
