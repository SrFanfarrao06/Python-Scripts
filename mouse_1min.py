import pyautogui
import time

try:
    while True:
        # Move o mouse 30 pixels para cima
        pyautogui.move(0, -300, duration=0.5)
        time.sleep(10)  # Espera 1 minuto

        # Move o mouse 30 pixels para baixo
        pyautogui.move(0, 300, duration=0.5)
        time.sleep(10)  # Espera 1 minuto

except KeyboardInterrupt:
    # Interrompe o loop quando pressionada a combinação de teclas Ctrl+C
    pass
