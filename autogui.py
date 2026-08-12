import pyautogui
import time

mensagem = ("")
quantidade = 10000

intervalo = 0.1

time.sleep(3)

for i in range(quantidade):
    pyautogui.write(f"{mensagem} #{i + 1}", interval=0)
    pyautogui.press("enter")
    time.sleep(intervalo)