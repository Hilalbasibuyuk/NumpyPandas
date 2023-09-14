import pandas as pd

customers = {
    'CustomersID': [1,2,3,4],
    'FirstName':["Ali","Ayşe","Hilal","Tolga"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    'OrderID': [10,11,12,13],
    'CustomersID': [1,2,5,7],
    'OrderDate': ["2010.07.04","2011.07.17","2000.08.04","2020.04.25"]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

result = pd.merge(df_customers,df_orders,how="inner") # Ortak column bilgileri gelir
result = pd.merge(df_customers,df_orders,how="left") # soldaki (df_customers) bilgileri tam gelir diğeri ile birleşir. Ortak olmayan yerlere NaN yazısı gelir
result = pd.merge(df_customers,df_orders,how="right") # sağdaki (df_orders) bilgileri tam gelir diğeri ile birleşir. Ortak olmayan yerlere NaN yazısı gelir
result = pd.merge(df_customers,df_orders,how="outer") #ortak olsa da olmasa da tüm bilgiler birleşmiş şekilde gelir

customersA = {
    'CustomersID': [1,2,3,4],
    'FirstName':["Ali","Ayşe","Hilal","Tolga"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomersID': [4,5,6,7],
    'FirstName':["Aliye","Alp","eren","ela"],
    'LastName': ["tuncay","buket","Çelik","Yaprak"]
}

df_customersA = pd.DataFrame(customersA)
df_customersB = pd.DataFrame(customersB)
result = pd.concat([df_customersA,df_customersB]) # concat ile listeleri birleştirmiş oluruz
result = pd.concat([df_customersA,df_customersB],axis=1) # listeleri yan yana birleştirme işlevini yapar

print(result)