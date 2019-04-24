import sys
import csv

def leArquivo(sys.argv[1]):
    arq = open(sys.argv[1], 'r')
    dic={}
    lst = []
    conteudo=arq.readline()
    
    

    

    while conteudo!='':
        if conteudo = '#':
            conteudo=arq.readline()
            dic[conteudo]
        conteudo=conteudo.split()
        
        lst.append(conteudo)
        conteudo=arq.readline()


def escreveCSV(dic):
    with open('resultados.csv', 'w') as f:
        for key in dic.keys():
            f.write("%s,%s\n"%(key,dic[key]))
        f.close()