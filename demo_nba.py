import pandas as pd

df = pd.read_csv("all_seasons.csv")

# 1- İlk 10 kaydı getiriniz.

                # print(df.head(10))

# 2- Toplam kaç kayıt vardır ?
        # print(df.shape)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?

# 4- En yüksek maaşı ne kadardır ?

# 5- En yüksek maaşı alan oyuncu kimdir ?

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
      
        # result =df[(df["age"]>20) &  (df["age"]<25)] [["age"]]
        # print(result.sort_values)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?

# print(df[df["player_name"]=="John Holland"])
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?


# 9- Kaç farklı takım mevcut ?
# print(df["team_abbreviation"].value_counts())
#team_abbreviation

# 10- Her takımda kaç oyuncu oynamaktadır ?

# 11- İsmi içinde "and" geçen kayıtları bulunuz.

result = df[df["player_name"].str.contains("and")]
print(result)







