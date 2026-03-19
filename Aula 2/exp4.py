print("Validar data")
s = input()
data = s.split("/") # split: divide a data (variável s) em 3 partes
dia = int(data[0]) #primeira parte convetida me inteiro
mes = int(data[1])
ano = int(data[2])

#calcula se o ano é bissexto
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
#calcula o maior número de dias de acordo com o número no mes
m = 31
if mes in [4, 6, 9, 11]: m = 30
if mes == 2:
    if bissexto == True: m == 29
    else: m = 28
#teste a data
if dia >= 1 and dia <= m and mes >=1 and mes <= 12 and ano <= 2100:
    print("A data informada é válida")
else:
    print("A data informada não é válida")