#Importando Lib's
import pyautogui
from time import sleep

#Armazenar os grupos em uma lista
Lista_grupos = ['grupo 1','grupo 2', 'grupo 3', 'Teste']

#Abrir WhatsApp DeskTop
def Abrir_WhatsApp_Desktop():
    #Clicar no botão do whindows
    pyautogui.press('winleft')
    #Abrir o WhatsApp Desktop
    pyautogui.write('WhatsApp')
    pyautogui.press('enter')
    #Dar um tempo para abrir
    sleep(10)
    #Entrar na conversa que encaminhou o video
    pyautogui.hotkey('ctrl','f')
    pyautogui.write('Marcos(TI)')
    pyautogui.click(216,174,duration=1)


#Encaminhar Primeira Menssagem
def Encaminhar_primeira_menssagem(grupo):
    #Encaminhar Primeira Menssagem

    # 1 - Clicar na menssagem para abrir caixa de opções(Cordenadas: 829,877)
    pyautogui.rightClick(829,877,duration=1)
    # 2 - Clicar em Encaminhar (Cordenadas: 899,760)
    pyautogui.doubleClick(899,760,duration=1)
    sleep(2)
    # 3 - Escrever nome do grupo que vai ser encaminhado a menssagem
    pyautogui.write(grupo)
    # 4 - Seleciona ro grupo (Cordenadas: 1016,672)
    pyautogui.click(1016,672,duration=1)
    # 5 - Clicar em "Encaminhar Menssagem" (Cordenadas: 958,631)
    pyautogui.click(958,631,duration=1)


#Encaminhar Menssagens Restantes
def Encaminhar_outras_menssagem(grupo):
    sleep(2)
    # 1 - Clicar na menssagem para abrir caixa de opções(Cordenadas: 829,877)
    pyautogui.rightClick(1508,870,duration=1)
    # 2 - Clicar em Encaminhar (Cordenadas: 899,760)
    pyautogui.doubleClick(1553,729,duration=1)
    sleep(2)
    # 3 - Escrever nome do grupo que vai ser encaminhado a menssagem
    pyautogui.write(grupo)
    # 4 - Seleciona ro grupo (Cordenadas: 1016,672)
    pyautogui.click(1338,678,duration=1)
    # 5 - Clicar em "Encaminhar Menssagem" (Cordenadas: 958,631)
    pyautogui.click(1349,632,duration=1)


#Executar Comandos
def Executar_Comandos():
    #Abrir WhatsApp Desktop
    Abrir_WhatsApp_Desktop()
    #Rodar essa lista
    for index, grupo in enumerate(Lista_grupos):
        if  index == 0:
            Encaminhar_primeira_menssagem(grupo)
        else:
            Encaminhar_outras_menssagem(grupo)

        #Printa no Terminal
        Cor_Verde = "\033[0;32m"
        print(Cor_Verde + f'Enviado com SUCESSO! *******{grupo}*******')


#Chamando as Funções
Executar_Comandos()