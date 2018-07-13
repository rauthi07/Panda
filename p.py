#Q1
'''import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Name': ['sohan', 'mohan', 'rohan'],
    'Age':[21, 20, 19],
    'MailID': ['sohan111@gmail.com','mohan222@gmail.com','rohan333@gmail.com'],
    'Phone Number' : [9988787898,9999998877,8888987654]})
print(df)'''


#Q2
'''import pandas as pd
import numpy as np
df=pd.read_csv("File.csv")
print("A.First Five rows of Dataframe")
print(df.head())
print("B.First 10 rows of Dataframe")
print(df.head(10))
print("C.Some statistics Function On This DataFrame")
print("1.Sum:\n",df.sum())
print("2.Row Wise Sum:\n",df.sum(1))
print("3.Mean:\n",df.mean())
print("4.Standred Daviation:\n",df.std())
print("5.variance:\n",df.var())
print("6.Summarizing the data:\n",df.describe())
print("D.Last 5 rows of Dataframe")
print(df.tail())
df1 = df[df.columns[1]]
print("Some Statistics function on these 2nd column:\n")
a=df1.describe(include=['object'])
print(a)'''