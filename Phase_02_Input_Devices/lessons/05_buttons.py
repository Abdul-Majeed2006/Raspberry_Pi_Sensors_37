# -----------------------------------------------------------------------------
# Lesson 05: The Power of Inputs (Buttons & Touch)
# -----------------------------------------------------------------------------
# Modules: KY-004 Button / KY-036 Metal Touch
# Goal: Master both "On/Off" (Digital) and "How Much" (Analog) detection.
#
# WHY THIS MATTERS:
# - Digital (DO): Tells you IF someone is touching the sensor (Yes/No).
# - Analog (AO): Tells you HOW INTENSE the touch is (Static discharge strength).
#
# WIRING (Clustered Standard):
# [KY-004 Button]
# - S -> GP16 (Digital In)
# - - -> GND (Wait for PULL_UP logic)
#
# [KY-036 Metal Touch]
# - G -> GND
# - + -> 3.3V
# - DO -> GP17 (Digital In)
# - AO -> GP26 (Analog In/ADC0)
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Digital Inputs ---
# We use PULL_UP because most physical buttons 
# connect to Ground (0) when pressed.
# 1 = IDLE | 0 = PRESSED
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
touch_digital = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

# --- Setup Analog Input ---
touch_analog = machine.ADC(machine.Pin(26))

# Onboard LED
led = machine.Pin("LED", machine.Pin.OUT)

print("--- INPUT DIAGNOSTIC ACTIVE ---")
print("Press a button and watch the numbers change.")

while True:
    # 1. Read Raw States
    btn_raw = button.value()
    touch_raw = touch_digital.value()
    intensity = touch_analog.read_u16()
    
    # 2. Print Diagnostic (See what the Pico 'feels')
    print(f"Pin Values: Button={btn_raw} | Touch={touch_raw} | Analog={intensity}")
    
    # --- Logic (PULL_UP = 0 when pressed) ---
    if btn_raw == 0:
        print(">> BUTTON DETECTED")
        led.value(1)
    elif touch_raw == 0:
        print(">> TOUCH DETECTED")
        led.value(1)
    else:
        led.value(0)
    
    time.sleep(0.1) 
