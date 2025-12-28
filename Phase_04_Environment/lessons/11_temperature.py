# -----------------------------------------------------------------------------
# Lesson 11: Temperature Sensing (Analog Thermistor)
# -----------------------------------------------------------------------------
# Module: KY-013 Analog Temperature Sensor Module
# Goal: Measure how hot or cold it is using resistance.
#
# WHY THIS MATTERS:
# Every digital thermostat, air conditioner, and car engine uses a 
# "Thermistor." It is one of the most common sensors in the world because 
# it's cheap and reliable.
#
# HOW IT WORKS:
# The sensor is an "NTC" (Negative Temperature Coefficient) resistor. 
# - Cold = High Resistance (Electricity moves SLOW)
# - Hot  = Low Resistance (Electricity moves FAST)
# By measuring this change, we can calculate the exact temperature.
#
# WIRING:
# - S (Signal) -> GP26 (Analog Input 0)
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import time
import math # We need this for the "log" function (Complex Math)

# --- Setup Pins ---
# Just like the joystick, we use ADC to measure "intensity."
sensor = machine.ADC(machine.Pin(26))

print("System Active. Hold the sensor between your fingers to watch it warm up!")

while True:
    # 1. Read the Raw Number (0 to 65535)
    # 0 = 0V, 65535 = 3.3V
    raw_value = sensor.read_u16()
    
    # 2. Math Magic (The Conversion)
    # To get Celsius, we have to do "Steinhart-Hart" math. 
    # Don't worry if this looks scary! Most of this is standard math for 
    # NTC sensors.
    try:
        # Convert raw number back to voltage
        voltage = (raw_value / 65535) * 3.3
        
        # Calculate resistance of the sensor (The 'R' value)
        # We assume the module has a 10,000 Ohm (10k) resistor on board.
        if voltage < 3.3 and voltage > 0:
            resistance = (10000 * voltage) / (3.3 - voltage)
            
            # Use the Beta equation (A standard shortcut for temperature)
            BETA = 3950 
            temp_kelvin = 1 / ( (1/298.15) + (1/BETA) * math.log(resistance/10000) )
            
            # Convert Kelvin -> Celsius -> Fahrenheit
            temp_c = temp_kelvin - 273.15
            temp_f = (temp_c * 9/5) + 32
            
            # Display results (':.1f' means "show 1 decimal place")
            print(f"Temperature: {temp_c:.1f}°C  ({temp_f:.1f}°F)")
        
    except Exception as e:
        print("Sensor Error: Check your wiring!")
        
    time.sleep(1.0) # Check once every second
