""" upload csv files into df
sort
plot
"""
import matplotlib.pyplot as plt
import pandas as pd
from load_data import load_data
from visualize_data import visualize_single, visualize_comparison

FILEPATH_JAN24 = 'data/jan24 - Sheet1.csv'
FILEPATH_JAN25 = 'data/jan25 - Sheet1.csv'

if __name__ == '__main__':
    """Runs the visualization code using the loaded data."""
    # visualize_single(load_data(FILEPATH_JAN25))
    visualize_comparison(load_data(FILEPATH_JAN24), load_data(FILEPATH_JAN25))

