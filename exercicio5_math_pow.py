from math import pow 

print("==CALCULADORA DE POTÊNCIA==")
print("\n")
num1 = int(input("Digite o númeor para calcular a potência:"))
num2 = int(input("Digite o expoente da potência:"))
potencia = pow(num1, num2)
print(f"o resultado de {num1} elevado a {num2} é igual a:\n{potencia}")