#Importando Lib's
import pyautogui
from time import sleep


#***Processo manual****Compartilhar o Video do Youtube com o Número de Ofertas
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
pyautogui.rightClick(829,877,duration=1)
pyautogui.doubleClick(899,760,duration=1)
sleep(2)
pyautogui.write('grupo 2')
pyautogui.click(1016,672,duration=1)
pyautogui.click(958,631,duration=1)
#Encaminhar Outras Menssagens
sleep(2)
pyautogui.rightClick(1508,870,duration=1)
pyautogui.doubleClick(1541,731,duration=1)
sleep(2)
pyautogui.write('grupo 1')
pyautogui.click(1338,678,duration=1)
pyautogui.click(1349,632,duration=1)





"""
#Armazenar os grupos em uma lista
Lista_grupos = ['grupo 1','grupo 2', 'grupo 3', 'Teste']



#Criar Função para executar o código
def Encaminhar_primeira_menssagem(grupo):
    # Mandando Menssagem pro Pimeiro Grupo

    # 1 - Clicar Para encaminhar menssagem (Cordenadas: 1015,784)
    pyautogui.click(1015,784,duration=1)
    sleep(2)
    # 2 - Digitar nome do Grupo
    pyautogui.write(grupo)
    # 3 - Selecionar Grupo
    sleep(2)
    pyautogui.press('enter')
    # 4 - Encaminar (cordenadas: 1113,859)
    pyautogui.click(1113,859,duration=1)


def Encaminhar_outras_menssagem(grupo):
    # Mandando Menssagem para outros Grupos

    # 1 - Clicar Para encaminhar menssagem (Cordenadas: 1390,733)
    pyautogui.click(1393,776,duration=1)
    sleep(2)
    # 2 - Digitar nome do Grupo
    pyautogui.write(grupo)
    # 3 - Selecionar Grupo(Cordenadas:780,382)
    sleep(2)
    pyautogui.click(780,382,duration=1)
    # 4 - Encaminar (cordenadas: 1113,859)
    pyautogui.click(1113,859,duration=1)



Cor_Verde = "\033[0;32m"
#--------------------------------------EXECUÇÃO---------------------------------------------------#

def Executar_Comandos():

    #Rodar essa lista
    for index, grupo in enumerate(Lista_grupos):
        if  index == 0:
            Encaminhar_primeira_menssagem(grupo)
        else:
            Encaminhar_outras_menssagem(grupo)

        #Printa na Tela
        print(Cor_Verde + f'Enviado com SUCESSO! *******{grupo}*******')

Executar_Comandos()
"""
