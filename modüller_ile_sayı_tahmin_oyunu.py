import random
import time

rastgele_sayı=random.randint(1,100)
tahmin_hakkı=10
while True:
    tahmin=int(input("sayı giriniz"))
    if(tahmin>rastgele_sayı):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("lütfen aşşagı bır sayı gırınız")
        tahmin_hakkı-=1
    elif(tahmin<rastgele_sayı):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("lütfen yukarı bır sayı gırınız")
        tahmin_hakkı -= 1
    else:
        print("tebrikler dogru sayı girdiniz")
        break
    if(tahmin_hakkı==0):
        print("üzgünüm hakkınız bitti")
        print("tutlan sayı", rastgele_sayı)
        break



