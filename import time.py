import time
inicio = time.perf_counter()  # Início da contagem de tempo

print("\n\033[93m ### CODE START ### \033[0m\n")

# 👇👇👇 Coloque o seu código na linha abaixo desse comentário 👇👇👇

entrada = (input('Digite 1 numero: '))
numero = int(entrada)
while numero != int():
    try:
        print('Digite apenas numeros!')
        break
    except ValueError:
        numero == int()
while numero > 99:
    try:
        print('Digite um numero menor que 100')
        numero = int(input('Digite 1 numero: '))
        breakpoint
    except ValueError:
        numero <=99

#print('numero')
resultado = numero%2
if resultado == 0:
    print('Seu numero é par')
else:
    print('Seu numero é ímpar')

print(resultado)



# numero = int(input('Entre com 1 numero: '))



# 👆👆👆 Coloque o seu código na linha acima desse comentário 👆👆👆

time.sleep(1)  # Exemplo de código a ser medido

print("\n\033[92m ### CODE END SUCCESS!!! ### \033[0m\n")

fim = time.perf_counter()  # Fim da contagem de tempo

print(f"\033[96mTempo de execução: {fim - inicio:.2f} segundos\033[0m\n\n\n")