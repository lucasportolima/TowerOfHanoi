def hanoi(n):
    discos = n
    tamanhoMax = int(2 ** discos) - 1
    sequenciaPares = []
    sequenciaImpares = []
    indexPar = 0
    indexImpar = 0

    if discos % 2 == 0:
        sequenciaPares = ["1-->2", "2-->3", "3-->1"]
        sequenciaImpares = ["1-->3", "1-->2", "3-->2"]
    else:
        sequenciaPares = ["1-->3", "3-->2", "2-->1"]
        sequenciaImpares = ["1-->2", "1-->3", "2-->3"]

    for i in range(0,tamanhoMax):
        if i % 2 == 0:
            if indexPar > 2:
                indexPar = 0
            print(sequenciaPares[indexPar])
            indexPar += 1
        else:
            if indexImpar > 2:
                indexImpar = 0
            print(sequenciaImpares[indexImpar])
            indexImpar += 1
                     

hanoi(3)