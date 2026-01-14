import time

inicio = time.perf_counter()  # Início da contagem de tempo

print("\n\033[93m ### CODE START ### \033[0m\n")

# 👇👇👇 Coloque o seu código na linha abaixo desse comentário 👇👇👇

numero1 = 'N1'
numero2 = 'N2'
count_tentativas = 0

while True:  
    try:
        numero1 = int(input("Digite um número inteiro: "))
        numero2 = int(input("Digite outro número inteiro: "))
        print(f"Você digitou: {numero1}")
        print(f"Você digitou: {numero2}")
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
        count_tentativas = count_tentativas + 1
        print(count_tentativas)
    if count_tentativas > 3:
        print('Numero máximo de tentativas. Saindo do programa')
        break
        
print(numero1)
print(numero2)

numero3 = numero1 / numero2

numero3F = int(numero3)

print(numero3F)

# 👆👆👆 Coloque o seu código na linha acima desse comentário 👆👆👆

time.sleep(1)  # Exemplo de código a ser medido

print("\n\033[92m ### CODE END SUCCESS!!! ### \033[0m\n")

fim = time.perf_counter()  # Fim da contagem de tempo

print(f"\033[96mTempo de execução: {fim - inicio:.2f} segundos\033[0m\n\n\n")