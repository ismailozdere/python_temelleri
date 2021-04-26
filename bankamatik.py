 
ismailhesap={
    "ad": "ismail özdere",
    "hesapno": "125487",
    "bakiye": 3000,
    "ekhesap": 2000
    }

yusufhesap={
    "ad": "yusuf özdere",
    "hesapno": "135489",
    "bakiye": 2000,
    "ekhesap": 1000
}



def paracek(hesap,miktar): 
    print(f'merhaba {hesap["ad"]}')

    if (hesap["bakiye"]>= miktar) :
        hesap["bakiye"]-= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam=hesap["bakiye"]+ hesap["ekhesap"]

        if (toplam >=miktar):
            ekhesapkullanimi = input("ek hesap kullanılsın mı (e/h)")

            if ekhesapkullanimi=="e"   :
                ekhesapkullanilacakdeger=miktar-hesap["bakiye"]

                hesap["bakiye"]=0
                hesap["ekhesap"]-=ekhesapkullanilacakdeger
                print("paranızı çekebilirsiniz")


            else:
                print(f'{hesap["hesapno"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır')                
        else:
            print( "üzgünüz bakiyeniz yeterli değil")
                       

paracek(ismailhesap,3000)    
paracek(ismailhesap,2000)  