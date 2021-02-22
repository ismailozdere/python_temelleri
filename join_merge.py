import pandas as pd

customer = {
    "customerId": [1,2,3,4] ,
    "firstName" : ["ahmet","ali" ,"hasan" , "canan"],
    "lasttName" : ["yılmaz","korkmaz" ,"çelik" , "toprak"]

    }

orders ={
    "orderId" : [10,11,12,13],
    "customerId": [1,2,5,7],
    "orderDate" : ["2010-07-05" , "2010-09-16", "2010-04-13" ,"2010-02-18"]
}

df_customers= pd.DataFrame(customer, columns = ["customerId" , "firstName", "lasttName" ])
df_orders=pd.DataFrame(orders , columns = ["orderId" , "customerId" , "orderDate"])


print(df_customers)
print(df_orders)


result=pd.merge(df_customers,df_orders ,how="inner")

print(result)





















