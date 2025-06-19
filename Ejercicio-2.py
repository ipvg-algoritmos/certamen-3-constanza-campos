## Problema 2: Análisis de Notas de Evaluación (35 pts)
#**Enunciado:**  
#En una clase, se registran las notas de 3 estudiantes en 3 asignaturas. El profesor necesita saber los promedios y si todos aprobaron, 
# además de alertar si algún estudiante tiene bajo rendimiento.
#**Indicaciones paso a paso:**
#1. Crea una matriz 3x3 para guardar las notas.
#2. Calcula el promedio de cada estudiante (por fila) y de cada asignatura (por columna).
#3. Verifica si todos los estudiantes aprobaron (nota >= 4.0).
#4. Muestra una alerta si algún promedio individual es menor a 3.5.
matriz = [[" ", " ", " "],
           [" ", " ", " "],
            [" ", " ", " "]]
notas=[]
estudiantes = 3
asignaturas = 3

for fila in range(3):
    suma = 0
    for col in range(3):
        int(input("Ingrese notas: "))
    