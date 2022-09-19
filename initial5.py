lista = [1,3,12,8,12]

#append - adicionar elemento no final
print("antes",lista)
lista.append(3)
print("depois",lista)

#insert - adicionar elemento em determinada posição(indice)
lista.insert(2,10) #insert(indice,elemento)
print("depois insert",lista)

#extend - juntar lista (join)
lista2 = [1,2,3]
lista.extend(lista2)
print("depois extend",lista)

#pop - remover elemento
lista.pop() #sem parametro remove o ultimo
print("apos pop",lista)

lista.pop(0) #com parametro remove o elemento no indice indicado pop(indice)
print("apos pop",lista)

#remove - remove elemento indicado
lista.remove(3) #remove o primeiro item indicado que ele encontra - remove(elemento)
print("apos remvoe",lista)

#count - contar quantas vezes aparece um elemento em uma lista
print("quantidade count 12: ",lista.count(12) )#conta quantas vezes aparece elemento - count(elemento)

#index - mostra o indice de um elemento em uma lista
print("indice do elemento 12: ", lista.index(12))

#sort - ordena os elementos de uma lista

lista.sort()# ordena em modo crescente
print("apos sort: ",lista )

lista.sort(reverse=True)# ordena em modo crescente
print("apos sort desc: ",lista )


#funções para lista

#len - tamanho da lista
print(len(lista))

#sum - soma elementos da lista
print(sum(lista))

#min - menor elemento
print(min(lista))

#max - maior elemento
print(max(lista))








