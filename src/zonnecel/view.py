import matplotlib.pyplot as plt
import pyvisa
from model import ExperimentZonnecel


def graph():
    U0_U1_karakteristiek = ExperimentZonnecel("ASRL3::INSTR")

    voltages_U0, voltages_PV, currents_PV = U0_U1_karakteristiek.IU(0, 3.3, 1)
    print(voltages_U0)
    print(voltages_PV)

    # plt.plot(voltages_U0, voltages_PV, 'o')
    # plt.xlabel("Spanning voor bepalen weerstand")
    # plt.ylabel("Spanning door zonnepaneel")
    # plt.show()

    plt.plot(voltages_PV, currents_PV, 'o')
    plt.xlabel("Spanning PV")
    plt.ylabel("Stroomsterkte PV")
    plt.show()


if __name__ == "__main__":
    view = graph()
