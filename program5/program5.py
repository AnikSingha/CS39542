"""
Name: Anik Singha
Email: anik.singha68@myhunter.cuny.edu
Resources:
"""

import pandas as pd

def parse_datetime(df, column='DATE'):
    '''
    df: a DataFrame containing the column column.
    column: the name of a column. column has default value of 'DATE'
    The function should return a DataFrame with three additional columns:
    timestamp: contains the datetime object corresponding to the string stored in column.
    month: return the number corresponding to the month of timestamp: 1 for Jan, ... 12 for Dec
    year: return the number corresponding to year of timestamp.
    '''
    df["timestamp"] = pd.to_datetime(df[column])
    df["month"] = df["timestamp"].dt.month
    df["year"] = df["timestamp"].dt.year
    return df

def compute_lin_reg(xes, yes):
    '''
    xes: an iterables of numeric values representing the independent variable
    yes: an iterables of numeric values representing the dependent variable
    The function computes the slope and y-intercept of the linear regression line
    using ordinary least squares. The pseudocode for this:
    Compute the standard deviation of the xes and yes. Call these sd_x and sd_y.
    Compute the correlation, r, of the xes and yes.
    Compute the slope, theta_1, as theta_1 = r*sd_y/sd_x.
    Compute the y-intercept, theta_0, as theta_0 = average(yes) - theta_1 * average(xes)
    Return theta_0 and theta_1
    '''
    sd_x = xes.std()
    sd_y = yes.std()
    r = xes.corr(yes)
    theta_1 = r * sd_y / sd_x
    theta_0 = yes.mean() - theta_1 * xes.mean()
    return theta_0, theta_1


def predict(xes, theta_0, theta_1):
    '''
    xes: an iterables of numeric values representing the independent variable
    theta_0: the y-intercept of the linear regression model
    theta_1: the slope of the linear regression model
    The function returns the predicted values of the dependent variable, xes,
    under the linear regression model with y-intercept theta_0 and slope theta_1
    '''
    return None

def mse_loss(y_actual,y_estimate):
    '''
    y_actual: a Series containing numeric values.
    y_estimate: a Series containing numeric values.
    The series are of the same length and contain numeric values only
    (all null and non-numeric values have been dropped).
    The function returns the mean square error loss function between y_actual and y_estimate
    (e.g. the mean of the squares of the differences).
    '''
    total = 0
    for i in range(len(y_actual)):
        total += (y_actual[i] - y_estimate[i]) ** 2
    return total / len(y_actual)

def rmse_loss(y_actual,y_estimate):
    '''
    y_actual: a Series containing numeric values.
    y_estimate: a Series containing numeric values.
    The series are of the same length and contain numeric values only
    (all null and non-numeric values have been dropped).
    The function returns the square root of the mean square error loss function between
    y_actual and y_estimate (e.g. the square root of the mean of the squares of the differences)
    '''
    return mse_loss(y_actual,y_estimate) ** 0.5

def compute_error(y_actual,y_estimate,loss_fnc=mse_loss):
    '''
    y_actual: a Series containing numeric values.
    y_estimate: a Series containing numeric values.
    loss_fnc: function that takes two numeric series as input parameters and
    returns a numeric value. It has a default value of mse_loss.
    The series are of the same length and contain numeric values only
    (all null and non-numeric values have been dropped).
    The result of computing the loss_fnc on the inputs y_actual and y_estimate is returned.
    '''
    return loss_func(y_actual,y_estimate)

def compute_ytd(df):
    '''
    df: a DataFrame containing columns month, year and USINFO.
    The function returns a Series with the number of jobs since the
    beginning of the year for that entry. For example, for the January 2022 row,
    the number would be 0 since January is the beginning of the year.
    For July 2022, the number be the difference between USINFO for July and USINFO for January.
    '''
    return None

def compute_year_over_year(df):
    '''
    df: a DataFrame containing columns month, year and USINFO.
    Computes and returns a Series with the percent change from the previous year for USINFO.
    You can assume that the DataFrame is ordered by date,
    with earlier dates coming first in the DataFrame.
    Note: you may find the df.pct_change function useful for computing
    the change from the previous year.
    '''
    return None
