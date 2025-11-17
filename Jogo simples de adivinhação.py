import random

num = random.randint(1, 20)
chute = int(input("Adivinhe um número entre 1 e 20: "))

if chute == num:
    print("Acertou!")
else:
    print("Errou! O número era:", num)
