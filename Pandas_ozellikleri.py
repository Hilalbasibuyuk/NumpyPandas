import pandas as pd
import numpy as np

"""#Data oluşumu
numbers = [20,30,40,50]
letters = ["a","b","c","d"]
dictionary = {"a":"Ali","b":"Beyza", "c": "Ceren"}
random_numbers = np.random.randint(10,60,6)

pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series(dictionary) # Sözlük şeklinde çıktı verir sırasıyla
pandas_series = pd.Series(5,[1,2,3]) # sırayla 3 tane 5 yazar
pandas_series = pd.Series(random_numbers)

print(pandas_series)"""


"""#DataFrame oluşumu

s1 = pd.Series([2,6,9,7])
s2 = pd.Series([5,9,8,1])

data = dict( apples = s1 , orange = s2)

df = pd.DataFrame(data)
print(df)

liste = [["Ali",60],["Yağmur",45],["Çilem",90],["Akın",55]]
dict = {"Name": ["ALi", "Ayşe","Fatma","Gül"], "Scor": [80,90,99,100]}

datafm = pd.DataFrame(liste) #satır ve sütunlar şeklinde yazdırır
datafm = pd.DataFrame(liste, columns=["name", "Scor"],index=[1,2,3,4]) #columnlara isim verdik ve indexleri de biz belirledik
datafm = pd.DataFrame(dict , index=[255,256,257,258])
print(datafm)"""



