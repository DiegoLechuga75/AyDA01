import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    datos = pd.read_csv("m1.csv", sep=";")
    datosDos = pd.read_csv("m2.csv", sep=";")
    
    x = datos.N
    y = datos.Tiempo
    yy = datosDos.Tiempo
    
    plt.plot(x, y, x, yy)
    plt.ylabel("Tiempo")
    plt.xlabel("N")
    plt.title("Burbuja vs Inserción")
    plt.legend(('burbuja','insercion'),prop={'size':10})
    plt.grid()
    plt.show()