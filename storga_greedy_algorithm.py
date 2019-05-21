old_fita = [1, 4, 7, 9, 3, 9, 8]
new_fita = []

while len(old_fita) > 0:
    sel = min(old_fita)
    new_fita.append(sel)
    ind = old_fita.index(sel)
    del old_fita[ind]

print(new_fita)
