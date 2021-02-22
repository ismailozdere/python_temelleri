import pandas as pd
import numpy as np

data =np.random.randint(10,100,75).reshape(15,5)
df= pd.DataFrame(data,columns= ["column1","column2","column3","column4","column5"])

result=df

result=df.columns
result=df.head()
result=df.head(10)
result=df.tail()
result=df.tail(10)
result= df["column1"].head()

print(result)
result=df > 50
result=df [df % 2 == 0 ]

result=df[df["column1"] > 50] [["column1","column2"]]
result=df[( df["column2"]> 50 ) & (df["column1"] <= 70)]
result=df[( df["column2"]> 50 ) | (df["column1"] <= 70) ]
result=df[( df["column2"]> 50 ) | (df["column1"] > 50) ][["column1","column2"]]

result=df.query("column1 >= 50 & column1 % 2 == 0")




# print(result)





