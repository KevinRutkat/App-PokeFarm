import pygetwindow as gw

# Obtener y mostrar todas las ventanas abiertas
ventanas = gw.getAllTitles()

for ventana in ventanas:
    print(ventana)  # Imprime los nombres de todas las ventanas abiertas
