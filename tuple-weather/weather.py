import machine
from libs import bme280_float as bme280
# from libs import si1145

class WeatherStation:
    def __init__(self):
        self.bme = None
        self.si = None
        self.i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

        self.init_bme280()
        # self.init_si1145()

    def init_bme280(self):
        self.bme = bme280.BME280(i2c=self.i2c)

    # def init_si1145(self):
    #     self.si = si1145.SI1145(i2c=self.i2c)

    def read_data(self):
        data = {}
        if self.bme:
            t, p, h = self.bme.read_compensated_data()
            data["temperature"] = t
            data["humidity"] = h
            data["pressure"] = p
        return data
