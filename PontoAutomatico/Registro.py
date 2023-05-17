import pyautogui
from time import sleep
from dotenv import load_dotenv
load_dotenv()
import os

pyautogui.PAUSE = 1
#passo 1: acessar o sistema da empresa
pyautogui.moveTo(1845, 1060) #abrir uma aba do navegador
pyautogui.click() #clicar no botão
pyautogui.moveTo(1782, 81)#clicar na barra de pesquisa
pyautogui.click()

#passo 2: fazer login no sistema
pyautogui.moveTo(3147, 415)
pyautogui.click()
pyautogui.write(os.environ["email"])
pyautogui.press("tab")
pyautogui.write(os.environ["senha"]) 
pyautogui.press("enter")

#passo 3: entrar na tela de registro de ponto
sleep(8)
pyautogui.moveTo(2560, 460)
pyautogui.click()

#passo 4: registrar o ponto e confirmar
sleep(12)
pyautogui.moveTo(2989, 653)#selecionar localizacao do botão de registro
pyautogui.click()
pyautogui.moveTo(2694, 599) #selecionar localizacao do botao de confirmar
#pyautogui.click()#clicar em confirmar
sleep(1)
pyautogui.press("f5")#recarregar a pagina