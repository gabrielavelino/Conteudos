def baska():

    det = (B*B) - (4*A*C)


    if det<0 or A==0:
        print("Impossivel calcular")
    else:    

        r1 = (-B + det**(1/2))/(2*A)
        r2 = (-B - det**(1/2))/(2*A)

    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)

A, B, C = map(float,input().split())

baska()