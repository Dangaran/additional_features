# Preliminary plots

Script to import the class preliminary_plots. With this class you can make simple plotnine plots for your DataFrames.

The plots to show are:

- Scatterplot
- Lineplot
- Barplot
- Density plot
- Histogram
- Boxplot
- Countplot

# Functionality

Select the option **manual = True** in each method to check the available options before using them.

Input:
  - *pandas_db*: df, pandas dataframe with the variables to plot
  - *x_axis*: str, column name to plot in x axis
  - *y_axis*: str, column name to plot in y axis

Output:
  - If *manual=True*: check the available options for that method
  - If *manual=False* (default option): plot from selected method
    
