
# Gustavo Faria Cardoso
# Pedro Costa Lyra

from tkinter import filedialog as fd


def separado(texto, char):
    lista = ()
    sete = set(lista)
    while texto.find(char) != -1:
        recorte = texto[:texto.find(char)]
        sete.add(recorte)
        texto = texto[texto.find(char)+len(char):]
    sete.add(texto)
    return sete


def separado2(texto, char):
    lista = []
    while texto.find(char) != -1:
        recorte = texto[:texto.find(char)]
        lista.append(recorte)
        texto = texto[texto.find(char)+len(char):]
    lista.append(texto)
    return lista


def oper(linha, texto):
    resposta = ""
    operacao = ""
    A = separado(texto[linha+1],",")
    B = separado(texto[linha+2],",")
    if texto[linha] == "U":
        operacao = "União"
        resposta = (A | B)
    elif texto[linha] =="I":
        operacao = "Interseção"
        resposta = A.intersection(B)
    elif texto[linha] == "D":
        operacao = "Diferença"
        resposta = (A - B)
    elif texto[linha] == "C":
        operacao = "Produto Cartesiano"
        for i in A:
            for j in B:
                resposta += (f'({i},{j})')
    conjunto1 = texto[linha+1]
    conjunto2 = texto[linha + 2]
    saida = operacao+': conjunto 1 {'+texto[linha+1]+'}, conjunto2 {'+texto[linha+2]+'}. Resultado:'+str(resposta)
    print(saida)


arquivo = open(fd.askopenfilename())
arquivo_s = arquivo.read()

linhas = separado2(arquivo_s, "\n")
nmr_op = int(linhas[0])

for i in range(nmr_op):
    oper(3*i+1, linhas)

