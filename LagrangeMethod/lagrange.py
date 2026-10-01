import math 

def CalculateLi(x , i , x_points):
    result = 1
    n = len(x_points)
    for j in range(n) :
        if(j != i):
            result = result * ((x - x_points[j]) / (x_points[i] - x_points[j]))
    return result
def Lagrange(x , x_points , y_points):
    result = 0
    n = len(x_points)
    for i in range(n):
        result = result + (y_points[i] * CalculateLi(x , i , x_points))
    return result



# maintenant on va tester avec 3 points :
# On choisit la fonction exp :
# on choisit x = 1.5
# la vraie valeur 
print("Exp(1.5) = " , math.exp(1.5))
# par lagrange
x_points = [1 , 2 , 3]
y_points = [ math.exp(1) , math.exp(2) , math.exp(3)]
r = Lagrange( 1.5 , x_points , y_points)
print("P(1.5) = " , r)

# maintenant on augmente le nombre du points :

# la vraie valeur 
print("Exp(1.5) = " , math.exp(1.5))
# par lagrange
x_points = [1 , 1.5 , 2 , 2.5 , 3]
y_points = [ math.exp(1) , math.exp(1.5) , math.exp(2) , math.exp(2.5) , math.exp(3)]
r = Lagrange( 1.5 , x_points , y_points)
print("P(1.5) = " , r)

# donc si on augmente le nombre des points la précision est augmente
