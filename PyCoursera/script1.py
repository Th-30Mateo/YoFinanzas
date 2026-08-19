import os

file = open("spider.txt", "r")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

import os

# Obtenemos la lista de todos los archivos y subcarpetas del directorio actual
contenido = os.listdir()

print("Elementos encontrados en el directorio actual:")
for elemento in contenido:
    print("-", elemento)
# Obtenemos el valor de una variable de entorno del sistema (por ejemplo, 'PATH' o 'USER')
# Si la variable no existe, podemos definir un valor por defecto ('No disponible')
user_system = os.environ.get('USER', 'No disponible')
path_system = os.environ.get('PATH', 'No disponible')

print("Usuario actual del sistema operativo:", user_system)
print("Rutas del PATH configuradas:", path_system)