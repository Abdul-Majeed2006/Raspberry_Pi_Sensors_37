# -----------------------------------------------------------------------------
# Lesson 17: Climate Monitoring (DHT11)
# -----------------------------------------------------------------------------
# Module: KY-015 Temperature & Humidity Sensor (DHT11)
# Goal: Measure both Temperature AND Humidity using a specialized digital brain.
#
# WHY THIS MATTERS:
# Knowing just the temperature isn't enough for plants or computers. 
# "Relative Humidity" tells us how much water is in the air. High humidity 
# makes hard drives rust and people feel hotter! 
#
# HOW IT WORKS (The Digital Brain):
# Unlike the Analog thermistor (Lesson 11), the DHT11 has its own tiny 
# computer inside. It measures the air and then "talks" to the Pico using a 
# digital language (Single-Bus). Instead of measuring voltage, we just ask 
# it for the latest numbers!
#
# WIRING:
# - S (Signal) -> GP21 (Safe Pin)
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import dht  # Special library for the DHT protocol
import time

# --- Setup Pins ---
# We use the DHT11 class from the library to handle the complex timing.
sensor = dht.DHT11(machine.Pin(21))

print("System Active. Waiting for initial climate data...")

while True:
    try:
        # 1. Trigger the measurement (The Pico asks the sensor to wake up)
        sensor.measure()
        
        # 2. Grab the latest numbers from the sensor's memory
        temp_c = sensor.temperature()
        hum = sensor.humidity()
        temp_f = (temp_c * 9/5) + 32
        
        print(f"Climate: {temp_c}°C ({temp_f:.1f}°F) | Humidity: {hum}%")
        
    except OSError:
        # DHT11 is sensitive to timing. If it fails, just wait and try again.
        print("Reading timed out. Retrying...")
        
    # IMPORTANT: The DHT11 is slow. 
    # If you ask it for data too fast (less than 2 seconds), it will error out!
    time.sleep(2.0)
