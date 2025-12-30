# -----------------------------------------------------------------------------
# Lesson 19: The Pulse (Heartbeat Sensor)
# -----------------------------------------------------------------------------
# Module: KY-039 Finger Heartbeat Sensor
# Goal: Detect the faint blood flow changes in your fingertip.
#
# ANATOMY:
# This sensor is just an IR LED and a Photo-Transistor. 
# When your heart pumps, blood fills your finger, which blocks slightly more 
# light. The sensor sees this tiny dip in brightness.
#
# WIRING:
# - S (Signal) -> GP26 (ADC)
# - + (Power)  -> 3.3V
# - - (GND)    -> GND
# *Note: This is a very noisy sensor. Don't expect medical grade precision!
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_SENSOR = 26
    PIN_BEAT_LED = "LED"
    
    # Thresholding is hard with this sensor because it depends on your finger size.
    # We use a "Dynamic Threshold" (Detecting rapid changes).
    SENSITIVITY = 500

def main():
    sensor = machine.ADC(HardwareConfig.PIN_SENSOR)
    beat_led = machine.Pin(HardwareConfig.PIN_BEAT_LED, machine.Pin.OUT)
    
    print("--- SYSTEM READY: HEART MONITOR ---")
    print("Place finger GENTLY between the LED and the Receiver.")
    print("Do not press hard! Pressing hard stops blood flow.")
    
    # Calibration Loop
    last_val = sensor.read_u16()
    
    while True:
        current_val = sensor.read_u16()
        
        # Calculate the "Derivative" (Rate of Change)
        change = current_val - last_val
        
        # If the change is sudden and positive, that's a pulse!
        if change > HardwareConfig.SENSITIVITY:
            print(f"♥ BEAT! (Delta: {change})")
            beat_led.value(1)
            time.sleep(0.1) # Debounce the beat
            beat_led.value(0)
            
        last_val = current_val
        time.sleep(0.02) # High speed polling (50Hz)

if __name__ == "__main__":
    main()
