import pandas as pd

data = pd.read_csv("NBA.csv")
result = data
# İlk 10 kaydı getiriniz
result = data.head(10)

# Toplam kaç kayıt vardır
result = len(data.index)

# Tüm oyuncuların toplam yaş ortalaması nedir
result = data["age"].head(10).mean()

# En büyük oyuncunun yaşı nedir
result = data["age"].max()

# En büyük oyuncu kimdir
result = data[data["age"] == data["age"].max()]["player_name"].iloc[0] # iloc[0] ifadesinde 0. index seçilir. Yani sadece player_name gösterilir bu sayede

#Yaşı 20-25 yaş arası oyuncuların ismi ve oynadıkları takımı azalan şekilde sırala
result = data[(data["age"] >= 20) & (data["age"] <= 25)][["player_name","team_abbreviation","age"]].sort_values("age",ascending=False)

# Tony Smith adlı oyuncunun oynadığı takım ismi nedir
result = data[data["player_name"] == "Tony Smith"]["team_abbreviation"].iloc[0]

# Ülkelere göre oyuncuların ortalama boy bilgisi
data["player_height"] = data["player_height"].astype(float) #floata çevirdik
result = data.groupby("country")["player_height"].mean()

# Kaç farklı ülke vardır
result = len(data.groupby("country"))
result = data["country"].nunique() #Diğer yöntem. Tekrar edenleri çıkararak sayısını verir

# Her ülkede kaç oyuncu oynamaktadır
result = data["country"].value_counts()

# İsmi içinde "and" geçen kayıtları bulunuz
result = data[data.player_name.str.contains("and")]
print(result)