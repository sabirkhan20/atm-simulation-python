# lets start num.py from  here 

# l1=[1,2,3]
# l2=[4,5,6]

# using list



# print(list(zip(l1,l2)))  #zip function of list
# import time

# size=1_0000_00
# l1=np.array(list(range(size)))
# l2=np.array(list(range(size)))
# start=time.time()
# add=l1+l2
# end=time.time()
# print(end-start)

# making array


# import numpy as np


# import numpy as np
# Creating a 1D NumPy array
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
# # Creating a 2D NumPy array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)
# # Checking type and shape
# print("Type:", type(arr1))
# print("Shape:", arr2.shape)

 
# arr=np.array([[1,2,3,4],[2,34,212,2]])
# print(type(arr))


# creating zeroes arrays

# arr= np.zeros([3,4]) #its 2 d array
# print(arr)

# arr=np.ones([4,3])
# print(arr)


# arr=np.full([3,3],7)
# print(arr)

# arr=np.eye(3)
# print(arr.shape)

# arr=np.arange(1,100,2)
# print(arr)


# arr=np.linspace(0,100,5)
# print(arr)



# myarr=np.array([[[1,2,3],[4,5,6],[7,8,9]]]),dtype='flost32'
# print(myarr)
# print('the shape of my arr is',myarr.shape)
# print('the size of my arr is',myarr.size)
# print('dimensions of my arr is ',myarr.ndim)
# print('data type of my arr is',myarr.dtype) 

# import numpy as np

# myarr = np.array(
#     [[[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]],
#     dtype='float32'
# )

# print(myarr)



# indexing and slicicng using numpy

# arr=np.array([[[1,2,3,],[4,5,6,],[7,8,9],[11,12,13]]])
# # print(arr.ndim)

# flat=arr.flatten()
# print(flat) #to make given array in 3d to 1d
# print(flat.ndim)

# print(flat[0:6]) #indeing k liye 
# print(flat[:6]) #same as 0:6
# print(flat[:13])#same as [0:13]
# print(flat[3:13])#same as 
# print(flat[::2])#every second element

# b=(flat[3:7])# isme copy laga denge to flat m koi bhi change nhi aayga 
# print(b)
# (b[0])=984
# # print(b[0])
# print(b)
# print(flat)


# arr=np.array([1,54,23,53,2,3,34,5,6])
# print(arr)

# print(arr>3)


# indexing in multidimensional array

# arr=np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# print(arr)

# print('the sum of column is',np.sum(arr,axis=0))
# print('the sum of row is',np.sum(arr,axis=1))

# print(arr[1,2])
# print(arr[0,0])

# print(arr[0:2,1:3])

# arr3d=np.array([[[1,2,3,],
#                 [4,5,6],
#                 [10,11,12]]])
# print(arr3d.ndim)

# print(arr3d[0,1,2])# 





# data types in numpy

# arr=np.array([23,4,3,23])
# print(arr.dtype)
# print(arr.nbytes)





# # broadcasting in numpy
# arr=np.array([1,2,3,4,5])
# print(arr+10)# isme array update ho jyga


# arr=np.array([1,2,3,])
# arr2=np.array([2,3,4])
# print(arr+arr2)


# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# arr1 = np.array([1,2,3])
               
                 

# print(arr + arr1)
        


# # Simulating a dataset (5 samples, 3 features)
# data = np.array([[10, 20, 30],
# [15, 25, 35],
# [20, 30, 40],
# [25, 35, 45],
# [30, 40, 50]])
# # Calculating mean and standard deviation for each feature (column)
# mean = data.mean(axis=0)
# std = data.std(axis=0)
# # Normalizing the data using broadcasting
# normalized_data = (data - mean) / std
# print(normalized_data)




# pandas start from here 

import pandas as pd

# a=pd.Series([1,2,3])
# print(a)

#giving indexes ye ek 1 d array h 

# A1 = pd.Series(['harry','sabir','riya'], index=[50,70,80])
# # print(A1)
# print(A1[A1 == 'sabir'])


# creating data frame using dict 

# data={
#     'name':['charlie','bob','alice'],
#     'age':[20,20,23],
#     'city':['newyork','bigben','abudhabi']
# }
# print(pd.DataFrame(data))

# creating data frame using list

# data=[['harry','34'],['bill',90],['sabir',90],['gaurav',98]]
# print(pd.DataFrame(data,columns=['name','marks']))


#  making data frame using num py
# import numpy as np
# arr=np.array([[1,2],[5,6]])
# df=(pd.DataFrame(arr))
# print(df)




# reading excel data using pandas without opening excel

# a=pd.read_excel('data.xlsx')
# print(a)

# df.head()
# df.tail()
# df.info()
# df.describe()
# df.columns        
# df.shape          
# First 5 rows
# Last 5 rows
# Column info: types, non-nulls
# Stats for numeric columns
# List of column names
# (rows, columns)

import pandas as pd


# actual data analysis using pandas 
data = {
    "Movie": [
        "3 Idiots", "Dangal", "KGF Chapter 1", "Bahubali 2",
        "PK", "Gully Boy", "RRR", "Drishyam"
    ],
    "Actor": [
        "Aamir Khan", "Aamir Khan", "Yash", "Prabhas",
        "Aamir Khan", "Ranveer Singh", "Ram Charan", "Ajay Devgn"
    ],
    "Genre": [
        "Comedy-Drama", "Sports-Drama", "Action", "Action-Fantasy",
        "Comedy-Drama", "Musical-Drama", "Action-Drama", "Thriller"
    ],
    "Release_Year": [
        2009, 2016, 2018, 2017, 2014, 2019, 2022, 2015
    ],
    "IMDB": [
        4.6, 5.8, 6.3, 6.9, 7.4, 8.1, 9.2, 9.7

    ],
    "Collection_Cr": [
        460, 2000, 250, 1800, 850, 240, 1200, 220
    ]
}

df = pd.DataFrame(data)
# print(df)

# print(df['Actor']) selecting a particular column 
# print(df['Genre'][1]) selecting something specific fromm column

# print(df[['IMDB',"Actor",'Genre',"Collection_Cr"]]) selecting multiple column

# print(df.loc[0])  accesing a specific row

# print(df.iloc[0]) acceseing a specific row by by indexng

# print(df.loc[7,'Actor']) accessing a specific index iska matlab 7 num p kunsa actor h 

# print(df.iloc[7,5])

# print(df.loc[0:5,['Actor','IMDB']]) accesing unique from 

# print(df.at[0,'Genre'])  accesing one specifc elemnt 

# print(df['IMDB']>6) filtering the data

# print(df[df['IMDB'] > 7]['Actor']) extra filter

# print(df.loc[(df['IMDB'] > 6) & (df['Release_Year'] > 2016)])


# print(df.query('Release_Year>2016'))

# print(df.query('Release_Year > 2016 & IMDB > 6'))



# data cleaning and preprocessing usning pandas


data2 = {
    "Emp_ID": [101, 102, 103, 104, 105, 103, 106, 102],
    "Name": ["Rahul", "Anita", "Aman", "Pooja", "Rakesh", "Aman", "Neha", "Anita"],
    "Age": [25, 28, 30, None, 45, 30, None, 28],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female"],
    "Department": ["IT", "HR", "IT", "Finance", "Management", "IT", "HR", "HR"],
    "Joining_Date": [
        "2021-06-15",
        "2020-01-10",
        None,
        "2019-11-23",
        "2018-05-01",
        None,
        "2022-03-18",
        "2020-01-10"
    ],
    "Salary": [35000, 42000, None, None, 70000, None, 38000, 42000]
}


df=pd.DataFrame(data)
# print(df.isnull()) to finding null value between
# print(df.isnull().sum()) getting sum  of null values 
# print(df.dropna()) it will remove all null row and column
# print(df.dropna(axis=1)) drop all column of null constrain
# print(df.fillna(0)) value enter karna 
# print(df['Age'].fillna(df['Age'].mean())) average value insert in place of na 
# print(df.duplicated()) row m check karna same  h ya duplicate h 
# print(df['Age'].fillna(0).astype(int))

# sorting data

import pandas as pd

data_sort = {
    "Emp_ID": [105, 102, 108, 101, 104, 102, 107, 103],
    "Name": ["Rakesh", "Anita", "Pooja", "Rahul", "Aman", "Anita", "Neha", "Aman"],
    "Age": [45, 28, None, 25, 30, 28, None, 30],
    "Department": ["Management", "HR", "Finance", "IT", "IT", "HR", "HR", "IT"],
    "Salary": [70000, 42000, None, 35000, 50000, 42000, 38000, None],
    "Joining_Date": [
        "2018-05-01",
        "2020-01-10",
        "2019-11-23",
        "2021-06-15",
        "2020-08-12",
        "2020-01-10",
        None,
        "2021-03-18"
    ]
}

df = pd.DataFrame(data_sort)
# print(df)
# print(df.sort_values(['Salary']))
# print(df.sort_values(['Emp_ID','Age','Salary']))
# print(df.reset_index())
  




import requests

a = requests.get('https://books.toscrape.com/')

with open('html/page1.html', 'r', encoding='utf-8') as f:
    data = f.read()

print(data)
