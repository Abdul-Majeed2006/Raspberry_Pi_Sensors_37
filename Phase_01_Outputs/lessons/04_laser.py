# -----------------------------------------------------------------------------
# Lesson 04: Laser Precision (Morse Code Transmitter)
# -----------------------------------------------------------------------------
# Module: KY-008 Laser Transmitter Module
# Goal: Use invisible light (or focused light) to send secret messages.
#
# WHY THIS MATTERS:
# Fiber optic cables carry the entire Internet using lasers just like this 
# one. By "blinking" the light in a specific pattern, we can send complex 
# data across the world in milliseconds.
#
# SAFETY WARNING:
# NEVER look directly into the laser beam. It can cause permanent eye damage.
# Treat it like a concentrated beam of sun!
#
# WIRING:
# - S (Signal) -> GP15
# - - (GND)    -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# The laser is a DIGITAL output. 1 is ON, 0 is OFF.
laser = machine.Pin(15, machine.Pin.OUT)

# --- Data Structure: The Dictionary ---
# We store the "Translation" for every letter here.
# A Dot (.) is a short blink. A Dash (-) is a long blink.
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  ' ': '/'
}

# --- The "Actions" (Functions) ---
def dot():
    """Blinks a short pulse (0.2s)"""
    laser.value(1)
    time.sleep(0.2) 
    laser.value(0)
    time.sleep(0.2) # Small gap after the blink

def dash():
    """Blinks a long pulse (0.6s)"""
    laser.value(1)
    time.sleep(0.6) 
    laser.value(0)
    time.sleep(0.2) 

def transmit(text):
    """
    Translates a whole sentence into laser blinks.
    """
    # 1. Clean the text (Make it all BIG letters)
    text = text.upper()
    print(f"TRANSMITTING: {text}")
    
    # 2. Iterate (Loop) through every letter in the word
    for character in text:
        if character in MORSE_CODE:
            code = MORSE_CODE[character]
            print(f"[{character}] : {code}")
            
            # 3. Blink the DOTS and DASHES for that specific letter
            for symbol in code:
                if symbol == '.':
                    dot()
                elif symbol == '-':
                    dash()
                elif symbol == '/':
                    # A slash means a space between words
                    time.sleep(0.5) 
            
            # Tiny gap before the next letter starts
            time.sleep(0.5) 
        else:
            print(f"Error: {character} is not in Morse Code.")

# --- The Mission ---
while True:
    # Send the universal signal for Distress: SOS
    transmit("SOS")
    
    # Wait 3 seconds before repeating
    time.sleep(3)
    
    # EXERCISE: Change "SOS" to your name and see if you can decode it!
