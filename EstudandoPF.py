'''
import random
n = random.randint(0,10)

resp = int(input('Qual o seu chute?: '))

tentativa = 1

print(n)
while tentativa < 5 and resp != n:
    print('Voce errou')
    print('Tente novamente')
    resp = int(input('Qual o seu chute?: '))
    tentativa+=1

if resp == n:
    print('Voce acertou')
else:
    print('Voce perdeu')
'''
'''
def calculando_log(x,b):
    valor = x/b
    log = valor / b
    contador=2
    while log > b:
        valor_novo = valor / b
        log = valor / b
        contador += 1
    return contador
x=9
b=2
print(calculando_log(x,b))


def conta_letras(palavra):
    i=0
    letra=0
    while i<len(palavra):
        if palavra[i] == 'a':
            letra+=1
        i+=1
    return letra
palavra = 'antonio'
print(conta_letras(palavra))
'''
'''
def palindromo(palavra):
    if palavra[:len(palavra)] == palavra[len(palavra)::-1]:
        return 'é palindromo'
    else:
        return 'nao é palindromo'
palavra = 'ete'
#palavra = 'antonio'
print(palindromo(palavra))
'''
'''
def positivos(numeros):
    i=0
    lista_positivos = []
    while i<len(numeros):
        if numeros[i] > 0:
            lista_positivos.append(numeros[i])
        i+=1
    return lista_positivos
numeros = [1,2,-1,-3,1]
print(positivos(numeros))
'''
'''
def posicao(email):
    i=0
    while i<len(email):
        if email[i] == '@':
            arroba = i+1
        i+=1
    return arroba
email = 'antonio@gmail'
print(posicao(email))
'''
'''
def nome_email(email):
    i=0
    while i < len(email):
        if email[i] == '@':
            arroba = i
            nome = email[:arroba]
        i+=1
    return nome
email = 'antoniofuziy@gmail.com'
print(nome_email(email))
'''

'''
i=0
soma=0
maior=0
lista_vazia=[]
for numero in range(0,10):
    numero = int(input('digite um numero: '))
    lista_vazia.append(numero)
while i < len(lista_vazia):
    if maior < lista_vazia[i]:
        maior = lista_vazia[i]
    soma+=lista_vazia[i]
    i+=1
print(soma)
print(maior)
'''
'''
i=0
lista_mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes=str(input('Qual o mês que você deseja saber o número correspondente? :'))
while i < len(lista_mes) and mes in lista_mes:
    if mes == lista_mes[i]:
        print(i+1)
    i+=1
'''

#DEU ERRADO
'''
i=0
lista_vazia=[]
palavra = input('Digite uma palavra: ')
if palavra[0] == 'a' or 'A':
    lista_vazia.append(palavra)
elif palavra == 'fim':
    print(lista_vazia)

while palavra != 'fim':
    palavra = input('Digite uma palavra: ')
    if palavra[0] == 'a' or 'A':
        lista_vazia.append(palavra)
print(lista_vazia)
'''
'''
lista_vazia = []

n = int(input('Digite um numero: '))

while n > 0:
    lista_vazia.append(n)
    n = int(input('Digite um numero: '))

lista_vazia.reverse()
print(lista_vazia)
'''
'''
def numero_no_indice(lista_numeros):
    i=0
    lista_vazia=[]
    while i < len(lista_numeros):
        if lista_numeros[i] == i:
            lista_vazia.append(lista_numeros[i])
        i+=1
    return lista_vazia
lista_numeros=[0,1,3,2,4,6,7]
print(numero_no_indice(lista_numeros))
'''
'''
def estritamente_crescente(lista_numeros):
    i=0
    lista_vazia=[]
    maior=0
    while i<len(lista_numeros):
        if lista_numeros[i] > maior:
            lista_vazia.append(lista_numeros[i])
            maior = lista_numeros[i]
        i+=1
    return lista_vazia

lista_numeros=[0,1,2,3,2,1,4]
print(estritamente_crescente(lista_numeros))
'''
'''
def eh_crescente(lista_numeros):
    i=0
    maior=0
    lista_vazia=[]
    while i<len(lista_numeros):
        if maior < lista_numeros[i]:
            maior = lista_numeros[i]
            lista_vazia.append(maior)
            if len(lista_numeros) > len(lista_vazia):
                return False
        i+=1
    print(len(lista_numeros))
    print(len(lista_vazia))
    return True
lista_numeros=[0,1,2,3,4,5,6,7]
#lista_numeros=[0,1,2,5,1,1]
print(eh_crescente(lista_numeros))
'''
'''
def inverte_lista(lista_numeros):
    i=len(lista_numeros)-1
    lista_vazia=[]
    while i >= 0:
        lista_vazia.append(lista_numeros[i])
        i-=1
    return lista_vazia

lista_numeros=[0,1,2,3,4]
print(inverte_lista(lista_numeros))
'''
'''
def soma_impares(lista):
    i=0
    soma=0
    lista_soma=[]
    while i<len(lista):
        if lista[i]%2 > 0:
            lista_soma.append(lista[i])
            soma += lista[i]
        i+=1
    return soma

lista=[0,1,2,3]
print(soma_impares(lista))
'''

#NAO DEU CERTO
'''
def acha_bigramas(palavra):
    i=0
    lista_bigramas=[]
    while i < len(palavra):
         lista_bigramas.append(palavra[i:i+2])
         i+=1
    return lista_bigramas

palavra = 'banana'
print(acha_bigramas(palavra))
'''

'''
def capitaliza(palavra):
    i=0
    while i < len(palavra):
        string = palavra[0].upper() + palavra[1:i+1]
        i+=1
    return string

palavra='banana'
print(capitaliza(palavra))
'''
'''
def alunos_impares(lista):
    i=0
    lista_impares=[]
    while i < len(lista):
        if i % 2 != 0:
            lista_impares.append(lista[i])
        i+=1
    return lista_impares

lista=['antonio','joao','isa','lari','fernando','mariana','pedro']
print(alunos_impares(lista))
'''
'''
def separa_trios(lista_alunos):
    i=0
    lista_trios=[]
    while i<len(lista_alunos):
        lista_trios.append(lista_alunos[i:i+3])
        i+=1
    return lista_trios

lista_alunos=['antonio','joao','isa','lari','fernando','mariana','pedro']
print(separa_trios(lista_alunos))
'''
'''
def remove_vogais(palavra):
    i=0
    while i<len(palavra):
        if palavra[i] == 'a' or palavra[i]== 'e' or palavra[i]=='i' or palavra[i]=='o' or palavra[i]=='u':
            palavra[i].clear()
        i+=1
    return palavra

palavra='antonio'
print(remove_vogais(palavra))
'''
'''
def conta_bigramas(palavra):
    dic={}
    i=0
    while i < len(palavra)-1:
        bigrama = palavra[i] + palavra[i+1]
        if bigrama in dic:
            dic[bigrama]+=1
        else:
            dic[bigrama] = 1
        i+=1
    return dic
palavra='banana nanica'
print(conta_bigramas(palavra))
'''
'''
def aniversariantes_setembro(dicionario):
    dic={}
    for k,v in dicionario.items():
        if dicionario[k][3:5] == '09':
            dic[k] = v
    return dic
dicionario={'antonio':'22/05/2001', 'mariana':'22/09/1981'}
print(aniversariantes_setembro(dicionario))
'''

def calcula_tempo(dicionario):
    dic={}
    for k,v in dicionario.items():
        dic[k]=(200/v)**(1/2)
    return dic

dicionario={'antonio':'2','joao':'1','ramon':'0.5'}
print(calcula_tempo(dicionario))