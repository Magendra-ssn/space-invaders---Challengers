import math

p=1
q=2
r=3

#converting (p,q,r) to rectangular coordinates

a=p*math.sin(q)*math.cos(r)
b=p*math.sin(q)*math.sin(r)
c=p*math.cos(q)

print(a,b,c)