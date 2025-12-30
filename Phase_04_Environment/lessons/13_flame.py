# -----------------------------------------------------------------------------
# Lesson 13: Fire Detection (Flame Sensor)
# -----------------------------------------------------------------------------
# Module: KY-026 Flame Sensor Module
# Goal: Detect IR Light signature of fire.
#
# ANATOMY:
# The black receiver bulb filters out visible light and only lets Infrared (IR)
# pass through. Fire emits a lot of weak IR light.
#
# WIRING:
# - D0 (Digital) -> GP16 (Trigger)
# - A0 (Analog)  -> GP26 (Meter)
# - G (GND)      -> GND
# - + (Power)    -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_DIGITAL = 16
    PIN_ANALOG  = 26
    PIN_BUZZER  = 17

def play_siren(buzzer):
    """Plays a high-pitched Wee-Woo sound."""
    buzzer.freq(1000)
    buzzer.duty_u16(32768) # 50% volume
    time.sleep(0.1)
    buzzer.freq(1500)
    time.sleep(0.1)

def main():
    # 1. Setup Input: Digital Trigger (Active Low)
    # 0 = Fire Detected
    fire_trigger = machine.Pin(HardwareConfig.PIN_DIGITAL, machine.Pin.IN)
    
    # 2. Setup Input: Analog Meter (Measure Distance/Intensity)
    # Lower number = Stronger Signal
    fire_meter = machine.ADC(HardwareConfig.PIN_ANALOG)
    
    # 3. Setup Output: Buzzer
    buzzer = machine.PWM(machine.Pin(HardwareConfig.PIN_BUZZER))
    buzzer.duty_u16(0) # Start Silent
    
    print("--- SYSTEM READY: FIRE ALARM ---")
    
    while True:
        # A. Check Digital Trigger
        if fire_trigger.value() == 0:
            # FIRE DETECTED!
            strength = fire_meter.read_u16()
            print(f"!!! ALERT: FIRE DETECTED !!! (Intensity: {strength})")
            
            # B. Sound the Alarm
            play_siren(buzzer)
        else:
            # Silence
            buzzer.duty_u16(0)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
