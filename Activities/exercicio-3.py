# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

produto1 = float(input("Input the price of the first product: "))
produto2 = float(input("Input the price of the segundo product: "))
produto3 = float(input("Input the price of the third product: "))

smallerPrice = produto1

if smallerPrice > produto2:
    smallerPrice = produto2
elif smallerPrice > produto3:
    smallerPrice = produto3

print(f"The smallest price is: R$ {smallerPrice:.2f}")