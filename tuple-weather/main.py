from weather import WeatherStation
from tuple import Tuple
import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

w = WeatherStation(600)  # The altitude of the weather station

data = w.read_data()

text = "Temperature: " + str(data.get('temperature')) + "°C\n" \
    + "Humidity: " + str(data.get('humidity')) + "%\n" \
    + "Pressure: " + str(data.get('pressure')) + "hPa"
print(text)

t = Tuple("192.168.178.100", "!ggpDjdETiNCJTpSGto:eiselecloud.de")  # The MQTT Broker's IP and a Matrix room ID

t.send(data, text)

print("send data")
t.done()

rtc.alarm(rtc.ALARM0, 60000 * 15)  # 15 minutes

print("goodbye")

machine.deepsleep()
