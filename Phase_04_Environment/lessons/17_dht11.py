# -----------------------------------------------------------------------------
# Lesson 17: Climate Monitoring (DHT11)
# -----------------------------------------------------------------------------
# Module: KY-015 Temperature & Humidity Sensor (DHT11)
# Goal: Measure both Temperature AND Humidity using a digital protocol.
#
# WIRING:
# - S (Signal) -> GP16
# - middle (+) -> 3.3V
# - (-)        -> GND
#
# Skills Learnt:
# - Digital Protocols (Single-Bus)
# - Using built-in libraries (dht)
# - Humidity vs Temperature data
# -----------------------------------------------------------------------------

import machine
import dht
import time

# --- Setup Pins ---
# The DHT11 uses a specific digital protocol, so we use the 'dht' library.
sensor = dht.DHT11(machine.Pin(16))

print("Starting Climate Monitor...")

while True:
    try:
        # 1. Trigger the measurement
        sensor.measure()
        
        # 2. Read the values
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # 3. Print Results
        print(f"Temp: {temp}°C | Humidity: {hum}%")
        
    except OSError as e:
        print("Failed to read sensor. Check wiring!")
        
    # DHT11 needs at least 1-2 seconds between readings!
    time.sleep(2)
