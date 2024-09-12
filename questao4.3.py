qnotas = int(input("Quantas notas serão definidas? "))
notas = []
for i in range(qnotas):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)
media = sum(notas)/qnotas
print(f"Sua media é {media:.2f}")

"""
podia ser feito como
quantidadeNotas = int(input("informe a quantidade de notas: "))

x = 1
soma = 0
while (x<= quantidadeNotas):
    nota = float(input(f"Informe a {x} nota: "))
    x+=1
    soma +=nota
    
"""