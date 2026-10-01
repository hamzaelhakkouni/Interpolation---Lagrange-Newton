import math
def CalculateCoefficient(i , x_points , x):
    produit = 1 
    for j in range(i):
        produit = produit * ( x - x_points[j])

    return produit

def DevidedDifference(x_points , y_points):
    n = len(x_points)
    matrice = [[0.0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            matrice[j][k] = 0
    for j in range(n):
        matrice[j][0] = y_points[j]
    for j in range(1 , n):
        for k in range(n - j ):
            matrice[k][j] = (matrice[k+1][j-1] - matrice[k][j-1] ) / (x_points[j + k] - x_points[k])
    return matrice 

def ConstruirePolynome(x_points , y_points , x):
    n = len(x_points)
    matrice = DevidedDifference(x_points , y_points)
    result = matrice[0][0]
    for j in range(1, n):
        result += matrice[0][j] * CalculateCoefficient(j, x_points, x)
    return result


# Exemple de test avec la fonction ln(x) et 3 points 
#On Va calculer ln(1.5) et P(1.5)
print("ln(1.5) = ", math.log2(1.5))

#maintenant calculons le polynome a partir des points ( 1 , ln(1)) , ( 2 , ln(2)) , (2.5 , ln(2.5))
x_points = [ 1 , 2 , 2.5]
y_points = [math.log2(1) , math.log2(2) , math.log2(2.5)]
print("P(1.5) = " , ConstruirePolynome(x_points , y_points , 1.5))   



#maintenat en augmente le nombre de points dans l'intervalle [1 , 2.5]
# (1 , ln(1)) , (1.5 , ln(1.5)) , (2 , ln(2)) , (2.3 , ln(2.3)) , (2.5 , ln(2.5))
print("Apres l'ajout des points :")
print("ln(1.5) = ", math.log2(1.5))
x_points = [ 1 , 1.5 , 2 , 2.3 ,  2.5]
y_points = [math.log2(1) , math.log2(1.5) , math.log2(2) , math.log(2.3), math.log2(2.5)]
print("P(1.5) = " , ConstruirePolynome(x_points , y_points , 1.5))   
    