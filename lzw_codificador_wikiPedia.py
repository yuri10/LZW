# -*- coding: utf-8 -*-
"""
created on Mon Dec 23 18:04:19 2019

@author: Yuri Oliveira
"""

#Verifica se existe o simbolo no dicionario
#Retorna o seu indice, caso exista.
def existeNoDic(simbolo):
    if simbolo in dic:
        return dic.index(simbolo)
    return -1

#Cria o dicionario baseado na mensagem que sera codificada
def criaDic(mensagem):
    [dic.append(simbolo) for simbolo in mensagem if simbolo not in dic]
    

#LZW_WikiPedia

#Mensagem que será codificada    
mensagem = "ABRACADABRA"

#Dicionario 
dic = []    #cria um dicionario vazio
criaDic(mensagem)   #cria o dicionario inicial baseado na mensagem   
dic.sort()  #ordena o dicionario

#Saida Codificada
saida = []
#End of File variable
EOF = '`'
#Junta a mensagem com o EOF
mensagem = mensagem + EOF
#variaveis auxiliar
I = ''
i=0
for i in range(len(mensagem)):    
    c = mensagem[i]
    if existeNoDic(I+c) != -1:
        I = I+c
    else:
        saida.append(existeNoDic(I))
        dic.append(I+c)
        I = c
    if i < len(mensagem):
        continue
    else:
        saida.append(existeNoDic(I))
        
print("Dicionario Final:")
print(dic)
print("Saida Codificada:")
print(saida)

        