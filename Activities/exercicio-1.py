# Faça um Programa que verifique se uma letra
# digitada é "F" ou "M".
# Conforme a letra, escrever: F - Feminino, M -
# Masculino, Sexo Inválido.

tempInput = input("Please, only input 'F' or 'M': ").upper()

if (tempInput == "F"):
    print("The letter inserted represent the Female Public.")
elif (tempInput == "M"): print("The letter inserted represent the Male Public.")
else: print("Please only input the letter F or M")