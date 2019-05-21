def apagar(qte, num):
    
    qte_apagado = 0

    resul = ""

    for i in range(0, len(num)):
        #print(resul)
        if i + 1 != len(num):
            if num[i] <= num[i + 1]:
                qte_apagado += 1
            else:
                resul += num[i]
            if qte_apagado == qte:
                resul += num[i + 1:]
                break
    print(resul)
        
num = '1231239'
apagar(3, num)
num = '10000019'
apagar(4, num)
num = '22378950'
apagar(4, num)

