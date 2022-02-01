a, b, c = map(float,input().split())
z=1
def bhaskara(delta):
  delta  = (b*b) - (4*a*c)
  if delta < 0 or a==0:
    return z == 0
  else:
    return delta
  
if z==0:
  print("Impossivel")
else:
  x = -b + (delta)**(1/2)
  y = -b - (delta)**(1/2)
  print("R1 = %.5f"%x)
  print("R2 = %.5f"%y)

8,1*10^22 - 8,1*10^25
69.66*10^33
-149.769*10^41