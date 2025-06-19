## Problema 1: Control de Temperatura en un Invernadero (25 pts)

#**Enunciado:**  
#Un agricultor necesita monitorear la temperatura de su invernadero para asegurar el crecimiento óptimo de sus plantas. 
# Debes ayudarle a identificar si las temperaturas registradas están dentro del rango adecuado y alertar si alguna es peligrosa.

#**Indicaciones paso a paso:**
#1. Solicita al usuario que ingrese 5 temperaturas.
#2. Guarda las temperaturas en una lista.
#3. Calcula el promedio y la temperatura máxima.
#4. Verifica si todas las temperaturas están entre 15°C y 30°C.
#5. Si alguna temperatura está fuera de 10°C–35°C, muestra una advertencia.

temperatura_invernadero = []
for i in range(5):
    temperatura_ingresada = int(input("ingresa una temperatura:"))
    temperatura_invernadero.append(temperatura_ingresada)

promedio_temperatura = sum(temperatura_invernadero)/len(temperatura_invernadero)
print(f"El promedio de la temperatura del invernadero es: {promedio_temperatura}")

temperatura_max = max(temperatura_invernadero)
print(f"La máxima temperatura alcanzada: {temperatura_max}")

if temperatura_ingresada >= 15 and temperatura_ingresada <=30:
    print("La temperatura está en el rango optimo")

else:
     temperatura_ingresada < 15 or temperatura_ingresada > 30
        
print("¡ADVERTENCIA! La temperatura no es optima")
        