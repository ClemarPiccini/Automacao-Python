import pyautogui
from time import sleep

pyautogui.PAUSE = 1
#comandos fundamentais:
#pyautogui.click (passar as cordenadas da tela para o mouse se movimentar e clicar)
#pyautogui.write (escrever "string")
#pyautogui.press (apertar o botão do mouse, tanto o direito quanto esquerdo)
#pyautogui.hotkey( duas teclas combinadas"ctrl+t")

#passo 1: acessar o sistema da empresa
pyautogui.moveTo(1845, 1060) #abrir uma aba do navegador
pyautogui.click() #clicar no botão
pyautogui.moveTo(1782, 81)#clicar na barra de pesquisa
pyautogui.click()
#pyautogui.write("link")#passar o link que quer acessar
#pyautogui.press("enter")

#passo 2: fazer login no sistema
#clicar na barra de email
#digitar email
#presionar tab
#digitar a senha
#precionar enter

#passo 3: entrar na tela de registro de ponto
#selecionar localizacao do registro de ponto
#clicar com o mouse

#passo 4: registrar o ponto e confirmar
#selecionar localizacao do botão de registro
#selecionar localizacao do botao de confirmar
#recarregar a pagina