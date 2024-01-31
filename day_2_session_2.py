# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:35:23 2024

@author: chris

Doing ETL
"""

import pandas as pd

df = pd.read_csv("country_data_index.csv", index_col=0)  # using index column removes the python index column
# print(df)

df1 = pd.read_excel("residentdoctors.xlsx")

# Regular expressions
df1["lower_age"] = df1["AGEDIST"].str.extract("(\d+)-")  # (\d+) indicates 1st number; - with this indicates 1st number before hyphin
df1["upper_age"] = df1["AGEDIST"].str.extract("-(\d+)")

df1["lower_age"] = df1["lower_age"].astype(int)  # this overwrites the new column which is a string, with the same values but as integers

# print(df1.info())

"""
Working with dates

10-01-2024 - UK

01-10-2024 - US


"""

dates = pd.read_csv("time_series_data.csv",index_col=0)  # Most cases, dates are pulled in as a string
dates["Date"] = pd.to_datetime(dates["Date"])  # pandas has built in functionality to convert string to date format
dates["Year"] = dates["Date"].dt.year  # .dt function that allows for modification of dataframe

# print(dates.info())

df = pd.read_csv("patient_data_dates.csv",index_col=0)
df.drop(index=26, inplace=True)  # can remove rows of data
# df["Date"] = pd.to_datetime(df["Date"],format="mixed")  # format = "mixed" allows python to interpret dates in the same set which are formatted differently
df["Date"] = pd.to_datetime(df["Date"])
avg_cal = df["Calories"].mean()
# df["Calories"].fillna(avg_cal, inplace=True)  # putting the average value in places where no value was recorded
print(df)
print(df.info())

"""
Best Practices
"""

df.dropna(inplace=True)  # can remove a row where a nan exists
df.reset_index(drop=True)  # reset index to be sequential after dropping values
# df.loc[7,"Duration"] = 45  # replace data at a certain location with a value
df["Duration"] = df["Duration"].replace([450],45)  # replace any 450 in duration with 45
print(df)