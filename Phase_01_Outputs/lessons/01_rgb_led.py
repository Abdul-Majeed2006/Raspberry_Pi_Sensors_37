# -----------------------------------------------------------------------------
# Lesson 01: The Hello World of Hardware (RGB LED)
# -----------------------------------------------------------------------------
# Module: KY-016 RGB LED Module
# Goal: Control a single LED to create any color in the rainbow.
#
# WHY THIS MATTERS:
# Every screen you look at (Phone, TV, Laptop) works exactly like this! 
# Screens are just millions of tiny Red, Green, and Blue dots. By mixing 
# them at different intensities, we can trick the human eye into seeing 
# any color (like Yellow, Purple, or White).
#
# COMMON ANODE VS COMMON CATHODE:
# Electronics are like plumbing. Electricity needs to flow from (+) to (-).
# 1. Common Cathode (-) : All colors share one GROUND pin. You push (+) 
#    from the Pico to turn them ON. (Standard Logic)
# 2. Common Anode (+) : All colors share one 3.3V pin. To turn them ON, 
#    you must PULL the Pico pin to Ground (0V). (Inverse Logic)
#
# WIRING:
# - R (Red)   -> GP18
# - G (Green) -> GP17
# - B (Blue)  -> GP16
# - - (GND)   -> GND
# -----------------------------------------------------------------------------

import machine  # The "machine" module gives us control over the Pico's hardware pins.
import time     # The "time" module allows us to pause the code (sleep).

# --- CONFIGURATION ---
# Set this to True if your LED module is "Common Anode" 
# (Usually if it turns OFF when you set duty to 65535).
COMMON_ANODE = True 

# --- Setup Pins (The PWM Class) ---
# We use PWM to "vibrate" the power. 
# 0 = Always OFF, 65535 = Always ON, 32768 = Half Brightness.
# 
# Frequency = 1000 Hz. This means the LED flashes 1,000 times per second.
# It happens so fast that your eyes see a smooth glow instead of a flicker!

red = machine.PWM(machine.Pin(18))
green = machine.PWM(machine.Pin(17))
blue = machine.PWM(machine.Pin(16))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

# --- The Helper Function (Code Reusability) ---
# We define a function so we don't have to type three lines of code every 
# time we want to change the color. We just "call" set_color(r, g, b).
def set_color(r, g, b):
    """
    Sets the color of the RGB LED.
    - r, g, b: Brightness values between 0 (OFF) and 65535 (ULTRA BRIGHT).
    
    WHY 65535? 
    The Pico uses 16-bit numbers for PWM. 2 to the power of 16 is 65536. 
    So 0 to 65535 is the full range of power.
    """
    if COMMON_ANODE:
        # If your module is "Common Anode", we have to flip the logic.
        # "65535 - r" makes 0 become 65535 (Bright) and 65535 become 0 (Off).
        red_led.duty_u16(65535 - r)
        green_led.duty_u16(65535 - g)
        blue_led.duty_u16(65535 - b)
    else:
        # Standard logic: Higher number = More Power = Brighter LED.
        red_led.duty_u16(r)
        green_led.duty_u16(g)
        blue_led.duty_u16(b)

# --- The Main Loop ---
# This loop runs forever (While True is always true!).
print("Starting Color Cycle... (Press Ctrl+C to stop)")

try:
    while True:
        # 1. Pure Red
        print("Color: RED")
        set_color(65535, 0, 0) # Red Full, Others Off
        time.sleep(1)

        # 2. Pure Green
        print("Color: GREEN")
        set_color(0, 65535, 0)
        time.sleep(1)

        # 3. Pure Blue
        print("Color: BLUE")
        set_color(0, 0, 65535)
        time.sleep(1)

        # 4. Yellow (Mixing Red + Green)
        print("Color: YELLOW")
        set_color(65535, 65535, 0)
        time.sleep(1)

        # 5. Cyan (Mixing Green + Blue)
        print("Color: CYAN")
        set_color(0, 65535, 65535)
        time.sleep(1)

        # 6. Magenta (Mixing Red + Blue)
        print("Color: MAGENTA")
        set_color(65535, 0, 65535)
        time.sleep(1)

        # 7. White (Mixing All Colors)
        print("Color: WHITE")
        set_color(65535, 65535, 65535)
        time.sleep(1)

        # 8. All Off
        print("Color: OFF")
        set_color(0, 0, 0)
        time.sleep(0.5)

except KeyboardInterrupt:
    # This block runs when you press stop. It's polite to turn off the 
    # lights before leaving the room!
    set_color(0, 0, 0)
    print("\nProgram stopped safely.")
