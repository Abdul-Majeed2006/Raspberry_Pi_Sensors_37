# -----------------------------------------------------------------------------
# Lesson 03: Making Noise (Active vs Passive Buzzers)
# -----------------------------------------------------------------------------
# Modules: KY-006 (Passive) / KY-012 (Active)
# Goal: Learn the difference between Active and Passive buzzers.
#       Types of buzzers in your kit:
#       1. Active Buzzer (Usually has a "REMOVE SEAL" sticker). Beeps when powered.
#       2. Passive Buzzer (Green circuit board on back exposed). Needs PWM to make notes.
#
# WIRING:
# - Positive (+) -> GP15
# - Negative (-) -> GND
#
# Skills Learnt:
# - Passive vs Active Components
# - Frequencies & Pitch
# - Python Lists & Tuples
# -----------------------------------------------------------------------------

import machine
import time

# Setup the Buzzer pin as PWM (Pulse Width Modulation)
# We use PWM to create sound waves (notes) for the Passive Buzzer.
buzzer = machine.PWM(machine.Pin(15))

def play_tone(frequency, duration):
    """
    Plays a specific note (frequency) for a set time.
    """
    if frequency == 0:
        buzzer.duty_u16(0) # Logic for "Rest" (Silence)
    else:
        buzzer.freq(frequency)  # Set pitch
        buzzer.duty_u16(32768)  # Set volume (50% duty cycle is loudest)
    
    time.sleep(duration)
    buzzer.duty_u16(0) # Turn off after note is done

# --- Part 1: The Active Buzzer Test ---
# If you have an Active Buzzer connected, this will just BEEP on/off.
# If you have a Passive Buzzer, this will sound like specific notes.
print("Playing Scale...")

# Frequencies for notes (C4 to C5)
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

# Play a melody (Super Mario-ish theme intro)
melody = [
    ('E4', 0.15), ('E4', 0.15), ('Rest', 0.15), ('E4', 0.15), 
    ('Rest', 0.15), ('C4', 0.15), ('E4', 0.3), ('G4', 0.3), ('Rest', 0.3)
]

for note_name, duration in melody:
    print(f"Playing {note_name}")
    if note_name == 'Rest':
        play_tone(0, duration)
    else:
        play_tone(notes[note_name], duration)
    time.sleep(0.05) # Tiny gap between notes

print("Done!")
