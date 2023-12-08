import pyvisa
import numpy as np 

from controller import ArduinoZonnecel, list_devices

class ExperimentZonnecel:
    def __init__(self, port):
        rm = pyvisa.RecourceManager("@py")
        self.device = ArduinoZonnecel(port = port)
    
    def IU(self, start, stop, repeats):
        for value_volt in np.arange(start, stop, 3.3/1023):
            voltages_U1 = []
            voltages_U2 = []
            for value in range(repeats):
                self.device.set_output_voltage(value=value_volt)
                voltage_U1 = self.device.get_input_voltage(channel=1)
                voltages_U1.append(voltage_U1)
                voltage_U2 = self.device.get_input_voltage(channel=2)
                voltages_U2.append(voltage_U2)

        self.device.set_output_value(value=0)
        return voltages_U1, voltages_U2