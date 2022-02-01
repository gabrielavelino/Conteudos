def remove_repetidos(lista):
    cop = []
    for num in lista:
        
        if num not in cop:
            cop.append(num)
               
    cop.sort()
    return cop

