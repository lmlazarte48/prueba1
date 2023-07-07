#Muestre la evolución de las lluvias mes a mes, a lo largo de un año en algún lugar de Argentina. Escribir en los ejes el nombre correspondiente a lo que se muestra.
#El grafico debe ser del tipo barras y de color rojo.
import matplotlib.pyplot as plt
listax = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
listay = [29.6, 33.1, 41.7, 60.7, 102.9, 114.1, 93.8, 84.4, 54.9, 41.8, 36.9, 35.9]
plt.bar (listax, listay, color='r')
plt.title('Promedio mensual de lluvias en el Bolsón')
plt.xlabel('Meses')
plt.ylabel('Lluvias en mm.')
plt.show()