# -----------------------------------------------------------------------------
# Lesson 12: Night Vision (Light Sensors)
# -----------------------------------------------------------------------------
# Goal: Detect how bright the room is.
#       We will use a "Photoresistor" (LDR - Light Dependent Resistor).
#       It works exactly like the Thermistor: Resistance changes with LIGHT.
#
# WIRING:
# - S (Signal) -> GP26 (ADC0)
# - middle     -> 3.3V
# - (-)        -> GND
#
# Skills Learnt:
# - Analog Inputs (LDR)
# - Calibration logic
# - Threshold switching
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# 0 = Pitch Black
# 65535 = Staring at the Sun (Warning: Do not stare at the sun)
light_sensor = machine.ADC(machine.Pin(26))

led = machine.Pin("LED", machine.Pin.OUT)

print("Monitoring Light Levels...")

while True:
    # 1. Read Light Level
    light_level = light_sensor.read_u16()
    
    print(f"Brightness: {light_level}")
    
    # 2. Automatic Night Light
    # If it gets dark (< 10000), turn on the light!
    if light_level < 10000:
        print(" -> It is dark! Lights ON.")
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.5)
