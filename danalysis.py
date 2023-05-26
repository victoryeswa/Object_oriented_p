#importing appropriate library
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#%matplotlib inline

#reading the dataset
fifa = pd.read_csv(r'WorldCups.csv')

print(fifa)

#showing the last ten record
print(fifa.tail(10))

#showing the first records of the dataset
print(fifa.head(5))

#finding the dimension of the dataset
print(fifa.ndim, 'ndim')

#showing the data types of the variable
print(fifa.dtypes, 'dtypes')

#using the info function
print(fifa.info())

#missing values 
