# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:28:27 2024

@author: chris
"""

import pandas as pd

df = pd.read_csv("iris.csv")
df1 = pd.read_csv("person_split1.csv")
df2 = pd.read_csv("person_split2.csv")

col_names = df.columns.tolist()

df["sepal_length_sq"] = df["sepal_length"]**2  # can work on simple examples
df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)  # more broadly applicable

grouped = df.groupby("class")  # class is a descriptive column in the dataframe
mean_square_values = grouped["sepal_length_sq"].mean()  # can then perform a calculation on the different groupings within the dataframe individually
# print(mean_square_values)

dfcomb = pd.concat([df1, df2], ignore_index=True)  # combine different dataframes together
# ignore index = true allows the index to continue counting from the 1st dataframe to the 2nd

df3 = pd.read_csv("person_education.csv")
df4 = pd.read_csv("person_work.csv")  # dataframes related by a ID (name, number, etc.) but contain different data about that ID
df_merge_inner = pd.merge(df3, df4, on="id")  # matches only if ID is in both files
df_merge_outer = pd.merge(df3, df4, on="id", how="outer")  # returns all IDs, where there is no match, NaN is reported for missing data

df["class"] = df["class"].str.replace("Iris-","")  # removes Iris- from the class column
# print(df)

values_5_up = df[df["sepal_length"]>5]  # filter by certain attribute
values_5_up = df[df["class"]=="virginica"]  # filter by class

df.to_csv("iris_cleaned.csv")  # exports the cleaned dataframe as a csv in the folder where the python code is located

pulsar = pd.read_csv("https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv")
