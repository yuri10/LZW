# -*-  coding: iso-8859-1 -*-
# using Python version 3.7
"""
created on Mon Dec 23 18:04:19 2019
@author: Yuri Oliveira
"""
import time
import os
import matplotlib.pyplot as plt

#Verifica se existe o simbolo no dicionario
#Retorna o seu indice, caso exista.
def existeNoDic(simbolo):
    if simbolo in dic:
        return dic.index(simbolo)
    return -1 

#Funcao que completa com zeros um numero binario, baseado em um parametro k (tamanho bin)
def binario(b, k):
    binario = bin(b)[2:].zfill(k)
    return binario

#Salva a saida codificada em um arquivo
def salva_saida(saida, k):
    arq = open("C:/Users/Yuri Oliveira/Desktop/lzw_saida_" + str(k) + ".txt","w+")
    
    for s in saida:
        arq.write(binario(s, k))
    
    arq.close()
    
#Le arquivo contendo a saida do lzw em binario 
def le_saida(k):
    #a primeira sequencia de bits
    saida_lzw = []
    arq = open("C:/Users/Yuri Oliveira/Desktop/lzw_saida_" + str(k) + ".txt","r+")
    conteudo = arq.read()
    #print(conteudo)
    for i in range(int(len(conteudo)/k)):
        saida_lzw.append(int(str(conteudo[i*k:(i+1)*k]), 2))
    arq.close()
    return saida_lzw

def lzw_decode(leitura):

    #Iniciando o dicionario
    dic_tamanho = 256
    dicionario = dict([(x, chr(x)) for x in range(dic_tamanho)])
    
    w = ""
    resultado=""
    proximo=256
    #LZW DECODE

    for dado in leitura:
        if not (dado in dicionario):
            dicionario[dado] = w + w[0]
        resultado += dicionario[dado]
        if not(len(w)==0):
            dicionario[proximo] = w + (dicionario[dado][0])
            proximo+=1
        w = dicionario[dado]

    return resultado
    
#LZW_WikiPedia

#Mensagem que será codificada  

arq = open("C:/Users/Yuri Oliveira/Desktop/corpus16MB.txt","r", encoding = 'iso-8859-1')
mensagem = arq.read()
#mensagem = "ABRACADABRA"
arq.close()
#Dicionario 
#dic_inicial = []  #cria um dicionario vazio     
#criaDic(mensagem)   #cria o dicionario inicial baseado na mensagem   
#dic_inicial.sort()  #ordena o dicionario


#Iniciando o dicionario
dic_tamanho = 256
dicionario = [chr(i) for i in range(dic_tamanho)]

#End of File variable
EOF = dicionario[3]
#Junta a mensagem com o EOF
mensagem = mensagem + EOF

tempos_k = []

#faz para K valendo de 9 a 16
for k in range(12,17):
    #pega o tempo de execucao
    tempo_inicial = time.time()
    #Saida Codificada
    saida = []
    #variaveis auxiliar
    I = ''
    i=0
    dic = dicionario[0:]
    #dic = dic_inicial   #para cada iteração, "zera" o dicionario
    for i in range(len(mensagem)):    
        c = mensagem[i]
        #verifica se existe o simbolo atual e o proximo no dicionario
        if existeNoDic(I+c) != -1:
            I = I+c
        #senao existir, adiciona o indice do simbolo atual na saida e
        #adiciona no dicionario o simbolo atual + proximo como novo indice
        else:
            saida.append(existeNoDic(I))
            #adiciona o novo simbolo no dicionario (se ele não estiver cheio)
            if len(dic) < (2**k):
                dic.append(I+c)
            I = c
        #Enquanto nao pegar todos os simbolos, continua rodando o looping
        if i < len(mensagem):
            continue
        else:
            saida.append(existeNoDic(I))
        
    #print("saidas utilizando k = {}".format(k))
    #print("Dicionario Final:")
    #print(dic)
    #print("Saida Codificada:")
    #print(saida)
    
    tempos_k.append(time.time() - tempo_inicial)
    salva_saida(saida, k)
    #saida_lida = le_saida(k)
    #print(saida_lida)


#graficos
'''    
statinfo = os.stat("C:/Users/Yuri Oliveira/Desktop/corpus16MB.txt")
tamanho_corpus = statinfo.st_size

tamanho_saidas = []
for i in range(9,14):
    statinfo = os.stat("C:/Users/Yuri Oliveira/Desktop/lzw_saida_"+ str(i) + ".txt")
    tamanho_saidas.append(int(statinfo.st_size/8))

#RC - Razão de Compressão (tamanho original / tamanho comprimido)
RC = [tamanho_corpus/ts for ts in tamanho_saidas]

#plt.bar(list(range(9,14)), RC, color = 'blue')
plt.title('RC x K')
plt.ylabel('Razão de Compressão')
plt.xlabel('K')
plt.plot(list(range(9,14)), RC)
plt.grid(True)


#Grafico tempo x k
plt.title('tempo x K')
plt.ylabel('tempo')
plt.xlabel('K')
plt.plot(list(range(9,14)), tempos_k)
plt.grid(True)

'''

