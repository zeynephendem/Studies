#BANKAMATİK UYGULAMASI

ZeynepHesap={
    "ad":"Zeynep Hendem",
    "hesapNo":"12345678",
    "bakiye":5000,
    "ekHesap":1000
}
FatmaHesap={
    "ad":"Fatma Yılmaz",
    "hesapNo":"21345678",
    "bakiye":4000,
    "ekHesap":3000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap["bakiye"]>=miktar):
        hesap["bakiye"]-=miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]

        if(toplam>=miktar):
            ekHesapKullanimi=input("Ek hesap kullanılsın mı (e/h)?")
             
            if ekHesapKullanimi=="e":
                bakiye=hesap["bakiye"]
                ekHesapKullanilacakMiktar=miktar-bakiye
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye kaldı.")
        else:
            print("Üzgünüz bakiye yetersiz.")
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL'dir.")

paraCek(ZeynepHesap,5000)
bakiyeSorgula(ZeynepHesap)

paraCek(FatmaHesap,2000)
