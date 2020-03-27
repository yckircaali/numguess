import random

print('*******************************')
print('Welcome to the Number Guessing Game')
 
rand=random.randint(1, 100)
kontrol = 0

while kontrol != 1 :
    sayi=int(input("Enter a value between 1 and 100:"))
    if sayi < rand:
        print("Your guess is low, you should enter a higher number.")
    elif sayi > rand:
        print("You should enter a lower number if your guess is high.")
    else:
        print("Congratulations randomly chosen number {0}!".format(rand)) ; kontrol = 1
