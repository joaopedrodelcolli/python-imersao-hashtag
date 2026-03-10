# Bibliotecas = pacotes de código
# pip install pyautogui


import time
import pyautogui

# pyautogui. click -> clica
# pyautogui.worte -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")

# Atalho Win + R para abrir o 'Executar'
pyautogui.hotkey("win", "r")
time.sleep(1)

# Comando para abrir o Chropythonimpressionador@gmail.comme no perfil específico
# O primeiro perfil costuma se chamar "Default", o segundo "João Pedro", etc.
pyautogui.write('chrome.exe --profile-directory="Pessoa 1"') 
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer Login

#clicar no ponto de email
pyautogui.click(x=2893, y=484)
pyautogui.write("pythonimpressionador@gmail.com")

#ir para o campo de senha
pyautogui.press("tab")
pyautogui.write("sua senha")

# ir para o campo de logar
pyautogui.press("tab")
pyautogui.press("enter")

# fazer um pausa para o site carregar
time.sleep(4)

# Passo 3: Abrir base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto

    # cod
    pyautogui.click(x=2883, y=364)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")


    # obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    # voltar para o início da tela
    pyautogui.scroll(5000)


# Passo 5: Repetir o passo 4 até acabar a lista

