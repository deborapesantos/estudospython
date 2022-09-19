
#criar funções

def saudacao():
    print("seja bem vinda(o)!")
    print("Olá, é um prazer ter você conosco!")
    
saudacao()
#------------------------------------------
def saudacao(nome,curso):
    print(f"seja bem vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você conosco no curso de {curso}!")
    
saudacao("Debora","Python")
saudacao("Diego","C#")
#------------------------------------------
def saudacao(nome,curso="Python"): #parametro default
    print(f"seja bem vinda(o), {nome}!")
    print(f"Olá, é um prazer ter você conosco no curso de {curso}!")
    
saudacao("Debora")
saudacao("Diego","C#")

#------------------------------------------
#funções com retorno
def soma(num1,num2):
    print("soma =",num1 + num2)
    
soma(5,7)
#------------------------------------------
def soma(num1,num2):
    return(num1 + num2)
    
resultado = soma(3,7)
print("soma =",resultado)
#------------------------------------------
def calculadora(num1,num2,operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2

print(calculadora(3,5))
print(calculadora(3,5,"-"))

