#variaveis
idade= 26 #int
altura=1.57 #float
nome="Debora" #str
brasileira=True #bool

print(idade,altura,nome,brasileira)

nomeusuario = input("digite seu nome")

#comentário em python
'''
bloco de comentário em python
'''

#exemplo interpolação
print(f"seu nome é {nomeusuario}")


#condicionais
age = 20

if age >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    
# else if
media = float(input("informe a media: "))

if media >= 7:
  print("Aprovada")
elif media >= 5:
  print("Recuperacao")
else:
  print("Reprovada")

#comparação conjunta
media = 10
presenca = 100

if media >= 7 and presenca >= 70: # && is AND e || is OR
    print("aprovada")
    print("Parabéns")
else:
    print("reprovada")
    

    




