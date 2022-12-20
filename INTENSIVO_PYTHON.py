import pyautogui
import pyperclip #permite escrever caracteres especiais
import time

pyautogui.PAUSE = 1
#pyautogui.click → clica
#pyautogui.press → aperta uma tecla
#pyautogui.hotkey → conjunto de teclas
#pyautogui.write → escreve um texto

#Passo 1: Entrar no sistema da empresa (no caso é o link do drive)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

#Passo 2: Navegar os sistema e encontrar a base de vendas (entrar na pasta exportar)
#usar o pyautogui.position()
pyautogui.click(x = 1023 , y = 710 , clicks = 2)
time.sleep(2)

#Passo 3: Fazer o download da base de vendas
pyautogui.click() #clicar no arquivo
pyautogui.click() #clicar nos 3 pontinhos
pyautogui.click() #clicar no fazer download
time.sleep(5) #esperar o download acabar

#Passo 4: Importar a base de dados de vendas pro Python
# import pandas
# tabela = pandas.read_excel(r'C:\\Users\...') → o r serve para o python transformar em uma raw string
# usar display caso estreja usando o jupyter

#Passo 5: Calcular os indicadores da empresa
# faturamento = tabela["Valor Final"].sum()
# print(faturamento)
# quantidade  = tabela["Quantidade"].sum()
# print(quantidade)

#Passo 6: Enviar um e-mail para a diretoria com os indicadores de venda

# abrir aba:
pyautogui.hotkey('ctrl', 't')


# entrar no link do email:
pyautogui.copy()
pyautogui.hotkey()
pyautogui.press('enter')
time.sleep(5)

# clicar no botao escrever:
pyautogui.click()

# preencher as informações do e-mail:
pyautogui.write()
pyautogui.press("tab") #selecionar o email

pyautogui.press("tab") #pular p o campo de assunto
pyautogui.write("relatorio de vendas")

pyautogui("tab") #pular para o campo de corpo de email


texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: {faturamento}
Qtd de produtos vendidos: {quantidade}

Qualquer dúvida estou a disposição.
Att.,
Dezin7 
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail:
pyautogui.hotkey("ctrl","enter")