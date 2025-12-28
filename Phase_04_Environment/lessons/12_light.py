# -----------------------------------------------------------------------------
# Lesson 12: Night Vision (Light Sensors)
# -----------------------------------------------------------------------------
# Module: KY-018 Photoresistor Module
# Goal: Detect the brightness of the room and build an "Auto-Night-Light."
#
# WHY THIS MATTERS:
# This is how streetlights know when to turn on at sunset, and how your 
# phone screen knows to dim itself when you're in a dark room. 
# It's all about saving power and human convenience!
#
# HOW IT WORKS:
# The sensor is an "LDR" (Light Dependent Resistor). 
# Photons (light particles) hit the sensor and "kick" electrons loose, 
# making it easier for electricity to flow.
# - Bright Light = Low Resistance (High Voltage)
# - Darkness     = High Resistance (Low Voltage)
#
# WIRING:
# - S (Signal) -> GP26 (Analog Input 0)
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use ADC because light isn't just ON or OFF; it has many levels.
light_sensor = machine.ADC(machine.Pin(26))

# The onboard LED acts as our "Streetlight"
led = machine.Pin("LED", machine.Pin.OUT)

print("System Active. Cover the sensor with your hand to see it react!")

while True:
    # 1. Read the Brightness (0 to 65535)
    brightness = light_sensor.read_u16()
    
    # 2. Display the value
    # Tip: Use this printed number to find the perfect "Darkness" threshold!
    print(f"Current Light Level: {brightness}")
    
    # 3. Night-Light Logic
    # Threshold: If brightness drops below 15,000, we consider it "Dark."
    if brightness < 15000:
        print(">>> STATUS: DARK (Lights ON)")
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.5) # Check twice per second
