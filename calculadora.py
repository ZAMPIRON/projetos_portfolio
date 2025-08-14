import math
import os

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero")
    return a / b

def multiplicar(a, b):
    return a * b

def potenciação(a, b):
    return math.pow(a, b)

def raiz(x):
    if x < 0:
        print("Erro, o número não pode ser menor que zero")
    return math.sqrt(x)

def fatorial(x):
    if x < 0:
        print("Erro, o número não pode ser menor que zero")
    return math.factorial(int(x))

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def log_base_10(x):
    if x <= 0:
        print("Erro: Logaritmo de número não positivo")
    return math.log10(x)

def log_base_e(x):
    if x <= 0:
        print("Erro: Logaritmo de número não positivo")
    return math.log(x)

def menu():
    print("\nSEJA BEM-VINDO!")
    print("ESTA É A CALCULADORA CIENTÍFICA")
    print("\nMENU ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Seno (graus)")
    print("9. Cosseno (graus)")
    print("10. Tangente (graus)")
    print("11. Logaritmo (base 10)")
    print("12. Logaritmo (base e)")
    print("13. Sair")

def vai_menu():
    menu()
    n = 1023

    while n == 1023:
        escolha = int(input("\nEscolha uma opção de 0 - 12 (0 para ver o menu e qualquer outro número para sair)\n--> "))

        if escolha == 0:
            os.system("cls")
            menu()

        elif escolha == 1:
            os.system("cls")
            print("\n*** SOMAR ***")
            a = float(input("1º número: "))
            b = float(input("2º número: "))
            print(f"Resultado --> {somar(a, b)}")

        elif escolha == 2:
            os.system("cls")
            print("\n*** SUBTRAIR ***")
            a = float(input("1º número: "))
            b = float(input("2º número: "))
            print(f"Resultado --> {subtrair(a, b)}")

        elif escolha == 3:
            os.system("cls")
            print("\n*** DIVIDIR ***")
            a = float(input("1º número: "))
            b = float(input("2º número: "))
            print(f"Resultado --> {dividir(a, b)}")

        elif escolha == 4:
            os.system("cls")
            print("\n*** MULTIPLICAR ***")
            a = float(input("1º número: "))
            b = float(input("2º número: "))
            print(f"Resultado --> {multiplicar(a, b)}")

        elif escolha == 5:
            os.system("cls")
            print("\n*** POTENCIAÇÃO ***")
            a = float(input("1º número: "))
            b = float(input("2º número: "))
            print(f"Resultado --> {potenciação(a, b)}")

        elif escolha == 6:
            os.system("cls")
            print("\n*** RAIZ QUADRADA ***")
            x = float(input("Número: "))
            print(f"Resultado --> {raiz(x)}")

        elif escolha == 7:
            os.system("cls")
            print("\n*** FATORIAL ***")
            x = float(input("Número: "))
            print(f"Resultado --> {fatorial(x)}")

        elif escolha == 8:
            os.system("cls")
            print("\n*** SENO ***")
            x = float(input("ÂNGULO: "))
            print(f"Resultado --> {seno(x)}")

        elif escolha == 9:
            os.system("cls")
            print("\n*** COSSENO ***")
            x = float(input("ÂNGULO: "))
            print(f"Resultado --> {cosseno(x)}")

        elif escolha == 10:
            os.system("cls")
            print("\n*** TANGENTE ***")
            x = float(input("ÂNGULO: "))
            print(f"Resultado --> {tangente(x)}")

        elif escolha == 11:
            os.system("cls")
            print("\n*** LOGARITMO BASE 10 ***")
            x = float(input("Número: "))
            print(f"Resultado --> {log_base_10(x)}")

        elif escolha == 12:
            os.system("cls")
            print("\n*** LOGARITMO BASE E ***")
            x = float(input("Número: "))
            print(f"Resultado --> {log_base_e(x)}")

        else:
            print("Saindo da calculadora. Até logo!")
            os._exit(0)
            
        

os.system("cls")
vai_menu()
