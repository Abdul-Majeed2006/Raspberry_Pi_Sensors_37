# -----------------------------------------------------------------------------
# Lesson 04: Laser Precision (Morse Code)
# -----------------------------------------------------------------------------
# Module: KY-008 Laser Transmitter
# Goal: Optic Communication using Morse Code.
#
# SAFETY:
# NEVER LOOK INTO THE BEAM. Class 3R Laser product.
#
# WIRING:
# - S -> GP16
# - - -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_LASER = 16
    DOT_TIME = 0.2

class MorseCode:
    TABLE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'S': '...',
        'O': '---',   ' ': '/'
    }

def blink(pin, duration):
    pin.value(1)
    time.sleep(duration)
    pin.value(0)
    time.sleep(HardwareConfig.DOT_TIME) # Inter-symbol gap

def transmit(pin, text):
    text = text.upper()
    print(f"TX: {text}")
    
    for char in text:
        code = MorseCode.TABLE.get(char, '')
        if not code: continue
        
        print(f"'{char}' -> {code}")
        for symbol in code:
            if symbol == '.':
                blink(pin, HardwareConfig.DOT_TIME)
            elif symbol == '-':
                blink(pin, HardwareConfig.DOT_TIME * 3)
            elif symbol == '/':
                time.sleep(HardwareConfig.DOT_TIME * 4) # Word gap
        
        time.sleep(HardwareConfig.DOT_TIME * 3) # Letter gap

def main():
    laser = machine.Pin(HardwareConfig.PIN_LASER, machine.Pin.OUT)
    
    print("--- SYSTEM READY: LASER TX ---")
    
    while True:
        transmit(laser, "SOS")
        time.sleep(3)

if __name__ == "__main__":
    main()
