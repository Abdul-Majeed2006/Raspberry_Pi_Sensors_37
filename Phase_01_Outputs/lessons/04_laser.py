# -----------------------------------------------------------------------------
# Lesson 04: Laser Precision (Morse Code Transmitter)
# -----------------------------------------------------------------------------
# Goal: Use the Laser Module to send a secret message using Morse Code.
#
# SAFETY WARNING:
# NEVER look directly into the laser beam. It can damage your eyes.
#
# WIRING:
# - S (Signal) -> GP14
# - - (GND)    -> GND
# - (Middle pin is usually not connected or VCC)
#
# Skills Learnt:
# - Signal Timing
# - String Manipulation
# - Python Dictionaries
# -----------------------------------------------------------------------------

import machine
import time

# Setup Laser on Pin 14
laser = machine.Pin(14, machine.Pin.OUT)

# Dictionary for Morse Code
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  ' ': '/'
}

def dot():
    laser.value(1)
    time.sleep(0.2) # Short flash
    laser.value(0)
    time.sleep(0.2) # Gap

def dash():
    laser.value(1)
    time.sleep(0.6) # Long flash (3x dot)
    laser.value(0)
    time.sleep(0.2) # Gap

def transmit(message):
    message = message.upper()
    print(f"Sending: {message}")
    
    for char in message:
        if char in MORSE_CODE:
            code = MORSE_CODE[char]
            print(f"{char}: {code}")
            
            # Blink the code
            for symbol in code:
                if symbol == '.':
                    dot()
                elif symbol == '-':
                    dash()
                elif symbol == '/':
                    time.sleep(0.5) # Space between words
            
            time.sleep(0.6) # Space between letters
        else:
            print(f"Unknown character: {char}")

# --- Main Program ---
while True:
    # Send "SOS" continuously
    transmit("SOS")
    time.sleep(2)
    
    # Uncomment below to send your own message:
    # transmit("Hello World")
    # time.sleep(2)
