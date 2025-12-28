import machine

# --- POKE TEST TOOL ---
# This script turns ALL specified pins ON simultaneously.
# This allows you to 'probe' your hardware without stopping the code.

# --- CONFIGURATION ---
# We test the Bottom-Right cluster (16, 17, 18) and the Analog block (26, 27).
TEST_PINS = [16, 17, 18, 26, 27]

print("========================================")
print("       THE 'POKE' TEST TOOL")
print("========================================")
print(f"Setting Clustered Pins {TEST_PINS} to HIGH.")
print("\nTROUBLESHOOTING STEPS:")
print("1. Keep this script running.")
print("2. Take a wire connected to your LED/Buzzer.")
print("3. Touch ('Poke') that wire into the pins listed above.")
print("4. If the LED lights up on GP16 but NOT GP13, your GP13 is likely dead.")
print("----------------------------------------\n")

# Initialize and turn on all pins
active_pins = []
for p in TEST_PINS:
    try:
        pin_obj = machine.Pin(p, machine.Pin.OUT)
        pin_obj.value(1)
        active_pins.append(pin_obj)
    except Exception as e:
        print(f"Skipping GP{p}: {e}")

print("All pins are now ACTIVE. Good luck probing!")

# Keep alive
while True:
    pass
