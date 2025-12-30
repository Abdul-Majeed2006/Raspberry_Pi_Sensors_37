# -----------------------------------------------------------------------------
# Lesson 05: The Power of Inputs (Buttons & Touch)
# -----------------------------------------------------------------------------
# Module: KY-004 Button / KY-036 Metal Touch
# Goal: Master both "On/Off" (Digital) and "How Much" (Analog) detection.
#
# HARDWARE ANATOMY:
# 1. KY-004 (Button): A simple mechanical bridge. Press = Bridge Closed.
# 2. KY-036 (Touch): Darlington Transistor amplifies skin conductivity.
#
# WIRING STRATEGY:
# [KY-004 Button]     [KY-036 Metal Touch]
# S -> GP16 (IN)      DO -> GP17 (IN) | AO -> GP26 (ADC)
# - -> GND            G  -> GND       | +  -> 3.3V
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    """Central configuration for Pin mapping."""
    PIN_BUTTON_S = 16
    PIN_TOUCH_DO = 17
    PIN_TOUCH_AO = 26
    PIN_LED_INT  = "LED"

def main():
    # 1. Setup Digital Inputs (Active Low logic: 0 = Pressed)
    btn_digital = machine.Pin(HardwareConfig.PIN_BUTTON_S, machine.Pin.IN, machine.Pin.PULL_UP)
    touch_digital = machine.Pin(HardwareConfig.PIN_TOUCH_DO, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # 2. Setup Analog Input (16-bit resolution: 0-65535)
    touch_analog = machine.ADC(HardwareConfig.PIN_TOUCH_AO)
    
    # 3. Setup Output (Feedback)
    led = machine.Pin(HardwareConfig.PIN_LED_INT, machine.Pin.OUT)
    
    print("--- SYSTEM READY: Input Diagnostic ---")
    print("Touch the sensor or press the button...")
    
    while True:
        # A. Read Raw Values
        # Note: 'value()' returns 1 (High/Idle) or 0 (Low/Active)
        btn_state = btn_digital.value()
        touch_state = touch_digital.value()
        analog_val = touch_analog.read_u16()
        
        # B. Visualize State
        # Invert logic for display: (1-x) turns 0->1 and 1->0
        is_btn_pressed = not btn_state
        is_touching = not touch_state
        
        print(f"Button: {'down' if is_btn_pressed else 'up  '} | "
              f"Touch: {'YES' if is_touching else 'NO '} | "
              f"Intensity: {analog_val:05d}")
        
        # C. Feedback Logic (OR Gate)
        if is_btn_pressed or is_touching:
            led.value(1)
        else:
            led.value(0)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
