import pandas as pd
import numpy as np
from numpy.random import randn

"""df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns= ["columns1", "columns2","columns3"])
result = df.loc["A"] #loc indexi A olan satırları verdi
df["Columns4"] =pd.Series(randn(3),["A","B","C"]) # yeni bir column ekleme işlemi
result = df.drop("Columns4", axis=1) # column silme işlevi
result = df.drop("Columns4", axis=1, inplace=False) #İnplace true olursa değişiklikleri kaydetmiş oluruz orijinalinde de silinir
print(df)
print(result)"""

"""#DataFrame Filtreleme

data = np.random.randint(10,100,75).reshape(15,5)
df =pd.DataFrame(data,columns=["column1","column2","column3","column4","column5"])
result =df
result=df.head()#ilk 5 satırı
result=df.head(10)#ilk 10 satırı
result=df.tail()#son 5 satırı
result=df.tail(10)#son 10 satırı
result=df["column1"].head() #column1 gösterilir ve ilk 5 satır. df.column1.head() -> böyle de yazılabilir
result=df[["column1","column2"]].head() # column1 ve column2'nin ilk 5 tanesi gösterişir
result=df[5:15][["column1"]]# 5 ve 15 arası colum1 gösterilir

result = df > 50 #50'den büyük olanlar için True küçükler için False değerlerini döndürür
result = df[df > 50] # true false yerine direkt 50'den büyük değerleri döndürür. Küçüklere NaN yazılmış olur
result =df[(df["column1"]>50) & (df["column2"]<20)]
result =df.query("column1>80 & column3 <=30") #koşul ifadesi

print(result)"""


"""#DataFrame ile groupby kullanımı
personeller = {
    "Çalışan": ["Ahmet","Alp","Hilal","Ela"],
    "Departman" : ["İnsan kaynakları","Bilgi işlem","Muhasebe","İnsan kaynakları"],
    "Yaş": [45,25,32,29],
    "Semt": ["Yenişehir","Yıldızkent","Eminönü","Kadıköy"],
    "Maaş": [5000,3600,9500,4200]
}

df = pd.DataFrame(personeller)
result = df
result = df["Maaş"].sum() # maaşlar toplamını verir
result = df.groupby("Semt").groups # Semttekileri indexleri ile beraber gösterir
result = df.groupby(["Çalışan","Departman"]).groups

for name,group in df.groupby("Semt"):
    print(name) # Semt adını yazar
    print(group) # O semttekilerin bilgisini girer

for name,group in df.groupby("Departman"):
    print(name)
    print(group)

result=df.groupby("Departman").get_group("İnsan kaynakları") # departmanı insan kaynakları olan kişileri getir.
result = df.groupby("Departman").sum() # aynı departmandakilerin maaş ve yaşlarının toplamını verir.
result = df.groupby("Departman").mean() # aynı departmandakilerin maaş ve yaşlarının ortalamasını verir.
result = df.groupby("Departman")["Çalışan"].count() # departmana göre çalışanların sayısını verir
result = df.groupby("Departman").agg(np.sum) # aynı departmandakilerin maaş ve yaşlarının toplamını verir.
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.max,np.min]) # departmana göre maaşların toplamını, max'ını ve min'ini verir


print(result)"""

# DataFrame Metotları
data = {
    "column1" : [1,2,3,4,5],
    "column2" : [10,20,30,40,10],
    "column3" : ["abs","ald","abc","dke","aws"]
}
df = pd.DataFrame(data)

result =df
result = df["column2"].unique() # Column2'de tekrar edenleri almayarak liste haline getirir.
result = df["column2"].nunique() # Yukarıda oluşan listede kaç eleman olduğunu gösterir
result = df["column2"].value_counts() # Listedeki elemanlardan kaçar tane olduğunu gösterir
result =df.sort_values("column2") #sıralar
result =df.sort_values("column3")
result =df.sort_values("column3",ascending=False) # Ters olarak sıralar

def kareAl(x):
    return x * x
result = df["column1"].apply(kareAl) # apply fonksiyonu uygular 

print(result)