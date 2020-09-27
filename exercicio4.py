palavra=  ("arroz")
palavraaocontrario =  ("zorra")
def parametroinverso(palavra,palavraaocontrario):
     if palavraaocontrario == palavra[::-1]:
        return True
        print("uma palavra é o contrario da outra")
     else:
        return False
        print("uma palavra não é o contrario da outra")