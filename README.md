# estudospython


Variáveis e Tipos de Dados
Em Python, você pode usar variáveis para armazenar informações. Não precisa declarar o tipo delas. Por exemplo:
`nome = "Maria"
idade = 25
altura = 1.65`

Saída de Dados:
Você pode imprimir informações na tela usando a função print():
`
print("Olá, mundo!")
print("Meu nome é", nome)`

Entrada de Dados:
Para receber entrada do usuário, use a função input():
`
entrada = input("Digite algo: ")
print("Você digitou:", entrada)`


Estruturas de Controle:
Use if, elif e else para tomar decisões:
`
idade = int(input("Qual é a sua idade? "))
if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
`

Laços de Repetição:
Use for para percorrer uma sequência (como uma lista):
`numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
`

Funções:
Defina funções para agrupar código:
`def saudacao(nome):
    print("Olá,", nome, "!")    
saudacao("João")
`

Listas:
Listas são coleções ordenadas de elementos:
`
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessando o primeiro elemento
`

Dicionários:
Dicionários armazenam pares chave-valor:
`
aluno = {"nome": "Ana", "idade": 20, "nota": 9.5}
print(aluno["nome"])
`

Classes e Objetos:
Classes definem estruturas para criar objetos:
`
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
pessoa1 = Pessoa("Pedro", 30)
print(pessoa1.nome)`
