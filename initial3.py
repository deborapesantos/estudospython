
'''for item in range(5): #(stop)
  print(item)'''
  
'''for item in range(1,6): #(initial,stop)
    print(item)'''
    
    
'''for item in range(2,10,2): #(initial,stop,step)
    print(item)'''

#fazer o input das 3 notas e calcular a media delas 
    
soma = 0
    
for item in range(1,4): # ou range(3)
    nota = float(input(f"Informe sua nota {item}: "))
    soma = soma + nota
    
media = soma / 3
print(f"média é {media}")
