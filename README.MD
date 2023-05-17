CODIGO PARA AUTOMATIZAR REGISTRO DE PONTO

#install:

pip install pyautogui

pip install python-dotenv

#.env

criar arquivo com nome (.env) na mesma pasta do código contendo as seguintes informações:

email = "seu_email_aqui"

senha = "sua_senha_aqui"

#mouse.py

utilizado para pegar as cordenadas do mouse na tela para definir onde deve ser feito os .click

#Registro.py

utilizado para realizar o passo a passo definido, deve ser alterado as cordenadas de acordo com cada monitor, e adicionado mais etapas para se adequar aos diferentes tipos de sistemas de login.

#sleep

utilizado para aguardar o tempo de atualização das paginas no servidor, pode variar de acordo com a velocidade de conexão