# -----------------------------------------------------------------------------
# Lesson 01: Light It Up (RGB LED)
# -----------------------------------------------------------------------------
# Module: KY-016 RGB LED Module
# Goal: Control an RGB LED to cycle through colors using PWM (Pulse Width Modulation).
#
# WIRING:
# - RED Pin   -> GP18
# - GREEN Pin -> GP17
# - BLUE Pin  -> GP16
# - GND (-)   -> Any GND Pin
#
# Skills Learnt:
# - Pulse Width Modulation (PWM)
# - Duty Cycles (0-65535)
# - Helper Functions
# -----------------------------------------------------------------------------

import machine
import time

# --- CONFIGURATION ---
# Set this to True if your colors are inverted or only one color shows!
# Common Cathode (Most kits): False
# Common Anode (Inverted logic): True
COMMON_ANODE = False 

# --- Setup Pins ---
# We use PWM (Pulse Width Modulation) to control brightness.
# Frequency = 1000 Hz (flickers too fast for human eye to see).
red_led = machine.PWM(machine.Pin(18))
green_led = machine.PWM(machine.Pin(17))
blue_led = machine.PWM(machine.Pin(16))

red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

# --- Helper Function ---
def set_color(r, g, b):
    """
    Sets the color of the RGB LED.
    Arguments r, g, b should be between 0 (off) and 65535 (full brightness).
    """
    if COMMON_ANODE:
        # Invert the signal: 0 is Full Bright, 65535 is OFF
        red_led.duty_u16(65535 - r)
        green_led.duty_u16(65535 - g)
        blue_led.duty_u16(65535 - b)
    else:
        # Standard: 65535 is Full Bright, 0 is OFF
        red_led.duty_u16(r)
        green_led.duty_u16(g)
        blue_led.duty_u16(b)

# --- Main Loop ---
print("Starting Color Cycle... (Press Ctrl+C to stop)")

try:
    while True:
        # 1. Red
        print("Color: RED")
        set_color(65535, 0, 0)
        time.sleep(1)

        # 2. Green
        print("Color: GREEN")
        set_color(0, 65535, 0)
        time.sleep(1)

        # 3. Blue
        print("Color: BLUE")
        set_color(0, 0, 65535)
        time.sleep(1)

        # 4. Yellow (mix Red + Green)
        print("Color: YELLOW")
        set_color(65535, 65535, 0)
        time.sleep(1)

        # 5. Cyan (mix Green + Blue)
        print("Color: CYAN")
        set_color(0, 65535, 65535)
        time.sleep(1)

        # 6. Magenta (mix Red + Blue)
        print("Color: MAGENTA")
        set_color(65535, 0, 65535)
        time.sleep(1)

        # 7. White (All On)
        print("Color: WHITE")
        set_color(65535, 65535, 65535)
        time.sleep(1)

        # 8. Off
        print("Color: OFF")
        set_color(0, 0, 0)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Turn off LED when stopping
    set_color(0, 0, 0)
    print("\nProgram stopped.")
