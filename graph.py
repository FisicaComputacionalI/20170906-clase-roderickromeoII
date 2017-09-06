import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del eje X
x = [6000,7000,8000,9000,10000]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y = [73,80,85,87,89]
# Grafica el vector x contra el vector y
pl.plot(x,y, 'r*')
pl.plot(x,y)
# Crea un vector (arreglo) con los valores del eje X
x1 = [7000,8000,9000,10000,11000]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y1 = [80,83,85,86,88] 
# Grafica el vector x contra el vector y
pl.axis ([0,100, 5000,12000])
pl.plot(x1,y1)
pl.plot(x1,y1, 'gD')
pl.ylabel('Voltaje [V]')
pl.xlabel('Eficiencia [%]')
#Guarda la grafica en el formato png
pl.savefig('graph.png')
pl.show()
