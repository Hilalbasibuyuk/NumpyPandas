import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy list
np_list = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list)) # çıktısı: <class 'list'>
print(type(np_list)) # çıktısı: <class 'numpy.ndarray'>

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_list.reshape(3,3) # 3'e 3'lük matris yapar

print(np_list.ndim) # ndim boyut bilgisini verir (1)
print(np_multi.ndim) # bu da iki boyutlu 3*3 matris olduğu için

print(np_list.shape) # çıktısı: (9,)
print(np_multi.shape) # çıktısı: (3,3)

result = np.arange(1,10) #1'den 9'a kadar yazdırır
result = np.arange(1,100,3) # 1'den 100'e kadar 3'er 3'er yazdırır
result = np.linspace(0,100,5) # çıktısı: [  0.  25.  50.  75. 100.] 
result = np.random.randint(1,10) #1 9 (9 dahil) arasında rastgele bir sayı verir
result = np.random.randint(1,10,3) # rastgele 3 sayı verir
result = np.random.rand(5) # 0-1 arasında rastgele 5 sayı verir
result = np.random.randn(5) # hem negatif hem pozitif sayı verir
print(result)

np_array = np.arange(50)
np_muti = np_array.reshape(5,10) # 5 satır 10 sütun haline getirir
print(np_muti.sum(axis=0)) # sütunların toplamını verir
print(np_muti.sum(axis=1)) # satırların toplamını verir

print(np_array.mean()) # oluşturulan sayıların ortalamasını verir mean metodu

dizi = np.random.randint(1,100,6)
dizi2 = np.random.randint(1,100,6)

result1 = np.sin(dizi)
result1 = np.log(dizi)
result1 = np.sqrt(dizi)
print(result1)

mdizi = dizi.reshape(2,3)
mdizi2 = dizi2.reshape(2,3)

sonuc = np.vstack((mdizi,mdizi2)) #dizileri dikey olarak alt alta getirir
sonuc = np.hstack((mdizi,mdizi2)) #dizileri yatay olarak yan yana getirir
print(sonuc)

