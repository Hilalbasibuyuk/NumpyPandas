import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=["a","b","e","h","g"],columns=["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","h","g"]) # yeni satırlar eklenir ama bu satırların içinde NaN yazılıdır.
result = df
result = df.drop("column1",axis=1) # column axis=1' dedir.Yani satır değil sütundur. Column1'i silen ifade budur.
result = df.drop(["column1","column2"],axis=1) #column1 ve column2 silinir

result = df.isnull() # NaN ifadesi boş olduğu için NaN olan yerlere True yazdırır.
result = df.notnull() # Yukarıdakinin tam tersi olarak NaN olan yerlere False yazdırır.
result =df[df["column1"].isnull()] # column1'de NaN olan yerleri getirir ama diğer sütunları da gösterir
result =df[df["column1"].isnull()]["column1"] #column1'de NaN olan yerleri getirir ve ssadece column1 sütununu gösterir

result = df.dropna() # NaN olan yerleri göstermez direkt dolu olan yerleri gösterir. Satır olarak
result = df.dropna(axis=1) # içi boşken satır olarak algıladığı için sütunu axis=1 diyerek sileriz.
result = df.dropna(how= "any") # Herhangi bir eksik değer içeren satırları/sütunları kaldırır (varsayılan)
result = df.dropna(how="all") # Tüm değerleri eksik olan satırları/sütunları kaldırır.
result = df.dropna(subset=["column1","column2"], how ="all") # subset belirli bir sütun kümesindeki eksik değerleri kontrol etmek için kullanılır
result = df.dropna(thresh=2) # En az 2 eksik değer içeren satırlar/sütunlar kaldırılır.
result = df.fillna(value="0") # NaN olan yerlere value'ye yazdığımız şeyi yazdırır

print(result)
