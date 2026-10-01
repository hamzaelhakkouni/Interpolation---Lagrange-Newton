import matplotlib.pyplot as plt
import math 
import newton

x_points = [ 1 , 2 , 2.5]
y_points = [math.log2(1) , math.log2(2) , math.log2(2.5)]
result_newton = []
axe_x = []
axe_y = [] 
pas = 0.05 
x = 1 
while x <= 2.5 :
    result_newton.append(newton.ConstruirePolynome(x_points , y_points , x))
    axe_x.append(x)
    axe_y.append(math.log2(x))
    x = x + pas
plt.figure(1)
plt.title("Interpolation avec 3 points")
plt.xlabel("l'axe X")
plt.ylabel("l'axe Y")
plt.grid(True)
plt.plot(axe_x , axe_y , label="La fonction Log2" , color="red")
plt.plot(axe_x , result_newton , label="Le Polynome d'interpolation" , color="green")
plt.scatter(x_points , y_points , color="black" , label="points d'interpolation")
plt.legend()
plt.show()

#maintenant avec 5 points :

x_points = [ 1 , 1.5 , 2 , 2.3 , 2.5]
y_points = [math.log2(1) , math.log2(1.5) , math.log2(2) , math.log2(2.3)  , math.log2(2.5)]
result_newton = []
axe_x = []
axe_y = [] 
pas = 0.05 
x = 1 
while x <= 2.5 :
    result_newton.append(newton.ConstruirePolynome(x_points , y_points , x))
    axe_x.append(x)
    axe_y.append(math.log2(x))
    x = x + pas

plt.figure(2)
plt.title("Interpolation avec 5 points")
plt.xlabel("l'axe X")
plt.ylabel("l'axe Y")
plt.grid(True)
plt.plot(axe_x , axe_y , label="La fonction Log2" , color="red")
plt.plot(axe_x , result_newton , label="Le Polynome d'interpolation" , color="green")
plt.scatter(x_points , y_points , color="black" , label="points d'interpolation")
plt.legend()
plt.show()