import pandas as pd

data = pd.read_csv("Youtubes.csv")
result = data

# İlk 10 kaydı getiriniz.
result = data.head(10)

# İkinci 5 kaydı getiriniz
result = data[5:].head()

# Dataset'te bulunan kolon isimleri ve sayısını bulunuz.
result = data.columns
result = len(data.columns)

# Bazı kolonları silin ve kalan kolonları listeleyiniz.(thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
data.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
result=data

# Beğenme ve beğenmeme sayılarının ortalamasını bulunuz.
result = (data[("likes")] + data[("dislikes")]).mean

# ilk 50 videonun likes ve dislike sayılarını bulunuz
result = data[:50][["likes","channel_title"]]
result = data[:50][["dislikes","channel_title"]]

# En çok görüntülenen video hangisidir
result = data[data["views"].max()== data["views"]]["title"].iloc[0]

# En düşük görüntülenen video hangisidir
result= data[data["views"].min()==data["views"]]["title"].iloc[0]

# En fazla görüntülenen ilk 10 video hangisidir
result = data.sort_values("views",ascending=False).head(10)

#Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz
# result = data.groupby("category_id").mean().sort_values("likes")["likes"] #Burada agg ile ilgilli hata veriyor

# Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
data["title_length"] = data["title"].apply(len)
result = data

# Her video için kullanılan tag sayısını yeni bir columnda gösteriniz.
data["tag_count"] = data["tags"].apply( lambda x: len(x.split("|")))

# En popüler videoları listeleyiniz (like/dislike durumuna göre)
def likedislike(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])
    liste = list(zip(likesList,dislikesList)) # Like ve dislikeları ikişer ikişer gruplar(zip)
    oranListesi = []

    for likes,dislikes in liste:
        if (likes+dislikes) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(likes/(likes+dislikes))
    return oranListesi

data["begeni_orani"] = likedislike(data)
print(data.sort_values("begeni_orani",ascending=False)[["title","likes","dislikes","begeni_orani"]])
