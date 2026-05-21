from datetime import datetime #datetime é uma classe do módulo datetime, Funciona para trabalhar com datas e horas
# o 1 datetime é o nome do módulo e o 2 datetime é o nome da classe dentro do módulo datetime
s = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
print(s)

d,m,a = s.split("/")

d = int(d)
m = int(m)
a = int(a)
print(d)
print(m)
print(a)
data = datetime.strptime(s,"%d/%m/%Y")
print(data)
print(data.strftime("%d/%m/%Y"))

#strptime - passa uma string e um formato e retorna um objeto datetime
#strftime - passa um objeto datetime e um formato e retorna uma string formatada

x = int(input("Informe um número: "))
d = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")
print(x)
