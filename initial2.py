#laço de repetição

numero_sorteado = 15
numero_escolhido = int(input("informe o numero entre 1 e 20:"))

while numero_sorteado != numero_escolhido:
    print("Errou o numero, tente novamente!")
    numero_escolhido = int(input("informe o numero entre 1 e 20:"))
    
print("parabens, acertou")
