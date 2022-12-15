import pyautogui
from time import sleep

# 1 - Clicar Para Pesquisar Grupo (Cordenadas: 245,170)
pyautogui.click(245,170,duration=1)
# 2 - Digitar nome do Grupo
pyautogui.write('grupo 2')
# 3 - Clicar no Grupo (Cordenadas: 308,292)
pyautogui.click(308,292,duration=1)
# 4 - Clicar no Campo para Mandar Menssagem (Cordenadas: 794,983)
pyautogui.click(794,983,duration=1)
# 5 - Colar Menssagem
pyautogui.write('https://youtu.be/YItDbfpi-SY')
# 6 - Clicar em Enviar Menssagem (Cordenadas: 1724,980)
#pyautogui.click(1724,980,duration=1)
pyautogui.press('enter')
pyautogui.press('enter')
