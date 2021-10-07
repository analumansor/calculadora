print("\n******************* Python Calculator *******************")

def adc(x,y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x,y):
    return x/y


print("Selecione uma operação:")
print("1 - Soma")
print("2 - Multiplicação")
print("3 - Subtração")
print("4 - Divisão")

operacao = input("Escolha sua operação: 1/2/3/4")

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))



if operacao == '1':
    print (n1,"+", n2, "=", adc(n1, n2))
    

elif operacao == '2':
    print (n1,"x", n2, "=", adc(n1, n2))
    
    
elif operacao == '3':
    print (n1,"-", n2, "=", adc(n1, n2))
    
    
elif operacao == '4':
    print (n1,"/", n2, "=", adc(n1, n2))
    
    
else:
    print ("Operação invalida")
    


