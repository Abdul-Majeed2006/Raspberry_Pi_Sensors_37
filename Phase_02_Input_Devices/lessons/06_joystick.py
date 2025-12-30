# -----------------------------------------------------------------------------
# Lesson 06: Analog Control (The Joystick)
# -----------------------------------------------------------------------------
# Module: KY-023 Joystick Module
# Goal: Accurate 2-Axis control with Deadzones.
#
# ANATOMY:
# A Joystick is just two Potentiometers (X and Y) and a Button.
# Center ~ 32768 (Half of 65535).
#
# WIRING:
# - GND -> GND
# - +5V -> 3.3V (The Pico uses 3.3V logic!)
# - VRx -> GP26 (ADC0)
# - VRy -> GP27 (ADC1)
# - SW  -> GP16 (Use PULL_UP)
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_X = 26
    PIN_Y = 27
    PIN_SW = 16
    
    # Calibration Constants
    CENTER = 32768
    DEADZONE = 5000  # Ignore small jitters around the center
    THRESHOLD_LOW = 10000
    THRESHOLD_HIGH = 50000

def get_direction(val):
    """Helper to convert analog value to direction."""
    if val < HardwareConfig.THRESHOLD_LOW:
        return -1 # Left/Up
    elif val > HardwareConfig.THRESHOLD_HIGH:
        return 1  # Right/Down
    else:
        return 0  # Center

def main():
    # 1. Setup Inputs
    joy_x = machine.ADC(HardwareConfig.PIN_X)
    joy_y = machine.ADC(HardwareConfig.PIN_Y)
    joy_btn = machine.Pin(HardwareConfig.PIN_SW, machine.Pin.IN, machine.Pin.PULL_UP)
    
    print("--- JOYSTICK CALIBRATION READY ---")
    
    while True:
        # 2. Read Sensors
        raw_x = joy_x.read_u16()
        raw_y = joy_y.read_u16()
        is_pressed = not joy_btn.value() # Active Low
        
        # 3. Process Logic (Deadzones are handled by the threshold check)
        dir_x_val = get_direction(raw_x)
        dir_y_val = get_direction(raw_y)
        
        # Decode X
        if dir_x_val == -1: dir_x = "LEFT "
        elif dir_x_val == 1: dir_x = "RIGHT"
        else: dir_x = "-----"
        
        # Decode Y
        if dir_y_val == -1: dir_y = "UP   "
        elif dir_y_val == 1: dir_y = "DOWN "
        else: dir_y = "-----"
        
        # 4. Display
        btn_status = "[X]" if is_pressed else "[ ]"
        print(f"{btn_status} X: {raw_x:05d} ({dir_x}) | Y: {raw_y:05d} ({dir_y})")
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
