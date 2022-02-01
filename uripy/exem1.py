def maior_primo(n):
    k = n        
    while k > 1 and e_primo(k)==False:
        k = k - 1
    return k

def e_primo(k):

    primo = True    
    div = 2

    while k>div:
    
        if k % div == 0:
            primo = False
        div = div + 1
            
    return primo