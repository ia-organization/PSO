import sys
import csv

def leArquivo(sys.argv[1]):
    arq = open(sys.argv[1], 'r')
    
    lst = []
    conteudo=arq.readline()
    
    

    

    while conteudo!='':
        if conteudo = '#':
            conteudo=arq.readline()
        conteudo=conteudo.split()
        lst.append(conteudo)
        conteudo=arq.readline()


def escreveCSV(lst):
    with open('resultados.csv', mode='w') as resultados_file:
    gbest_writer = csv.writer(resultados_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    gbest_writer.writerow(lst)