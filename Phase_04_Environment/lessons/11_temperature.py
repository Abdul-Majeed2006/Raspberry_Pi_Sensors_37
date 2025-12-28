# -----------------------------------------------------------------------------
# Lesson 11: Temperature (Analog Thermistor)
# -----------------------------------------------------------------------------
# Module: KY-013 Analog Temperature Sensor Module
# Goal: Measure how hot it is!
#       We will use the "Analog Temperature Sensor" (KY-013).
#       It works like a resistor that changes with heat.
#
# WIRING:
# - S (Signal) -> GP26 (ADC0) - MUST be an ADC pin!
# - (+) middle -> 3.3V
# - (-)        -> GND
#
# Skills Learnt:
# - Analog to Digital Conversion (ADC)
# - Voltage Division
# - Complex Math (Logarithms)
# -----------------------------------------------------------------------------

import machine
import time
import math

# --- Setup Pins ---
# We use ADC (Analog to Digital Converter) just like the Joystick.
sensor = machine.ADC(machine.Pin(26))

print("Reading Temperature...")

while True:
    # 1. Read Raw Value (0 to 65535)
    raw_value = sensor.read_u16()
    
    # 2. Convert to Voltage (0 to 3.3V)
    voltage = (raw_value / 65535) * 3.3
    
    # 3. Calculate Resistance (Ohm's Law magic)
    # The module usually has a 10k resistor divider.
    # If the reading is failing, try swapping logic (some modules are weird).
    if voltage > 0:
        resistance = (10000 * voltage) / (3.3 - voltage)
    else:
        resistance = 0
        
    # 4. Convert to Celsius (Steinhart-Hart Equation)
    # This is complex math to convert resistance to temperature.
    # We assume a standard NTC 10k Thermistor.
    try:
        # Values for a typical thermistor
        BETA = 3950 
        temp_kelvin = 1 / ( (1/298.15) + (1/BETA) * math.log(resistance/10000) )
        temp_celsius = temp_kelvin - 273.15
        temp_f = (temp_celsius * 9/5) + 32
        
        print(f"Raw: {raw_value} | Temp: {temp_celsius:.1f} C  /  {temp_f:.1f} F")
        
    except:
        print(f"Raw: {raw_value} (Math Error - Is sensor connected?)")

    time.sleep(1)
