import time

inicio = time.perf_counter()  # Início da contagem de tempo

print("\n\033[93m ### CODE START ### \033[0m\n")

# 👇👇👇 Coloque o seu código na linha abaixo desse comentário 👇👇👇

frase_inteira = 'Entrega teu destino a Ele, e o resto Ele fará'
frase_partida = frase_inteira.split()
print('Essa é a frase partida >>> ', frase_partida, '\n')
palavra_salvadora = frase_partida[7]
print('Essa é a palavra salvadora >>> ', palavra_salvadora, '\n')
palavra_salvadora_purificada = palavra_salvadora.split(',')
print('Essa é a palavra salvadora purificada >>> ', palavra_salvadora_purificada , '\n')
palavra_salvadora_purificada_sagrada = palavra_salvadora_purificada[0]
print('Essa é a palavra salvadora purificada sagrada>>> ', palavra_salvadora_purificada_sagrada , '\n')

if palavra_salvadora_purificada_sagrada == 'Ele':
    print('Sua alma será salva 🙏!')
else: print('Você ainda é um pecador! 😈')

# 👆👆👆 Coloque o seu código na linha acima desse comentário 👆👆👆

time.sleep(1)  # Exemplo de código a ser medido

print("\n\033[92m ### CODE END SUCCESS!!! ### \033[0m\n")

fim = time.perf_counter()  # Fim da contagem de tempo

print(f"\033[96mTempo de execução: {fim - inicio:.2f} segundos\033[0m\n\n\n")
