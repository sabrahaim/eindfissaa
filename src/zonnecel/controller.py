try:
    from nsp2visasim import sim_pyvisa as pyvisa
except ModuleNotFoundError:
    import pyvisa


class ArduinoZonnecel:
    def __init__(self, port):
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")

    def set_output_voltage(self, value):
        self.device.query(f"OUT:CH0 {int(value*(1023/3.3))}")

    def get_output_value(self):
        return self.device.query(f"OUT:CH0?")
    
    def get_input_value(self, channel):
        return int(self.device.query(f"MEAS:CH{channel}?"))

    def get_input_voltage(self, channel):
        return (int(self.device.query(f"MEAS:CH{channel}?")) / 1023) * 3.3

    def close(self):
        self.device.close()


def list_devices():
    rm = pyvisa.ResourceManager("@py")
    return rm.list_resources()


# lijst = list_devices()
# print(lijst)
