#!/usr/bin/env python3

from Adafruit_BMP.BMP085 import BMP085

class Bmp180(BMP085):
	address = 0x77

	@property
	def temperature(self):
		return self.read_temperature()

	@property
	def pressure(self):
		return self.read_pressure() / 100

	@property
	def data(self):
		return {
			"temperature": self.temperature,
			"pressure": self.pressure
		}

	@property
	def units(self):
		return {
			"temperature": "celsius",
			"pressure": "hectopascal"
		}

	def __str__(self):
		ret  = "Temperature: " + str(round(self.temperature, 2)) + u" \u00B0C\n"
		ret += "Pressure: " + str(round(self.pressure, 2)) + " hPa"
		return ret

if __name__ == "__main__":
	P_TEMP = Bmp180()
	print(str(P_TEMP))
