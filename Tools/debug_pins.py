import machine
import time

# --- HARDWARE CONFIGURATION ---
# We test the "Bottom-Right Cluster" (GP16, 17, 18) and ADC block (26, 27).
PINS_TO_TEST = [16, 17, 18, 26, 27]

print("========================================")
print("     CLUSTERED WIRING DIAGNOSTIC")
print("========================================")
print(f"Testing Pins: {PINS_TO_TEST}")
print("Instructions:")
print("1. We are testing the Bottom-Right block of the Pico.")
print("2. If the component DOES NOT turn on, that pin might be 'dead' or broken.")
print("3. In that case, you must change the pin number in YOUR code to a working one.")
print("----------------------------------------\n")

for p in PINS_TO_TEST:
    print(f"--> NOW TESTING: GP{p}")
    try:
        test_pin = machine.Pin(p, machine.Pin.OUT)
        
        print(f"    GP{p} set to HIGH (ON)")
        test_pin.value(1)
        time.sleep(2)
        
        print(f"    GP{p} set to LOW (OFF)")
        test_pin.value(0)
        time.sleep(1)
    except Exception as e:
        print(f"    Error testing GP{p}: {e}")

print("\nDIAGNOSTIC COMPLETE.")
print("Did it work? If not, check your breadboard alignment first!")
