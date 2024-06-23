# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
#  salários até R$ 280,00 (incluindo) : aumento de 20%
#  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#  salários de R$ 1500,00 em diante :
#  aumento de 5% Após o aumento ser realizado,
#  informe na tela:
#  o salário antes do reajuste;
#  o percentual de aumento aplicado;
#  o valor do aumento;
#  o novo salário, após o aumento.

salary = float(input("Input the salary to adjusted: "))

if salary <= 280:
    increase = 0.2
elif salary <= 700:
    increase = 0.15
elif salary <= 1500:
    increase = 0.1
else:
    increase = 0.05

print(f"""The salary before the increase: R$ {salary:.2f}
The increase about: {increase*100:.0f}%
The amount added is: R$ {salary*increase:.2f}
The new salary is: R$ {salary+ (salary*increase):.2f}""")