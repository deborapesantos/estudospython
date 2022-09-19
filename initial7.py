
# criar dictionary
dicionario = {}
dicionario = dict()

dicionario = {
    "nome":"Debora", 
    "idade":27,
    "altura":1.57
}

print(dicionario)
print(dicionario["idade"])

#adicionar elementos dicionario
dicionario["profissão"] = "Programadora"

#sobescrever valor
dicionario["idade"]= 1.60
print(dicionario)

#interar um dicionario
for key in dicionario:
    print(key,dicionario[key])
    
#testar existencia de uma chave
print("peso" in dicionario)
print("altura" in dicionario)
