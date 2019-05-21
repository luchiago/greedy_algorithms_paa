livros = [0.5, 0.1, 0.3, 0.2, 0.9, 0.8]

livros.sort()

mochila = []

while len(livros) > 0:
    esq = 0
    dire = len(livros) - 1
    if len(livros) == 1:
        mochila.append(livros[esq])
        del livros[esq]
    elif livros[esq] + livros[dire] > 1:
        mochila.append(livros[dire])
        del livros[dire]
    else:
        mochila.append([livros[esq], livros[dire]])
        del livros[esq]
        del livros[dire - 1]
print(mochila)

