# -----------------------------------------------------------------------------
# Lesson 13: Fire Detection (Flame Sensor)
# -----------------------------------------------------------------------------
# Goal: Detect visible flame (like a lighter).
#       The "Flame Sensor" is actually just a special IR (Infrared) diode.
#       Fire emits a LOT of Infrared light, which this sensor sees.
#
# WIRING:
# - A0 (Analog) -> GP26 (Optional - to see "How close" the fire is)
# - D0 (Digital)-> GP16 (Alarm trigger)
# - G (GND)     -> GND
# - + (Power)   -> 3.3V
#
# Skills Learnt:
# - Dual Mode Sensors (Analog + Digital)
# - Sound Synthesis (Alarms)
# - Safety Systems
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# Use Digital Pin for specific measuring, Analog for range.
flame_digital = machine.Pin(16, machine.Pin.IN)
flame_analog  = machine.ADC(machine.Pin(26))

buzzer = machine.PWM(machine.Pin(15)) # Reuse our buzzer

print("Monitoring for Fire...")

def alarm():
    # Wee-Woo sound
    buzzer.freq(500)
    buzzer.duty_u16(32768)
    time.sleep(0.2)
    buzzer.freq(800)
    time.sleep(0.2)

while True:
    # 1. Digital Check (Is there fire?)
    # Most sensors go LOW (0) when fire is detected.
    if flame_digital.value() == 0:
        print("!! FIRE DETECTED !!")
        alarm()
    else:
        buzzer.duty_u16(0) # Silence
        
    # 2. Analog Check (How close?)
    # Lower value = Closer/Hotter
    raw_val = flame_analog.read_u16()
    # print(f"IR Level: {raw_val}") # Uncomment to calibraten
        
    time.sleep(0.1)
