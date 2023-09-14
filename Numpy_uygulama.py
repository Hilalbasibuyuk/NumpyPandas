import numpy as np

np_dizi = np.array([10,15,30,45,60])
print(np_dizi)

np_dizi2 = np.arange(5,15)
print(np_dizi2)

np_dizi3 = np.arange(50,100,5)
print(np_dizi3)

np_dizi4 = np.zeros(10)
print(np_dizi4)

np_dizi5 = np.linspace(0,100,5)
print(np_dizi5)

np_dizi6 = np.random.randint(10,30,5)
print(np_dizi6)

np_dizi7 = np.random.randn(10)
print(np_dizi7)

np_dizi8 = np.random.randint(10,50,15).reshape(3,5)
print(np_dizi8)
print(np_dizi8.sum(axis=0))
print(np_dizi8.sum(axis=1))

enbuyuk = np_dizi8.max()
enkucuk = np_dizi8.min()
ortalama = np_dizi8.mean()
maxinIndeksi = np_dizi8.argmax()

print(enbuyuk)
print(enkucuk)
print(ortalama)
print(maxinIndeksi)
