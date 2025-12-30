# -----------------------------------------------------------------------------
# Lesson 11: Temperature Sensing (Analog Thermistor)
# -----------------------------------------------------------------------------
# Module: KY-013 Analog Temperature Sensor Module
# Goal: Measure how hot or cold it is using resistance.
#
# ANATOMY:
# A Thermistor is a resistor that changes with heat.
# - NTC: Negative Temperature Coefficient (Hotter = Less Resistance).
#
# PHYSICAL MATH:
# We use the Steinhart-Hart Equation to convert resistance to Celsius.
#
# WIRING:
# - S (Signal) -> GP26 (Analog Input)
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import time
import math

class HardwareConfig:
    PIN_TEMP = 26
    # Physics Constants
    BETA = 3950          # Beta value for NTC Thermistor
    R_REF = 10000        # 10k Resistor in series
    KELVIN_ZERO = 273.15 # 0C in Kelvin

def get_temperature_c(raw_adc):
    """
    Converts raw ADC value (0-65535) to Celsius.
    Uses Steinhart-Hart equation approximation (Beta Parameter).
    """
    if raw_adc == 0 or raw_adc == 65535:
        return None # Invalid reading
        
    # 1. Calculate Voltage
    voltage = (raw_adc / 65535) * 3.3
    
    # 2. Calculate Resistance of Thermistor
    # Divider Formula: Vout = Vin * (R2 / (R1 + R2))
    # Solving for R_thermistor...
    try:
        resistance = (HardwareConfig.R_REF * voltage) / (3.3 - voltage)
    except ZeroDivisionError:
        return None
    
    # 3. Apply Steinhart-Hart (Beta)
    # 1/T = 1/To + 1/B * ln(R/Ro)
    ref_temp_k = 298.15 # 25C in Kelvin
    
    inv_t = (1 / ref_temp_k) + (1 / HardwareConfig.BETA) * math.log(resistance / HardwareConfig.R_REF)
    temp_k = 1 / inv_t
    
    return temp_k - HardwareConfig.KELVIN_ZERO

def main():
    sensor = machine.ADC(HardwareConfig.PIN_TEMP)
    
    print("--- SYSTEM READY: THERMOMETER AGENT ---")
    print("Hold the sensor to warm it up...")
    
    while True:
        raw_val = sensor.read_u16()
        temp_c = get_temperature_c(raw_val)
        
        if temp_c is not None:
            temp_f = (temp_c * 9/5) + 32
            print(f"Reading: {raw_val:05d} | Temp: {temp_c:.1f}C ({temp_f:.1f}F)")
        else:
            print("Sensor Error: Check Wiring")
            
        time.sleep(1.0)

if __name__ == "__main__":
    main()
