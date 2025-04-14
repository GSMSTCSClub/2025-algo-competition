"""
If Mafan defeats you, Mafan must reach your location before you reach the singularity
let J be distance of Mafan
let K be your distance
If Mafan is further from the origin than you, it must move faster than you to the origin to defeat you
return K/u<=J/v
It may choose to reach you first, but if it can reach you then its speed must exceed yours, if so, it can reach the origin before you from the location that it reaches you.
If Mafan is closer to the orign that you, 
if it reaches the origin before you (not K/u<=J/v), you loses
if it doesn't reach the orign before you then K/u<=J/v
    We can rewrite this inequality to u/K>=v/J, which indicates your angular speed is higher than or equal to Mafan
    Thus, if you can maintain an infinitely small angle with Mafan and still move to the orign first.
    Note that you before Mafan and Mafan cannot catch you if it is not on the same line with you and the origin
    Because you starts first, you can ensure you are not on the same 
    For every angle it tries to turn to reach your line with the origin, you can move the same angle and approach the singularity at the same time. 
    Thus you win 
"""
x,y = map(float,input().split(" "))
a,b = map(float,input().split(" "))
print( (x**2+y**2)<=(a**2+b**2) )