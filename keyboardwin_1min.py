import time
import threading
import keyboard

# Função para pressionar a tecla "Win"
def press_win_key():
    while not stop_event.is_set():
        keyboard.press_and_release('win')
        print("Tecla Win pressionada!")
        time.sleep(10)  # Espera 1 minuto

# Função para parar o thread
def stop_thread():
    stop_event.set()

# Cria um evento para parar o thread
stop_event = threading.Event()

# Cria e inicia o thread para pressionar a tecla "Win" continuamente
win_key_thread = threading.Thread(target=press_win_key)
win_key_thread.start()

# Aguarda a entrada para parar o thread
input("Pressione Enter para parar o script...\n")
stop_thread()
win_key_thread.join()
print("Script encerrado.")
