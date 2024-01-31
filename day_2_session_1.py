# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:36:36 2024

@author: chris
"""

# Day 2 Python - More examples of importing data

import pandas as pd

df = pd.read_csv("iris.csv")

"""
Can copy file paths from the file explorer in spyder (absolute or relative)
absolute - C:/Users/chris/OneDrive - University of Cape Town/PhD/Coding Summer School/Day 2/Day 2/iris.csv
relative - iris.csv
"""

"""
can call data from online as well
    just provide url for data
"""
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, header=None, names=columns)

# Reading different data types
text = pd.read_csv("Geospatial Data.txt", sep=";")  # txt

excel = pd.read_excel("residentdoctors.xlsx")  # xlsx

json = pd.read_json("student_data.json")  # json

dfnew = pd.read_csv("Accelerometer_data.csv", header=None, names = ["date_time", "x", "y", "z"])

