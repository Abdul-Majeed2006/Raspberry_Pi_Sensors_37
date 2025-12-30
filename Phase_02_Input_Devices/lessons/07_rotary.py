# -----------------------------------------------------------------------------
# Lesson 07: Spinning Control (Rotary Encoder)
# -----------------------------------------------------------------------------
# Module: KY-040 Rotary Encoder Module
# Goal: Precise rotational tracking using Quadrature Encoding.
#
# ANATOMY:
# A Rotary Encoder sends two square waves (Griffith & Gray Code).
# By detecting WHICH pin changed first, we know the direction.
#
# WIRING:
# - GND -> GND
# - +   -> 3.3V
# - DT  -> GP17 (Data)
# - CLK -> GP16 (Clock)
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_CLK = 16
    PIN_DT  = 17

# --- Global State (Required for Interrupts) ---
# We store these outside the function because the IRQ needs to access them fast.
encoder_count = 0
last_clk_state = 0

def on_rotate(pin):
    """
    Interrupt Handler (IRQ). 
    This function runs AUTOMATICALLY whenever the CLK pin changes.
    """
    global encoder_count, last_clk_state
    
    # 1. Read the new state
    current_clk = clk_pin.value()
    current_dt = dt_pin.value()
    
    # 2. Key Logic: If CLK changed, check DT to find direction
    if current_clk != last_clk_state:
        if current_dt != current_clk:
            # Clockwise
            encoder_count += 1
            print(f">>> CW  [{encoder_count}]")
        else:
            # Counter-Clockwise
            encoder_count -= 1
            print(f"<<< CCW [{encoder_count}]")
            
    # 3. Update State
    last_clk_state = current_clk

# --- Setup ---
clk_pin = machine.Pin(HardwareConfig.PIN_CLK, machine.Pin.IN)
dt_pin = machine.Pin(HardwareConfig.PIN_DT, machine.Pin.IN)

# Initialize state
last_clk_state = clk_pin.value()

# --- Attach Interrupt ---
# Instead of a "While True" loop checking 1000 times a second, 
# we tell the CPU: "Wake up and run 'on_rotate' ONLY when the pin changes."
clk_pin.irq(trigger=machine.Pin.IRQ_CHANGE, handler=on_rotate)

print("--- ENCODER ACTIVE (IRQ MODE) ---")
print("Spin the knob. The main loop does NOTHING!")

while True:
    # Proof that the main loop is free to do other things
    # You could run a whole game here, and the encoder would still work!
    time.sleep(1)
