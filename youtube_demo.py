import pandas as pd

df=pd.read_csv("Gbvideos.csv")

# 1- İlk 10 kaydı getiriniz.
"""print(df.head(10))"""

# 2- İkinci 5 kaydı getiriniz.
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
#"""print(df.shape)"""

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.

# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
        # df= df.drop("thumbnail_link", axis=1)
        # print(df.columns)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
    #"""print(df["likes","dislike"].describe(std))"""

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
    #"""print( df.sort_values(by='likes', ascending=False).head(10))
    #print( df.sort_values(by='dislikes', ascending=False).head(10))"""

# 7- En çok görüntülenen video hangisidir ?
    #print(df.sort_values(by='views', ascending=False).head(1))

# 8- En düşük görüntülenen video hangisidir?
    #print( df.sort_values(by='views', ascending=True).head(1))

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
    #""""print( df.sort_values(by='views', ascending=False).head(10))"""


# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
        # result=  df.groupby("category_id")["likes"].mean()
        # print(result.sort_values( ascending=False))

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
        # result= df.groupby("category_id")["comment_count"].sum()
        # print(result.sort_values(ascending=False))

# 12- Her kategoride kaç video vardır ?
        # result= df.groupby("category_id")["video_id"].sum()
        # print(result.sort_values(ascending=False))

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
        # df["title_len"] = df["title"].apply(len)
        # print(df)

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
        # df["tag_count"] = df["tags"].apply(lambda x: len( x.split("|")))
        # print(df)

# 15- En popüler videoları listeleyiniz. (like/dislike oranına göre)


def oran(dataset):
    likes_list=list(dataset["likes"])
    dislike_list=list(dataset["dislikes"])
    liste= list(zip(likes_list,dislike_list))
    oranlist=[]


    for like ,dislike in liste:
        if (like+dislike) == 0:
            oranlist.append(0)
        else:
            oranlist.append(like/(like+dislike))

    return oranlist    


   

df["beğeni_oranı"] =oran(df)


print(df.sort_values(by='beğeni_oranı', ascending=False))