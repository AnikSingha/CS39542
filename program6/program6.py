"""
Name: Anik Singha
Email: anik.singha68@myhunter.cuny.edu
Resources:
"""

import pandas as pd

def import_data(file_name):
    '''
    file_name: the name of a CSV file containing Yellow Taxi Trip Data from OpenData NYC.
    The data in the file is read into a DataFrame, and
    the columns: VendorID,RatecodeID,store_and_fwd_flag,payment_type,extra,mta_tax,tolls_amount,
    improvement_surcharge,congestion_surcharge are dropped.
    Any rows with non-positive total_amount are dropped.
    '''

def add_tip_time_features(df):
    '''
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    The function computes 3 new columns:
    percent_tip: which is 100*tip_amount/(total_amount-tip_amount)
    duration: the time the trip took in seconds.
    dayofweek: the day of the week that the trip started, represented as 0 for Mon, 1 for Tue, etc
    '''

def impute_numeric_cols(df):
    '''
    : a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    Missing data in the numeric columns passenger_count,trip_distance,fare_amount,tip_amount,
    total_amount,duration,dayofweek are replaced with the median of the respective column.
    '''

def add_boro(df, file_name):
    '''
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    file_name: the name of a CSV file containing NYC Taxi Zones from OpenData NYC.
    Makes a DataFrame, using file_name, to add pick up and drop off boroughs to df.
    In particular, adds two new columns to the df:
    PU_borough that contain the borough corresponding to the
    pick up taxi zone ID (stored in PULocationID), and
    DO_borough that contain the borough corresponding to the
    drop off taxi zone (stored in DOLocationID)
    '''

def encode_categorical_col(col,prefix):
    '''
    col: a column of categorical data.
    prefix: a prefix to use for the labels of the resulting columns.
    Takes a column of categorical data and uses categorical encoding to create a new DataFrame
    '''

def split_test_train(df, xes_col_names, y_col_name, test_size=0.25, random_state=1870):
    '''
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC to which add_boro() has been applied.
    y_col_name: the name of the column of the dependent variable.
    xes_col_names: a list of columns that contain the independent variables.
    test_size: accepts a float between 0 and 1 and represents the proportion of the data set to
    use for training. This parameter has a default value of 0.25.
    random_state: Used as a seed to the randomization. This parameter has a default value of 1870.
    '''

def fit_linear_regression(x_train, y_train):
    '''
    x_train: an array of numeric columns with no null values.
    y_train: an array of numeric columns with no null values.
    Fits a linear model to x_train and y_train, using sklearn.linear_model.LinearRegression
    (see lecture & textbook for details on setting up the model).
    The resulting model should be returned as bytestream, using pickle (see Lecture 4)
    '''

def predict_using_trained_model(mod_pkl, xes, yes):
    '''
    mod_pkl: a trained model for the data, stored in pickle format.
    xes: an array or DataFrame of numeric columns with no null values.
    yes: an array or DataFrame of numeric columns with no null values.
    Computes and returns the mean squared error and r2 score between the values
    predicted by the model (mod_pkl on x) and the actual values (y).
    Note that sklearn.metrics contains two functions that may be of use:
    mean_squared_error and r2_score.
    '''

def main():
    '''
    testing
    '''

if __name__ == "__main__":
    main()
