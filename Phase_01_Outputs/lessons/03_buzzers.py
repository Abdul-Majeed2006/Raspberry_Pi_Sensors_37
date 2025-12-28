# -----------------------------------------------------------------------------
# Lesson 03: Making Noise (Active vs Passive Buzzers)
# -----------------------------------------------------------------------------
# Modules: KY-006 (Passive) / KY-012 (Active)
# Goal: Understand how sound is made by vibrating a membrane with electricity.
#
# WHY THIS MATTERS:
# Sound is just air vibrating. By vibrating a buzzer at specific speeds, we 
# can create "Notes." This is how your microwave beeps or your car's parking 
# sensors work.
#
# PASSIVE VS ACTIVE:
# 1. Active Buzzer: Like a siren. It has its own "brain" inside. Give it 
#    power, and it screams at one constant volume and pitch.
# 2. Passive Buzzer: Like a speaker. It is "dumb" and needs us to send a 
#    vibrating signal (PWM) to make it do anything. This is what we use 
#    to play songs!
#
# WIRING:
# - Positive (+) -> GP16
# - Negative (-) -> GND
# -----------------------------------------------------------------------------

import machine
import time

# --- Setup Pins ---
# We use PWM to "vibrate" the pin. 
# We use GP16 (Pin 21) which is easy to find at the bottom-right corner.
buzzer = machine.PWM(machine.Pin(16))

def play_note(frequency, duration):
    """
    Plays a musical note.
    - frequency: The "Pitch" (how high or low). Measured in Hz.
    - duration: How long the note lasts in seconds.
    """
    if frequency == 0:
        # If frequency is 0, we set duty cycle to 0 (No power = Silence).
        buzzer.duty_u16(0) 
    else:
        # .freq() sets the speed of vibration.
        buzzer.freq(frequency)  
        
        # .duty_u16 sets the volume. 
        # 32768 is exactly half of 65535, which creates a perfect "Square Wave."
        buzzer.duty_u16(32768)  
    
    time.sleep(duration)
    
    # It is VERY IMPORTANT to turn the buzzer off (set duty to 0) 
    # after the note ends, otherwise it will hum forever!
    buzzer.duty_u16(0) 

# --- Musical Data (Dictionaries) ---
# A dictionary maps a name (C4) to a value (262 Hz).
notes = {
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349,
    'G4': 392, 'A4': 440, 'B4': 494, 'C5': 523
}

# --- The Melody (A Tuple List) ---
# Each item is (NOTE_NAME, DURATION)
melody = [
    ('E4', 0.15), ('E4', 0.15), ('Rest', 0.15), ('E4', 0.15), 
    ('Rest', 0.15), ('C4', 0.15), ('E4', 0.3), ('G4', 0.3)
]

print("Playing melody... Can you guess the song?")

for note_name, duration in melody:
    print(f"Note: {note_name}")
    if note_name == 'Rest':
        play_note(0, duration)
    else:
        # We look up the note name in our 'notes' dictionary to get the Hz.
        play_note(notes[note_name], duration)
    
    # A tiny gap between notes makes them sound more distinct.
    time.sleep(0.05) 

print("Done! You just programmed a digital instrument.")
