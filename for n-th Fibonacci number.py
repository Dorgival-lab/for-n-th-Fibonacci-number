# Função para o enésimo número de Fibonacci
  
def Fibonacci(n): 
    if n<0: 
        print("Entrada incorreta") 
    # O primeiro número de Fibonacci é 0 
    elif n==1: 
        return 0
    # O segundo número de Fibonacci é 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(9)) 
  
#Este código é contribuído por Dorgival Fernando