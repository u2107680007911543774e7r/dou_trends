from load_data import load_data
from visualize_data import visualize_single, visualize_comparison,\
    visualize_exp_trends, visualize_analytics_exp_trends

FILEPATH_JAN24 = 'data/jan24.csv'
FILEPATH_JAN25 = 'data/jan25.csv'
LIST_OF_JAN24_BY_YEARS_OF_EXP = ['data/jan24_less_than_1_year_of_exp.csv',
                                 'data/jan24_1_3_years_of_exp.csv',
                                 'data/jan24_3_5_years_of_exp.csv',
                                 'data/jan24_more_than_5_years_of_exp.csv']
LIST_OF_JAN25_BY_YEARS_OF_EXP = ['data/jan25_less_than_1_year_of_exp.csv',
                                 'data/jan25_1_3_years_of_exp.csv',
                                 'data/jan25_3_5_years_of_exp.csv',
                                 'data/jan25_more_than_5_years_of_exp.csv']

if __name__ == '__main__':
    """Runs the visualization code using the loaded data."""

    """ Uncomment the next line to plot the data for Jan 24 """
    # visualize_single(load_data(FILEPATH_JAN24))

    """ Uncomment the next line to plot the data for Jan 25 """
    # visualize_single(load_data(FILEPATH_JAN25))

    """ Uncomment the next line to plot the data comparison for Jan 24 and Jan 25 """
    # visualize_comparison(load_data(FILEPATH_JAN24), load_data(FILEPATH_JAN25))

    """ Uncomment the next line to plot the data about the gains and demand of the Jan 2024 market by experience """
    # visualize_exp_trends([load_data(file) for file in LIST_OF_JAN24_BY_YEARS_OF_EXP])

    """ Uncomment the next line to plot the data about the gains and demand of the Jan 2025 market by experience """
    # visualize_exp_trends([load_data(file) for file in LIST_OF_JAN25_BY_YEARS_OF_EXP])

    """ Uncomment the next line to plot the data comparison about gains and demand of the Analyst role 
    between Jan 2024 and 2025 with the growth of experience """
    visualize_analytics_exp_trends([load_data(file) for file in LIST_OF_JAN24_BY_YEARS_OF_EXP],
                                   [load_data(file) for file in LIST_OF_JAN25_BY_YEARS_OF_EXP])
