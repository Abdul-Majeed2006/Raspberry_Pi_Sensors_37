# -----------------------------------------------------------------------------
# Lesson 03: Making Noise (Buzzers)
# -----------------------------------------------------------------------------
# Modules: KY-006 (Passive) / KY-012 (Active)
# Goal: Create sound waves using PWM.
#
# ANATOMY:
# - Active: Needs only Power (DC) to scream.
# - Passive: Needs a Wave (AC/PWM) to make notes.
#
# WIRING:
# - S/+ -> GP16
# - -   -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_BUZZER = 16

class MusicTheory:
    """Frequency table for notes (Hz)."""
    NOTES = {
        'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349,
        'G4': 392, 'A4': 440, 'B4': 494, 'C5': 523,
        'REST': 0
    }

def play_note(pwm_device, freq, duration):
    if freq == 0:
        pwm_device.duty_u16(0) # Silence
    else:
        pwm_device.freq(freq)
        pwm_device.duty_u16(32768) # 50% Duty = Square Wave (Loudest)
    
    time.sleep(duration)
    pwm_device.duty_u16(0) # Stop sound after note

def main():
    buzzer = machine.PWM(machine.Pin(HardwareConfig.PIN_BUZZER))
    
    # Melody: (Note Name, Duration)
    melody = [
        ('E4', 0.2), ('E4', 0.2), ('REST', 0.2), ('E4', 0.2),
        ('C4', 0.2), ('E4', 0.4), ('G4', 0.4)
    ]
    
    print("--- SYSTEM READY: MUSIC PLAYER ---")
    
    for note_name, duration in melody:
        print(f"Playing: {note_name}")
        freq = MusicTheory.NOTES.get(note_name, 0)
        play_note(buzzer, freq, duration)
        time.sleep(0.05) # Staccato gap

if __name__ == "__main__":
    main()
