import pyautogui
import time

# Função para pressionar a tecla "Win"
def press_win_key():
    pyautogui.press('win')

# Loop para pressionar a tecla "Win" a cada minuto
while True:
    press_win_key()
    print("Tecla Win pressionada!")
    time.sleep(60)  # Aguarda 1 minuto
