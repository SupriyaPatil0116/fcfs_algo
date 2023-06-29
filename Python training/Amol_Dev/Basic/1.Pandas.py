

# importing the pandas

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

print('#'*40)

#########################################
# you can write the above code as below:
# here we have imported pandas as pd
#Pandas is usually imported under the pd alias.
#alias: In Python alias are an alternate name for referring to the same thing.
#Create an alias with the as keyword while importing:

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# you can check the pandas version by using below line of code.
print(pd.__version__)
print(myvar)

print('#'*40)

"""

1. How to declare series using pandas
2. How to create the labels for the series content
3. How to create the pandas series from the content of the dictionary

"""

# No. 1 a series in the pandas is like column in a table

print("No.1 In the pandas a series is like column in the table.")
a = [1, 7, 2]

my_series = pd.Series(a)

print(my_series)

print('#'*40)




# you can assign the labels to the index in the series in the python

print ("to assign the label to the index in the series use index[]")

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

# here the index of the series has been changed to the string x,y,z instead of 0,1,2
print(myvar)


print('#'*40)

#You can also use a key/value object, like a dictionary, when creating a Series.
print("In order to display the content of the dictionary you can simply use the pandas sereis to display it.")

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

my_di_series=pd.Series(calories,index=["day3"])
print(myvar)
print(my_di_series)

print('#'*40)


#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.

print("In pandas , you can create the two-dimensional, three dimnesional or multidimensional tables \n which are also called as DataFrames")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print("Using the Dataframe structure you can create table 3x3,4x4 depending on your requirement.")

smart_watch_data={
    "Calories":[100,120,200,300],
    "Time":[10,12,20,30],
    "Activity":['Swimming','running','walking','jumping']
  }

myvar = pd.DataFrame(smart_watch_data)
print(myvar)

# if you want to locate the data from this data frame you can use the locator Loc[] function
# in which you pass on the index you want from the column, 3x3 dataframe or 4x4 data frame and pass that data to the

print("Locate Row")

data = {0,1,2,3,4,5}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#refer to the row index:
print(df.loc[1])

#if you want to display list of  indexes of  row

print(df.loc[[1,2]])
print('#'*40)

# similary if you got the data which is having more row and column or say 4x4 grid
# if you want to display 2x2 grid out of it you can use indexing method

"""
Step 1- Write down the data
step 2- target the index that you want to display
step 3- load that data into data frame object
step 4- apply locators to the Data frame object and then display the data.
"""
print("Displaying Indexing method for Bigger Dataframe")


motorcycle_data=\
    {
    "Motorcycle Name":["Honda Unicorn","Yamaha Fz-s","Royal Enfield-Hunter","Tvs Ronin"],
    "Engine in cc":[160,150,350,225],
    "Mileage":[52,45,37,40],
    "Type":['Commuter','Street','Cruiser','Cruiser+']
    }

df= pd.DataFrame(motorcycle_data)


#df = pd.Series(motorcycle_data, index ={"Motorcycle_1", "Motorcycle_2", "Motorcycle_3", "Motorcycle_4"})

# dataframe object= pandas extension (pd) dataframe function () and input data
print(df)

# to display the 0th data in the DataFrame use locator 0
print(df.loc[0])
# to diplay the Multiple data in the DataFrame use Locator [[0,1]],[[0,1,2]]
print(df.loc[[0,1]])

# While in the reverse way you can show the index of the Particular element
# you can trace the location of the required string or data

df = pd.DataFrame(motorcycle_data, index = ["Motorcycle_1", "Motorcycle_2", "Motorcycle_3", "Motorcycle_4"])
print(df)


