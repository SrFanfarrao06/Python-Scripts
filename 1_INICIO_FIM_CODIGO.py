import time

inicio = time.perf_counter()  # Início da contagem de tempo

print("\n\033[93m ### CODE START ### \033[0m\n")

# 👇👇👇 Coloque o seu código na linha abaixo desse comentário 👇👇👇

a=1
b=2
c= a + b

print(c)
d= c + 5
print(d)



# 👆👆👆 Coloque o seu código na linha acima desse comentário 👆👆👆

time.sleep(1)  # Exemplo de código a ser medido

print("\n\033[92m ### CODE END SUCCESS!!! ### \033[0m\n")

fim = time.perf_counter()  # Fim da contagem de tempo

print(f"\033[96mTempo de execução: {fim - inicio:.2f} segundos\033[0m\n\n\n")
