import numpy as np


# Global Constants
Faraday = 96485
R = 8.314


class Nernst():


    def temp(self):
        """
        :args:  none
        :return: Temperature in Kelvins
        """
        C = float(input("Temperature in Celsius"))
        K = C + 273.15
        return K


    def valence(self):
        """
        :args: none
        :return: valence shell of ionic species
        """
        v = int(input("Valence"))
        return v


    def innerConcentration(self):
        """
        :args: none
        :return: Concentration of ion species inside cellular membrane, in millimolars 
        """
        inner = float(input("Inner Concentration (mM)"))
        return inner


    def outerConcentration(self):
        """
        :args: none
        :return: Concentration of ion species outside of cellular membrane, in millimolars 
        """
        outer = float(input("Outer Concentration (mM)"))
        return outer


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


    def viz(self, volts):
        """
        :param volts: Volage in mV
        :return: none
        """
        plt.scatter([0,1], [0, volts])
        plt.plot([0,1], [0, volts])
        plt.ylim(-100,100)
        plt.xlim(0,2)
        plt.xticks(np.arange(0, 2, 1.0))
        plt.title("Membrane Potential Single Ion Species")
        plt.xlabel("Time")
        plt.ylabel("Voltage (mV")
        plt.show()

if __name__ == "__main__":
    Nernst = Nernst()
    temperature = Nernst.temp()
    charge = Nernst.valence()
    inner = Nernst.innerConcentration()
    outer = Nernst.outerConcentration()
    membrane = Nernst.equilibrium(temperature, charge, inner, outer)
    print("Result: " + str(membrane))
    Nernst.viz(membrane*1000)

