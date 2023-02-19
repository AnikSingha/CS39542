"""
    Name: Anik Singha
    Email: anik.singha68@myhunter.cuny.edu
    Resources:
"""

import pandas as pd
import numpy as np

def make_dog_df(license_file,zipcode_file):
    '''
    license_file: the name of a CSV file containing NYC Dog Licensing Data from OpenData NYC, and
    zipcode_file: the name of a CSV file containing BetaNYC's NYC Zip Codes by Borough.
    The names of the dogs AnimalName should be capitalized.
    The columns, 'LicenseExpiredDate', 'Extract Year' should be dropped.
    The two DataFrames should be (left) merged on zipcodes.
    Any reported dogs not in NYC (i.e. have NaN for Borough in the combined DataFrame)
    should be dropped.
    '''
    df = pd.read_csv(license_file)
    df2 = pd.read_csv(zipcode_file)
    df["AnimalName"] = df["AnimalName"].str.capitalize()
    df = df.drop(["LicenseExpiredDate","Extract Year"], axis=1)
    df2 = df2.drop(["post_office","neighborhood","population","density"],axis=1)
    result = df.merge(df2, left_on="ZipCode", right_on="zip", how="left")
    result.drop("zip",axis=1,inplace=True)
    result.rename(columns={"borough":"Borough"}, inplace=True)
    result = result.dropna()
    return result

def make_bite_df(file_name):
    '''
    The function should open the file file_name as DataFrame,
    dropping the Species column. The resulting DataFrame is returned.
    '''
    df = pd.read_csv(file_name)
    df.drop("Species",axis=1,inplace=True)
    return df


def clean_age(age_str):
    '''
    age_str: a string containing the age of the dog.
    If age_str ends in a Y, return the rest of the string as a number.
    For example, 3Y represents 3 years and the return value is 3.
    If age_str ends in a M, return the rest of the string as a number in years.
    For example, 6M represents 6 months and the return value is 0.5.
    If age_str contains only a number, return it as a number.
    For example, 3 represents 3 years and the return value is 3.
    For all other values, return None.
    '''
    if age_str[-1] == "Y":
        return float(age_str[:len(age_str)-1])
    elif age_str[-1] == "M":
        return float(age_str[:len(age_str)-1]) / 12
    elif len(age_str) == 1:
        return float(age_str)
    return None


def clean_breed(breed_str):
    '''
    breed_str: a string containing the breed of the dog.
    If breed_str is empty, return "Unknown".
    Otherwise, return the string in title format with each word in the string
    capitalized and all other letters lower case. For example, If the input is
    BEAGLE MIXED, you should return Beagle Mixed.
    '''
    if len(breed_str) == 0:
        return "Unknown"
    return breed_str.title()


def impute_age(df):
    '''
    df: a DataFrame containing the column Age Num.
    Your function should replace any missing values in the df['Age Num'] column
    with the median of the values of the column. The resulting DataFrame is returned.
    '''
    df["Age Num"] = df["Age Num"].fillna(df["Age Num"].median())
    return df


def impute_zip(boro, zipcode):
    '''
    boro: a non-empty string containing the borough.
    zipcode: a possibly empty string containing the zip code.
    If the zipcode column is empty, impute the value with the zip code of the general
    delivery post office based on value of boro: 10451 for Bronx, 11201 for Brooklyn,
    10001 for Manhattan, 11431 for Queens, 10341 for Staten Island, and None for Other.
    '''
    codes = {"Bronx": "10451", "Brooklyn": "11201", "Manhattan": "10001", "Queens": "11431",
            "Staten Island": "10341", "Other": None}
    if np.isnan(zipcode):
        return codes[boro]
    return zipcode

def parse_datetime(df, column='LicenseIssuedDate'):
    '''
    df: a DataFrame containing the column column. column has a default value of 'LicenseIssuedDate'
    timestamp: contains the datetime object corresponding to the string stored in column.
    month: return the number corresponding to the month of timestamp: 1 for January, 2 for February
    day_of_week: return the number corresponding to the day of the week of timestamp: 0 for Monday
    '''
    df["timestamp"] = pd.to_datetime(df[column])
    df["month"] = df["timestamp"].dt.month
    df["day_of_week"] = df['timestamp'].dt.day_of_week
    return df

def main():
    '''
    dog_df = make_dog_df("NYC_Dog_Licensing_Dataset_2021.csv",
                        "nyc_zip_borough_neighborhoods_pop.csv")
    dog_df = parse_datetime(dog_df)
    print(dog_df)
    print('Most popular names are:')
    print(dog_df['AnimalName'].value_counts()[:10])
    bite_df = make_bite_df("DOHMH_Dog_Bite_Data_2021.csv")
    print(bite_df)
    df_drop = bite_df.dropna()
    print(f'The full DataFrame has {len(bite_df)} entries.')
    print(f'Dropping undefined values leaves {len(df_drop)} entries.')
    bite_df = impute_age(bite_df)
    bite_df['ZipCode'] = bite_df.apply(lambda row: impute_zip(row['Borough'],row['ZipCode']),axis=1)
    print(bite_df)
    '''
    bite_df = make_bite_df("DOHMH_Dog_Bite_Data_2021.csv")
    bite_df['ZipCode'] = bite_df.apply(lambda row: impute_zip(row['Borough'],row['ZipCode']),axis=1)
    print(bite_df)

if __name__ == "__main__":
    main()
