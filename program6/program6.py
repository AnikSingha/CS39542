"""
Name: Anik Singha
Email: anik.singha68@myhunter.cuny.edu
Resources: Hint on blackboard
"""

import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd

def import_data(file_name):
    '''
    file_name: the name of a CSV file containing Yellow Taxi Trip Data from OpenData NYC.
    The data in the file is read into a DataFrame, and
    the columns: VendorID,RatecodeID,store_and_fwd_flag,payment_type,extra,mta_tax,tolls_amount,
    improvement_surcharge,congestion_surcharge are dropped.
    Any rows with non-positive total_amount are dropped.
    '''
    df = pd.read_csv(file_name)
    df.drop(["VendorID","RatecodeID","store_and_fwd_flag","payment_type","extra","mta_tax",
            "tolls_amount","improvement_surcharge","congestion_surcharge"], axis=1, inplace=True)
    df = df[df["total_amount"] > 0]
    return df

def add_tip_time_features(df):
    '''
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    The function computes 3 new columns:
    percent_tip: which is 100*tip_amount/(total_amount-tip_amount)
    duration: the time the trip took in seconds.
    dayofweek: the day of the week that the trip started, represented as 0 for Mon, 1 for Tue, etc
    '''
    df["percent_tip"] = 100 * df["tip_amount"] / (df["total_amount"] - df["tip_amount"])
    df["time"] = pd.to_datetime(df["tpep_dropoff_datetime"]) - \
        pd.to_datetime(df["tpep_pickup_datetime"])
    df["duration"] = df["time"].dt.seconds
    df["dayofweek"] = pd.to_datetime(df["tpep_dropoff_datetime"]).dt.day
    return df

def impute_numeric_cols(df):
    '''
    : a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    Missing data in the numeric columns passenger_count,trip_distance,fare_amount,tip_amount,
    total_amount,duration,dayofweek are replaced with the median of the respective column.
    '''
    df = df.fillna(df.median())
    return df

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
    df2 = pd.read_csv(file_name)
    zones = df2[["LocationID", "borough"]]
    zones.rename(columns={"LocationID":"PULocationID", "borough": "PU_borough"}, inplace = True)
    df = df.merge(zones, left_on="PULocationID", right_on="PULocationID")
    zones = df2[["LocationID", "borough"]]
    zones.rename(columns={"LocationID":"DOLocationID", "borough": "DO_borough"}, inplace = True)
    df = df.merge(zones, left_on="DOLocationID", right_on="DOLocationID")
    return df


def encode_categorical_col(col, prefix):
    '''
    col: a column of categorical data.
    prefix: a prefix to use for the labels of the resulting columns.
    Takes a column of categorical data and uses categorical encoding to create a new DataFrame
    '''
    return pd.get_dummies(col, prefix, prefix_sep='', drop_first=True)


def split_test_train(df, xes_col_names, y_col_name, test_size=0.25, random_state=1870):
    '''
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC to
    which add_boro() has been applied.
    y_col_name: the name of the column of the dependent variable.
    xes_col_names: a list of columns that contain the independent variables.
    test_size: accepts a float between 0 and 1 and represents the proportion of the data set to
    use for training. This parameter has a default value of 0.25.
    random_state: Used as a seed to the randomization. This parameter has a default value of 1870.
    '''
    return train_test_split(df[xes_col_names], df[y_col_name], test_size, random_state)

def fit_linear_regression(x_train, y_train):
    '''
    x_train: an array of numeric columns with no null values.
    y_train: an array of numeric columns with no null values.
    Fits a linear model to x_train and y_train, using sklearn.linear_model.LinearRegression
    (see lecture & textbook for details on setting up the model).
    The resulting model should be returned as bytestream, using pickle (see Lecture 4)
    '''
    reg = LinearRegression().fit(x_train, y_train)
    return pickle.dumps(reg)

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
    mod = pickle.loads(mod_pkl)
    y_pred = mod.predict(xes)
    return mean_squared_error(y_pred,yes), r2_score(y_pred, yes)

def main():
    '''
    testing
    '''
    df = import_data('taxi_jfk_june2020.csv')
    df = add_tip_time_features(df)
    #print(df[ ['trip_distance','duration','dayofweek','total_amount','percent_tip'] ].head() )
    #print(df[ ['passenger_count','trip_distance'] ].head(10))
    df = impute_numeric_cols(df)
    #print( df[ ['passenger_count','trip_distance'] ].head(10))
    df = add_boro(df,'taxi_zones.csv')
    #print('\nThe locations and borough columns:')
    #print(f"{df[['PULocationID','PU_borough','DOLocationID','DO_borough']]}")
    df_do = encode_categorical_col(df['DO_borough'],'DO_')
    print(df_do.head())

if __name__ == "__main__":
    main()
