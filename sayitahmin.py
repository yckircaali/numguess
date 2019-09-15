import random

print('*******************************')
print('Sayi Tahmin Oyununa Hosgeldiniz')
 
rand=random.randint(1, 100)
kontrol = 0

while kontrol != 1 :
    sayi=int(input("1 ile 100 arasinda bir deger girininiz :"))
    if sayi < rand:
        print("Tahmininiz dusuk, daha yuksek bir sayi girmelisiniz.")
    elif sayi > rand:
        print("Tahmininiz yuksek, daha dusuk bir sayi girmelisiniz.")
    else:
        print("Tebrikler rastgele secilen sayi {0}!".format(rand)) ; kontrol = 1