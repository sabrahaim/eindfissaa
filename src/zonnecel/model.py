import pyvisa
import numpy as np 

from zonnecel.controller import ArduinoZonnecel, list_devices

class ExperimentZonnecel:
    def __init__(self, port):
        rm = pyvisa.ResourceManager("@py")
        self.device = ArduinoZonnecel(port)
    
    def IU(self, start, stop, repeats):
        mean_currents = []
        mean_voltages = []
        error_voltages = []
        error_currents = []

        mean_powers = []
        mean_resistances = []
        error_powers = []
        error_resistances = []

        for value_volt in np.arange(start, stop, 3.3/1023):
            voltages_U0 = []
            voltages_U2 = []
            voltages_PV = []
            currents_PV = []

            powers_PV = []
            resistances_PV = []
            for value in range(repeats):
                self.device.set_output_voltage(value=value_volt)
                
                voltages_U0.append(self.device.get_output_value())

                voltage_U1 = self.device.get_input_voltage(channel=1)
                # voltages_U1.append(voltage_U1)

                voltage_U2 = self.device.get_input_voltage(channel=2)
                # voltages_U2.append(voltage_U2)

                voltage_PV = 3 * voltage_U1
                voltages_PV.append(voltage_PV)

                current_1 = voltage_U1/(10**6)
                current_2 = voltage_U2/4.7
                current_PV = current_2 + current_1
                currents_PV.append(current_PV)

                power_PV = voltage_PV*current_PV
                powers_PV.append(power_PV)

                resistance_PV = voltage_PV/current_PV
                resistances_PV.append(resistance_PV)
            
            mean_currents.append(np.mean(currents_PV))
            mean_voltages.append(np.mean(voltages_PV))
            
            error_voltages.append(np.std(voltages_PV)/np.sqrt(repeats))
            error_currents.append(np.std(currents_PV)/np.sqrt(repeats))

            mean_powers.append(np.mean(powers_PV))
            mean_resistances.append(np.mean(resistances_PV))

            error_powers.append(np.std(powers_PV)/np.sqrt(repeats))
            error_resistances.append(np.std(resistances_PV)/np.sqrt(repeats))



        self.device.set_output_value(value=0)
        return mean_voltages, mean_currents, error_voltages, error_currents, mean_powers, mean_resistances, error_powers, error_resistances
    
    def PR(self, start, stop, repeats):
        mean_powers = []
        mean_resistances = []
        error_powers = []
        error_resistances = []

        for value_volt in np.arange(start, stop, 3.3/1023):
            voltages_U0 = []
            voltages_U2 = []
            voltages_PV = []
            currents_PV = []
            powers_PV = []
            resistances_PV = []
            for value in range(repeats):
                self.device.set_output_voltage(value=value_volt)
                
                voltages_U0.append(self.device.get_output_value())

                voltage_U1 = self.device.get_input_voltage(channel=1)
                # voltages_U1.append(voltage_U1)

                voltage_U2 = self.device.get_input_voltage(channel=2)
                # voltages_U2.append(voltage_U2)

                voltage_PV = 3 * voltage_U1
                voltages_PV.append(voltage_PV)

                current_1 = voltage_U1/(10**6)
                current_2 = voltage_U2/4.7
                current_PV = current_2 + current_1
                currents_PV.append(current_PV)

                power_PV = voltage_PV*current_PV
                powers_PV.append(power_PV)

                resistance_PV = voltage_PV/current_PV
                resistances_PV.append(resistance_PV)


            mean_powers.append(np.mean(powers_PV))
            mean_resistances.append(np.mean(resistances_PV))

            error_powers.append(np.std(powers_PV)/np.sqrt(repeats))
            error_resistances.append(np.std(resistances_PV)/np.sqrt(repeats))



        self.device.set_output_value(value=0)
        return mean_powers, mean_resistances, error_powers, error_resistances
    

