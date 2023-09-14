import pandas as pd
imdb = pd.read_csv("imdb_top_1000.csv")
result = imdb.columns #column bilgileri gelir

# ilk 5 kaydı göster
result = imdb.head()

# son 10 kaydı göster
result = imdb.tail(10)

# sadece Series_Title kolonunu alın
result = imdb["Series_Title"]

# sadece movie title kolonunu içeren ilk 5 kaydı alın
result = imdb["Series_Title"].head()

# sadece IMDB_Rating ve Series_Title kolonunu içeren ilk 5 kaydı alın
result = imdb[["Series_Title", "IMDB_Rating"]].head()

# sadece IMDB_Rating ve Series_Title kolonunu içeren 5 ve 10 arası kayıtları alın
result = imdb[5:10][["Series_Title", "IMDB_Rating"]]

# sadece IMDB_Rating ve Series_Title kolonunu içeren imdb puani 8.0 ve üzerinde olan ilk 50 filmi yazsın
result = imdb[imdb["IMDB_Rating"]>=8.0][["Series_Title", "IMDB_Rating"]].head(50)

# Yayın tarihi 2014 ile 2015 tarihleri arasında olan filmlerin isimlerini getiriniz.

result = imdb[(imdb["Released_Year"] >= "2014") & (imdb["Released_Year"] <= "2015")][["Series_Title","Released_Year","IMDB_Rating"]]


print(result)
