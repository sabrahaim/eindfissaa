import matplotlib.pyplot as plt
import pyvisa
from model import ExperimentZonnecel


def graph():
    U0_U1_karakteristiek = ExperimentZonnecel("ASRL3::INSTR")

    mean_currents, mean_voltages, error_voltages, error_currents = U0_U1_karakteristiek.IU(0, 3.3, 3)


    # plt.plot(voltages_U0, voltages_PV, 'o')
    # plt.xlabel("Spanning voor bepalen weerstand")
    # plt.ylabel("Spanning door zonnepaneel")
    # plt.show()

    plt.plot(mean_voltages, mean_currents, "o")
    plt.xlabel("Spanning PV")
    plt.ylabel("Stroomsterkte PV")
    plt.show()


if __name__ == "__main__":
    graph()
