import matplotlib.pyplot as plt
import math
import lagrange

x_points = [1, 2, 3]
y_points = [math.exp(1), math.exp(2), math.exp(3)]

axe_x = []
axe_y = []
result_lagrange = []

x = 1
pas = 0.05

while x <= 3:
    axe_x.append(x)
    axe_y.append(math.exp(x))
    result_lagrange.append(lagrange.Lagrange(x, x_points, y_points))
    x += pas       


plt.title("Interpolation avec 3 points")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.plot(axe_x, axe_y, label="Fonction exp", color="red")
plt.plot(axe_x, result_lagrange, label="Interpolation de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="black", label="Points d'interpolation")

plt.legend()
plt.show()

# avec 5 points 
plt.figure(2)
x_points = [1, 1.5, 2 , 2.5 , 3]
y_points = [math.exp(1), math.exp(1.5), math.exp(2) , math.exp(2.5) , math.exp(3)]

axe_x = []
axe_y = []
result_lagrange = []

x = 1
pas = 0.05

while x <= 3:
    axe_x.append(x)
    axe_y.append(math.exp(x))
    result_lagrange.append(lagrange.Lagrange(x, x_points, y_points))
    x += pas          # ← correction importante ici

# Tracé
plt.title("Interpolation avec 5 points")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.plot(axe_x, axe_y, label="Fonction exp", color="red")
plt.plot(axe_x, result_lagrange, label="Interpolation de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="black", label="Points d'interpolation")

plt.legend()
plt.show()
