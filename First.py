import numpy as np
import pandas as pd
dict1={
    "Name":['harsh','sachin','rohoti','suman'],
    "Marks":[92,34,34,23],
    "City":['delhi','mumbai','pune','banglore']
}
#print(dict1)
#Creating DataFrame from dictionary in pandas and showing it in excel format
df=pd.DataFrame(dict1)
print(df)
#Saving DataFrame to csv file
df.to_csv('friends.csv')
#Saving DataFrame to csv file without index
df.to_csv('friends_index_False.csv',index=False)
#head is used to show first n rows of dataframe/data in your csv file .
#tail is used to show last n rows of dataframe
df.head(2)#To show first two rows of dataframe
df.tail(2)#To show last two rows of dataframe
print(df.head(2))
df.describe()#To show statistical summary of dataframe
print(df.describe())
