'''listaNotas = [9, 7.9 , 8.2]

newlista = []
lista = list()

#lista no python permite criar um array de dados variados
lista = [26,"Debora",True]

listaDeListas = [10,[1,2,3]]

#acessar um indice
listaPessoa = [27,"Debora","Brasileira","Desenvolvedora"]

print(f"idade {listaPessoa[0]}")
print(f"nome {listaPessoa[1]}")
print(f"profissão {listaPessoa[3]}")'''

#slices

listaNumeros = [10,50,30,40,25,60,5]
'''print(listaNumeros[0:3])
print(listaNumeros[3:6])
print(listaNumeros[3:]) #pega do indice 3 para frente
print(listaNumeros[3:6:2]) #pega do indice 3 até menor que 6, contando em 2 em 2'''

for item in listaNumeros:
    print(item)

print("comprimento da lista ",len(listaNumeros)) # len de length

for i in range(len(listaNumeros)):
    print(listaNumeros[i])
