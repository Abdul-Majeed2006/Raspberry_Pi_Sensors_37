# -----------------------------------------------------------------------------
# Lesson 12: Digital vs Analog (The Duel)
# -----------------------------------------------------------------------------
# Module: KY-018 Photoresistor Module
# Goal: Compare Software Logic (ADC) vs Hardware Logic (Comparator).
#
# THE MODULE ADVANTAGE:
# Anyone can buy a raw photoresistor. But this module has a "Comparator Chip"
# (LM393) and a Blue Dial (Potentiometer).
#
# - ANALOG (A0): Gives us the exact brightness (0-65535).
# - DIGITAL (D0): Gives us a simple 1 or 0 based on the Blue Dial.
#
# HARDWARE TUNING:
# You can use a screwdriver to change the sensitivity of D0 without writing
# a single line of code!
#
# WIRING:
# - A0 (Analog)  -> GP26
# - D0 (Digital) -> GP16
# - (+)          -> 3.3V
# - (-)          -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- PINS ---
analog_pin = machine.ADC(26)
digital_pin = machine.Pin(16, machine.Pin.IN)
led = machine.Pin("LED", machine.Pin.OUT)

print("--- HARDWARE VS SOFTWARE DUEL ---")
print("Adjust the Blue Dial to set the trigger point for D0!")

while True:
    # 1. Read Both Worlds
    soft_val = analog_pin.read_u16()
    hard_val = digital_pin.value()
    
    # 2. Logic Comparison
    # Software: We decide the threshold in code (e.g. < 20000)
    # Hardware: The Blue Dial decides the threshold physically
    
    status = "DARK" if hard_val == 1 else "LIGHT"
    
    # KY-018 Logic: D0 goes HIGH (1) when it crosses the threshold (Darkness)
    # Note: Some modules are inverted. Check yours!
    
    print(f"Analog: {soft_val} | Digital: {hard_val} ({status})")
    
    # 3. The LED follows the Hardware (D0)
    led.value(hard_val)
    
    time.sleep(0.2)
