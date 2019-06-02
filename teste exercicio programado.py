with open('teste exercicio.py','r') as arquivo:
    conteudo = arquivo.read()
i=0
conteudo = conteudo.upper()
if 'BANANA' in conteudo:
    i+=1
print(i)
        