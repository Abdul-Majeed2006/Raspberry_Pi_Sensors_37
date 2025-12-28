# -----------------------------------------------------------------------------
# Lesson 13: Fire Detection (Flame Sensor)
# -----------------------------------------------------------------------------
# Module: KY-026 Flame Sensor Module
# Goal: Detect the specific light spectrum of fire and trigger a "Fire Alarm."
#
# WHY THIS MATTERS:
# This is a critical safety component. It's used in industrial furnaces and 
# space heaters to ensure the flame is actually burning. If the flame goes 
# out, the gas must be shut off instantly to prevent an explosion!
#
# HOW IT WORKS:
# The black bulb on the sensor is an IR (Infrared) Receiver. 
# Fire emits a very specific frequency of Infrared light. The black coating 
# on the bulb "filters out" normal visible light so the sensor only 
# reacts to the "heat-light" of fire.
#
# WIRING:
# - D0 (Digital) -> GP21 (Safe Pin)
# - A0 (Analog)  -> GP26 (Safe Pin)
# - G (GND)      -> GND
# - + (Power)    -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use both Digital (to act as a trigger) and Analog (to measure distance).
flame_trigger = machine.Pin(21, machine.Pin.IN)
flame_meter   = machine.ADC(machine.Pin(26))

# We use the buzzer (GP15) to make the alarm sound.
buzzer = machine.PWM(machine.Pin(15))

print("System Active. Monitoring for IR Flame signature...")

def play_siren():
    """Plays a high-pitched Wee-Woo sound."""
    buzzer.freq(1000)
    buzzer.duty_u16(32768) # 50% volume
    time.sleep(0.1)
    buzzer.freq(1500)
    time.sleep(0.1)

while True:
    # 1. Digital Detection
    # 0 = FIRE DETECTED (Active Low)
    if flame_trigger.value() == 0:
        # Calculate how close it is (Smaller number = closer/stronger)
        strength = flame_meter.read_u16()
        print(f"!!! ALERT: FIRE DETECTED !!! (Intensity: {strength})")
        play_siren()
    else:
        # No fire, be quiet.
        buzzer.duty_u16(0) 
        
    time.sleep(0.1) # Check 10 times per second
