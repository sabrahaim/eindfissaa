import pyvisa
import numpy as np 

from controller import ArduinoZonnecel, list_devices

class ExperimentZonnecel:
    def __init__(self, port):
        rm = pyvisa.ResourceManager("@py")
        self.device = ArduinoZonnecel(port)
    
    def IU(self, start, stop, repeats):
        voltages_U0 = []
        voltages_U2 = []
        voltages_PV = []
        currents_PV = []
        for value_volt in np.arange(start, stop, 3.3/1023):
            for value in range(repeats):
                self.device.set_output_voltage(value=value_volt)
                
                voltages_U0.append(self.device.get_output_value())

                voltage_U1 = self.device.get_input_voltage(channel=1)
                # voltages_U1.append(voltage_U1)

                voltage_U2 = self.device.get_input_voltage(channel=2)
                voltages_U2.append(voltage_U2)

                voltage_PV = 3 * voltage_U1
                voltages_PV.append(voltage_PV)

                current_1 = voltage_U1/(3*10**6)
                current_2 = voltage_U2/4.7
                current_PV = current_2 - current_1
                currents_PV.append(current_PV)


        self.device.set_output_value(value=0)
        return voltages_U0, voltages_PV, currents_PV