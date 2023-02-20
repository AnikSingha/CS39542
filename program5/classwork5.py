import pandas as pd 

df = pd.read_csv("fred_info_2022_5yr.csv")

df.reset_index(inplace=True)

# df["USINFO"] -> yes

# df["index"] -> xes

sd_y = df["USINFO"].std()

sd_x = df["index"].std()

# df["USINFO"].corr(df["index"]) -> this gives the pearson's correlation coefficent

r = 0.657658

theta_1 = r * sd_y / sd_x # slope of the linear regression line 

theta_0 = df["USINFO"].mean() - (theta_1 * df["index"].mean()) # y-intercept 

