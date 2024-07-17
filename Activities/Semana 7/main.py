import funcoes

numero1 = -1
numero2 = -1

while numero2 != 0 and numero1 != 0:
    funcoes.menu()
    opcao = int(input("Qual operação gostaria de realizar? "))
    match opcao:
        case 1:
            numero1, numero2 = funcoes.pediDoisNumeros()
            print(funcoes.somaDoisNumeros(numero1, numero2))
        case 2:
            numero1, numero2 = funcoes.pediDoisNumeros()
            print(funcoes.subtraiDoisNumeros(numero1, numero2))
        case 3:
            numero1, numero2 = funcoes.pediDoisNumeros()
            print(funcoes.multiplicaDoisNumero(numero1, numero2))
        case 4:
            numero1, numero2 = funcoes.pediDoisNumeros()
            print(funcoes.dividiDoisNumero(numero1, numero2))
        case 5:
            numeroTabuada = int(input("Insirá o Número que deseja ver a tabuada: "))
            funcoes.gerarTabuada(numeroTabuada)
        case 6:
            listaDeCandidatos = funcoes.registraCandidato()
            funcoes.eleicao(listaDeCandidatos)
        case _:
            print("Opção Inválida!")
    