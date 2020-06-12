Tuple ESP8266 Weather Station Example
=====================================

A example project to send weather data from a ESP8266 to a [Matrix](matrix.org)
room using MQTT and [Tuple](https://github.com/derEisele/tuple).

It's using a ESP8266 flashed with [MicroPython]()

## Message Flow
```text
+---------+
| ESP8266 |
+---------+
     |
     |
     v
+-------------+
| MQTT Broker |
+-------------+
     ^     
     |
     |
     v
+-------+
| Tuple |
+-------+
    ^     
    |
    |
    v
+-------------------+
| Matrix Homeserver |
+-------------------+
    ^     
    |
    |
    v
+---------------+
| Matrix Client |
+---------------+

## Settings
```

## Configuration

* Modify the `boot.py` to match your Wifi credentials
* Modify the `main.py` to match your Matrix Room and MQTT Broker

## Setup

* Setup Tuple using it's [README](https://github.com/derEisele/tuple/blob/master/README.md)
* Flash the ESP8266 with Micropython [Tutorial](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)
* Attach the BME280 via I2C (SCL=5, SDA=6)

## Shopping List for a Weather Station

- 1x Wemos D1 mini clone
- 1x Wemos D1 Mini battery shield (USB works to as power source)
- 1x 3,7V Lithium rechargeable Battery (with matching connector
- 1x BME280 module as a pressure, humidity and temperature sensor
- Some pin headers and soldering material
- Some sort of case
- Wemos D1 Mini Prototype Perf Board
