

def menu():
    return print("""
===============================================
    Escolha que Operação entre dois números
===============================================
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir 
    5. Gerar Tabuada
    6. Eleições
===============================================""")

def pediDoisNumeros():
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))
    return numero1, numero2

def somaDoisNumeros(numero1, numero2):
    return numero1 + numero2

def subtraiDoisNumeros(numero1, numero2):
    return numero2-numero1

def multiplicaDoisNumero(numero1, numero2):
    return numero1*numero2

def dividiDoisNumero(numero1, numero2):
    return numero1/numero2

def gerarTabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{i} x {numero} = {i*numero}")

def registraCandidato():
    listaDeCandidatos = {}
    index = 1
    while True:
        candidato = input("Insira o nome do Candidato ou 0 para sair: ")
        if candidato != "0":
            listaDeCandidatos[index] = candidato
            index+=1
        else:
            break
    return listaDeCandidatos
            

def eleicao(listaDeCandidatos):
    votos = {}
    candidatos = []
    print(listaDeCandidatos)
    for b in listaDeCandidatos.keys():
        votos[b] = 0
        candidatos.append(b)
    eleitores = int(input("Quantos eleitores votarão: "))
    print(candidatos)
    votosNulos = 0
    for _ in range(eleitores):
        candidato = input("Em quem você quer votar? ")
        if int(candidato) in candidatos:
            votos[int(candidato)] += 1
        else: votosNulos+=1
    apuracaoDasEleicoes(votos, listaDeCandidatos)

def apuracaoDasEleicoes(votos, listaDeCandidatos):
    vencedor = 1
    empate = []
    for key in votos.keys():
        if votos[int(key)] == votos[int(vencedor)]:
            empate.append(key)
        elif votos[int(key)] > votos[int(vencedor)]:
            vencedor = key
            empate = []
    if len(empate) > 0:
        print(empate)
    else:
        print(f"O vencedor é: {listaDeCandidatos[vencedor]}")