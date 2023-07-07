#Muestre la evolución de la temperatura tomada cada una hora a lo largo de un día
import matplotlib.pyplot as plt
listax = []
listay = [4, 3, 3, 3, 3, 3, 3, 5, 6, 8, 9, 10, 11, 12, 12, 12 , 11, 11, 11, 11, 10, 11, 10, 9]
for i in range(24):
    listax.append(i)    
plt.plot(listax, listay)
plt.xlabel('Hora')
plt.ylabel('Temperatura')
plt.show()