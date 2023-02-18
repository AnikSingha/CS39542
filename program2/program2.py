"""
    Name: Anik Singha
    Email: anik.singha68@myhunter.cuny.edu
    Resources: DS 100: Chapter 6 (DataFrames)
    https://mccray.jodymaroni.com/how-to-rename-multiple-column-headers-in-a-pandas-dataframe/
"""

#import pandas as pd

def clean_df(df, year = 2015):
    """
    Alters the columns of the dataframes to match
    the naming convecntion of the 2015 filset

    Keyword arguments:
        df - A datafram
        year - The year the data was collected form
    """
    columns = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'address',
                'zipcode', 'boroname', 'nta', 'latitude', 'longitude',
                'council_district', 'census_tract']
    if year == 1995:
        df = df[['diameter', 'condition', 'spc_latin', 'spc_common', 'address', 'zip_original',
                'borough', 'nta_2010', 'latitude', 'longitude', 'council_district',
                'censustract_2010']]
        df.rename(columns={"diameter":"tree_dbh", "condition":"health", "zip_original":"zipcode",
                    "borough":"boroname", "nta_2010": "nta", "censustract_2010": "census_tract"},
                    inplace = True)
    elif year == 2005:
        df = df[['tree_dbh', 'status', 'spc_latin', 'spc_common', 'address', 'zipcode',
                'boroname', 'nta', 'latitude', 'longitude', 'cncldist', 'census_tract']]
        df.rename(columns={"status":"health", "cncldist":"council_district"}, inplace=True)
    return df[columns]

def filter_health(df, keep):
    """
    Return the rows where the value of
    the item in the health column is in
    the keep array
    """
    return df[df["health"].isin(keep)]

def add_indicator(row):
    """
    Aggregate function that returns 1
    or 0 depending on whether a condition
    is met
    """
    val = 1 if (row["health"] != "poor" and int(row["tree_dbh"])) > 10 else 0
    return val

def find_trees(df, species):
    """
    Return the column address
    where the spc_latin column
    is equal to the species parameter
    """
    return list(df[df["spc_latin"] == species]["address"])

def count_by_area(df, area="boroname"):
    """
    Group by the area parameter
    and return the count
    """
    return df.groupby(area)[area].count()
