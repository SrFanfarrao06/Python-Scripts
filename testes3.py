import time

inicio = time.perf_counter()  # Início da contagem de tempo

print("\n\033[93m ### CODE START ### \033[0m\n")

# 👇👇👇 Coloque o seu código na linha abaixo desse comentário 👇👇👇


senha = (f'123')
senha_inputada = input (f'entre a senha: ')
count_tentativas = 0
# print(senha_inputada)
# print(count_tentativas)

# if senha == senha_inputada:
#     print('BEM VINDO!')
# else:
#     print('SENHA INCORRETA')
#     senha_inputada = input (f'entre a senha: ')
#     count_tentativas = count_tentativas +1
#     if count_tentativas > 3:
#         print('Maximo de tentativas atingido. fechando programa')

while senha != senha_inputada and count_tentativas < 3:
       print('senha incorreta. Tente novamente')
       count_tentativas = count_tentativas + 1
       print('numero de tentativas: ', count_tentativas)
       senha_inputada = input ('entre a senha: ')
if senha == senha_inputada:
    print('BEM VINDO!')
else: count_tentativas >= 3
print('Maximo de tentativa alcançado. Fechando o programa')



# 👆👆👆 Coloque o seu código na linha acima desse comentário 👆👆👆

time.sleep(1)  # Exemplo de código a ser medido

print("\n\033[92m ### CODE END SUCCESS!!! ### \033[0m\n")

fim = time.perf_counter()  # Fim da contagem de tempo

print(f"\033[96mTempo de execução: {fim - inicio:.2f} segundos\033[0m\n\n\n")
