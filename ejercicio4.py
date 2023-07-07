#Dibujar en un mismo grafico la evolución de temperatura de un día en particular pero de dos
#ciudades diferentes de Argentina que estén muy distantes una de otra.
import matplotlib.pyplot as plt
listax = []
listaycom = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 5, 5, 5, 5 , 5, 5, 5, 4, 4, 3, 3, 3]
listaytil = [9, 8, 8, 7, 6, 5, 4, 4, 4, 6, 13, 17, 19, 21, 21, 22 , 22, 22, 20, 16, 15, 13, 11, 10]
for i in range(24):
    listax.append(i)    
plt.plot(listax, listaycom)
plt.plot(listax, listaytil)
plt.title('Temperaturas del 30/06/2023 en Comodoro y Tilcara')
plt.xlabel('Hora')
plt.ylabel('Temperatura')
plt.show()