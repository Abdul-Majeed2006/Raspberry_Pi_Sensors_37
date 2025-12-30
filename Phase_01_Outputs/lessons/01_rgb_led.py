# -----------------------------------------------------------------------------
# Lesson 01: The Hello World of Hardware (RGB LED)
# -----------------------------------------------------------------------------
# Module: KY-016 RGB LED Module
# Goal: Control color mixing using PWM (Pulse Width Modulation).
#
# ANATOMY:
# - Common Cathode (-): Shared Ground. Logic: High = ON.
# - Common Anode (+): Shared Power. Logic: Low = ON.
#
# WIRING:
# - R (Red)   -> GP18
# - G (Green) -> GP17
# - B (Blue)  -> GP16
# - - (GND)   -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_R = 18
    PIN_G = 17
    PIN_B = 16
    COMMON_ANODE = True # Set to False if using Common Cathode

def set_color(r_pwm, g_pwm, b_pwm, r_val, g_val, b_val):
    """
    Sets specific PWM duty cycles for RGB channels.
    Handles Common Anode logic inversion automatically.
    """
    if HardwareConfig.COMMON_ANODE:
        # Invert: 0 becomes 65535 (ON), 65535 becomes 0 (OFF)
        r_pwm.duty_u16(65535 - r_val)
        g_pwm.duty_u16(65535 - g_val)
        b_pwm.duty_u16(65535 - b_val)
    else:
        # Standard: Higher = Brighter
        r_pwm.duty_u16(r_val)
        g_pwm.duty_u16(g_val)
        b_pwm.duty_u16(b_val)

def main():
    # 1. Setup Pins (1kHz Frequency)
    red = machine.PWM(machine.Pin(HardwareConfig.PIN_R))
    green = machine.PWM(machine.Pin(HardwareConfig.PIN_G))
    blue = machine.PWM(machine.Pin(HardwareConfig.PIN_B))
    
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)
    
    print("--- SYSTEM READY: RGB CONTROLLER ---")
    
    colors = [
        ("RED",    65535, 0, 0),
        ("GREEN",  0, 65535, 0),
        ("BLUE",   0, 0, 65535),
        ("YELLOW", 65535, 65535, 0),
        ("CYAN",   0, 65535, 65535),
        ("MAGENTA",65535, 0, 65535),
        ("WHITE",  65535, 65535, 65535),
        ("OFF",    0, 0, 0)
    ]
    
    try:
        while True:
            for name, r, g, b in colors:
                print(f"Color: {name}")
                set_color(red, green, blue, r, g, b)
                time.sleep(1)
                
    except KeyboardInterrupt:
        # Turn off on exit
        set_color(red, green, blue, 0, 0, 0)
        print("\nProgram Stopped.")

if __name__ == "__main__":
    main()
