# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable1, variable2):
    # scatter plot with variable against target and fit a line
    sns.lmplot(variable1, variable2, data=data, fit_reg=True)
    return None
