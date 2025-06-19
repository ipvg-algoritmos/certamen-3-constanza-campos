## Problema 3: Sistema de Acceso Condicional (20 pts)

#**Enunciado:**  
#En una empresa, el acceso a una zona restringida depende de la edad, el rol de supervisor y la autorización especial. Debes crear un sistema que determine si una persona puede ingresar.

#**Indicaciones paso a paso:**
#1. Solicita al usuario su edad, si es supervisor y si tiene autorización.
#2. Verifica si puede acceder: debe ser mayor de edad y cumplir al menos una condición (ser supervisor o tener autorización).
#3. Muestra un mensaje indicando si el acceso está permitido o denegado.
edades = int(input("ingrese la edad: "))
supervisor = input("ingrese si es supervisor escribiendolo:")
autorizar = input("ingrese si está autorizado escribiendolo:")
while True:
    if edad <