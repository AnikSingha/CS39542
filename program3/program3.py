"""
    Name: Anik Singha
    Email: anik.singha68@myhunter.cuny.edu
    Resources:
"""

import pandas as pd

def clean_df(df, year = 2015):
    """
    df: the name of a DataFrame containing TreesCount Data from OpenData NYC.
    year: the year of the data set. There are three possible years 1995, 2005,
    or 2015. The default value is 2015.
    """
    columns = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'nta', 'latitude', 'longitude']
    if year == 2005:
        df = df[['tree_dbh', 'status', 'spc_latin', 'spc_common', 'nta', 'latitude', 'longitude']]
        df.rename(columns={"status":"health"}, inplace=True)
    elif year == 1995:
        df = df[['diameter', 'condition', 'spc_latin', 'spc_common',
                'nta_2010', 'latitude', 'longitude']]
        df.rename(columns={"diameter":"tree_dbh", "condition":"health",
                "nta_2010":"nta"}, inplace=True)
    return df[columns]

def make_nta_df(file_name):
    """
    file_name: the name of a CSV file containing population and names for neighborhood
    tabulation areas (NYC OpenData NTA Demographics).
    The function should open the file file_name as DataFrame, returns a DataFrame containing
    only the columns containing the NTA code (labeled as nta_code), the neigborhood name
    (labeled as nta_name), and the 2010 population (labeled as population)."""
    df = pd.read_csv(file_name)
    df.rename(columns={"Geographic Area - Neighborhood Tabulation Area (NTA)* Code":"nta_code",
                        "Geographic Area - Neighborhood Tabulation Area (NTA)* Name":"nta_name",
                        "Total Population 2010 Number":"population"},inplace=True)
    return df[["nta_code","nta_name","population"]]

def count_by_area(df):
    """
    The function should return a DataFrame that has two columns, [nta, num_trees] where
    nta is the code of the Neighborhood Tabulation Area and num_trees is the sum of the
    number of trees, grouped by nta.
    """
    return df.groupby("nta")["nta"].count().to_frame("num_trees").reset_index()

def neighborhood_trees(tree_df, nta_df):
    """
    tree_df: a DataFrame containing the column nta
    nta_df: a DataFrame with two columns, 'NTACode' and 'NTAName'.
    This function returns a DataFrame as a result of joining the two input dataframes,
    with tree_df as the left table. The join should be on NTA code.
    """
    new = pd.merge(tree_df, nta_df, how="left", left_on="nta", right_on="nta_code")
    new["trees_per_capita"] = new["num_trees"] / new["population"]
    return new[['nta','num_trees','nta_name','population','trees_per_capita']]

def compute_summary_stats(df, col):
    """
    df: a DataFrame containing a column col.
    col: the name of a numeric-valued col in the DataFrame.
    This function returns the mean and median of the Series df[col]. Note that
    since numpy is not one of the libraries for this assignment, your function
    should compute these statistics without using numpy.
    """
    return df[col].mean(), df[col].median()

def mse_loss(theta,y_vals):
    """
    theta: a numeric value.
    y_vals: a Series containing numeric values.
    Computes the Mean Squared Error of the parameter theta and a Series, y_vals.
    See Section 4.2: Modeling Loss Functions where this function is implemented using numpy.
    """
    total = 0
    for val in y_vals:
        total += (val-theta)**2
    return total/len(y_vals)

def mae_loss(theta,y_vals):
    """
    theta: a numeric value.
    y_vals: a Series containing numeric values.
    Computes the Mean Absolute Error of the parameter theta and a Series, y_vals. See
    Section 4.2: Modeling Loss Functions where this function is implemented using numpy
    """
    total = 0
    for val in y_vals:
        total += abs(val-theta)
    return total/len(y_vals)

def test_mse(loss_fnc=mse_loss):
    """
    loss_fnc: a function that takes in two input parameters (a numeric value and a Series
    of numeric values) and returns a numeric value. It has a default value of mse_loss.
    This is a test function, used to test whether the loss_fnc returning True if the loss_fnc
    performs correctly (e.g. computes Mean Squared Error) and False otherwise.
    """
    vals = [1,2,3,4,5]
    if loss_fnc(2,vals) == mse_loss(2,vals):
        return True
    return False
