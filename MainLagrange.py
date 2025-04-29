#   Codigo que implementa la interpolacion de Lagrange 
#   para ajustar un conjunto de datos
#   
#           Autor:
#   Gilbert Alexander Mendez Cervera
#   mendezgilbert222304@outlook.com
#   Version 1.01 : 08/04/2025

import numpy as np
import matplotlib.pyplot as plt

# Nuevos puntos dados (posición en metros, deformación en mm)
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Calcular la deformación en x = 1.25
x_eval = 1.25
y_eval = lagrange_interpolation(x_eval, x_points, y_points)
print(f"Deformación esperada en x = {x_eval} m: {y_eval:.4f} mm")

# b) Graficar la interpolación en el rango [0.5, 2.0]
x_values = np.linspace(0.5, 2.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Gráfica
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Puntos dados")
plt.scatter(x_eval, y_eval, color="green", label=f"Interpolado en x={x_eval}")
plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.title("Interpolación de Lagrange - Deformación en una Viga")
plt.legend()
plt.grid(True)
plt.savefig("interpolacion_viga.png")
plt.show()

""" 
#EJERCICIO 2
# Datos de profundidad (cm) y temperatura (°C)
x_points = np.array([1.0, 2.5, 4.0, 5.5])
y_points = np.array([85, 78, 69, 60])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estimar la temperatura a una profundidad de 3.0 cm
x_eval = 3.0
y_eval = lagrange_interpolation(x_eval, x_points, y_points)
print(f"Temperatura estimada a una profundidad de {x_eval} cm: {y_eval:.2f} °C")

# b) Graficar la interpolación en el rango [1.0, 5.5]
x_values = np.linspace(1.0, 5.5, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Gráfica
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos experimentales")
plt.scatter(x_eval, y_eval, color="green", label=f"Estimación en x={x_eval}")
plt.xlabel("Profundidad (cm)")
plt.ylabel("Temperatura (°C)")
plt.title("Interpolación de Lagrange - Temperatura en un bloque de motor")
plt.legend()
plt.grid(True)
plt.savefig("interpolacion_temperatura_motor.png")
plt.show()
"""

"""
#EJERCICIO 3
import numpy as np
import matplotlib.pyplot as plt

# Nuevos puntos de interpolación según la imagen
x_points = np.array([2.0, 4.0, 6.0, 8.0])  # Altitud (km)
y_points = np.array([2500, 2300, 2150, 2050])  # Consumo (kg/h)

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estimación del consumo a 5 km de altitud
altitud_objetivo = 5.0
consumo_estimado = lagrange_interpolation(altitud_objetivo, x_points, y_points)
print(f"Consumo estimado a {altitud_objetivo} km de altitud: {consumo_estimado:.2f} kg/h")

# b) Gráfica de la interpolación
x_values = np.linspace(min(x_points), max(x_points), 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(8,5))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales")
plt.scatter([altitud_objetivo], [consumo_estimado], color="green", label=f"Estimación a {altitud_objetivo} km")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.title("Interpolación de Lagrange - Consumo de Combustible")
plt.legend()
plt.grid(True)
plt.savefig("interpolacion_consumo_combustible.png")
plt.show()
"""

