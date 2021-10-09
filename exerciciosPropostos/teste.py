def gerarNota():
    def nota(n1, n2):
        print((n1 + n2) / 2)
    return nota

nota_gerada = gerarNota()
nota_gerada(5, 7)