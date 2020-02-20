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
#def criaDic(mensagem):
#    [dic_inicial.append(simbolo) for simbolo in mensagem if simbolo not in dic_inicial]
    

#Funcao que completa com zeros um numero binario, baseado em um parametro k (tamanho bin)
def binario(b, k):
    binario = bin(b)[2:]
    while len(binario) < k:
        binario = '0' + binario
    return binario

#Salva a saida codificada em um arquivo
def salva_saida(saida, k):
    arq = open("C:/Users/Yuri Oliveira/Desktop/lzw_saida_" + str(k) + ".txt","w+")
    #arq.write(binario(9, k))
    
    for s in saida:
        arq.write(binario(s, k))
    
    arq.close()
    
#Le arquivo contendo a saida do lzw em binario 
def le_saida(k):
    #a primeira sequencia de bits
    saida_lzw = []
    arq = open("C:/Users/Yuri Oliveira/Desktop/lzw_saida_" + str(k) + ".txt","r+")
    conteudo = arq.read()
    print(conteudo)
    for i in range(int(len(conteudo)/k)):
        saida_lzw.append(int(str(conteudo[i*k:(i+1)*k]), 2))
    arq.close()
    return saida_lzw
    
#LZW_WikiPedia

#Mensagem que será codificada    
mensagem = "ABRACADABRA"

#Dicionario 
#dic_inicial = []  #cria um dicionario vazio     
#criaDic(mensagem)   #cria o dicionario inicial baseado na mensagem   
#dic_inicial.sort()  #ordena o dicionario


#Iniciando o dicionario
dic_tamanho = 256
dicionario = [chr(i) for i in range(dic_tamanho)]

#End of File variable
EOF = '`'
#Junta a mensagem com o EOF
mensagem = mensagem + EOF


#faz para K valendo de 9 a 16
for k in range(9,17):
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
        
    print("saidas utilizando k = {}".format(k))
    #print("Dicionario Final:")
    #print(dic)
    print("Saida Codificada:")
    print(saida)
    
    
    salva_saida(saida, k)
    saida_lida = le_saida(k)
    print(saida_lida)


