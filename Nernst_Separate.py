import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Global Constants
Faraday = 96485
R = 8.314
Temp = 310.15

class Nernst():

    def equilibrium(self, T, z, Xi, Xo):
        """
        :param T: Temperature in Kelvins
        :param z: Valence of ionic species
        :param Xi: Inner membrane concentration
        :param Xo: Outer membrane concentration
        :return: Membrane potential for single species
        """
        GasIons = (R*T)/(z*Faraday)
        Concentrations = np.log(Xo/Xi)
        membranePotential = GasIons*Concentrations
        return membranePotential

    def viz(self, volts, ion):
        plt.scatter([0,1,2,3], [0, 0, volts, volts])
        plt.plot([0,1,2,3], [0, 0, volts, volts])
        plt.ylim(-100,100)
        plt.xlim(0,3)
        xlabs = np.arange(0, 3, 1.0)
        bins = ['','Channel Closed', 'Channel Open','']
        plt.xticks(xlabs, bins)
        plt.text(2, volts+5, str(round(volts, 2)))
        plt.title("Membrane Potential Single Ion Species: "+str(ion))
        plt.xlabel("Membrane Permeability")
        plt.ylabel("Voltage (mV)")
        plt.show()

if __name__ == "__main__":
    file = pd.read_csv('C:\\Users\\ajh\\Desktop\\ions.txt',
                       names=['name', 'charge', 'temperature', 'inner', 'outer'],
                       dtype={'name':str, 'charge':int, 'temperature':int, 'inner':int, 'outer':float},
                       skiprows=1)

    df = pd.DataFrame(file)
    Nernst = Nernst()
    for index,row in file.iterrows():
        potential = Nernst.equilibrium(Temp,row.charge,row.inner,row.outer)
        Nernst.viz(potential*1000, df.name[index])
