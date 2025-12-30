# -----------------------------------------------------------------------------
# Lesson 16: Robot Vision (Obstacle Avoidance)
# -----------------------------------------------------------------------------
# Module: KY-032 Obstacle Avoidance Module
# Goal: Stop a robot before it hits a wall.
#
# ANATOMY:
# Active IR: Shoots IR light out and looks for a 'bounce' (reflection).
# - No Bounce  = Open Space.
# - Bounce     = Wall/Object nearby.
#
# TUNING:
# Adjust the two potentiometers on the board to change the RANGE (Distance)
# and the FREQUENCY (Sensitivity).
#
# WIRING:
# - OUT -> GP16
# - +   -> 3.3V
# - G   -> GND
# -----------------------------------------------------------------------------

import machine
import time

class HardwareConfig:
    PIN_SENSOR = 16
    PIN_BRAKES = "LED"

def main():
    # 1. Setup Sensor (Active Low)
    # 0 = Obstacle Detected (Reflection received)
    # 1 = Clear Path
    sensor = machine.Pin(HardwareConfig.PIN_SENSOR, machine.Pin.IN)
    
    # 2. Setup Output (Simulated Brakes/Warning Light)
    brakes = machine.Pin(HardwareConfig.PIN_BRAKES, machine.Pin.OUT)
    
    print("--- SYSTEM READY: ROBOT NAVIGATOR ---")
    print("Move hand towards sensor...")
    
    while True:
        is_obstacle = (sensor.value() == 0)
        
        if is_obstacle:
            print(">>> STOP! OBSTACLE <<<")
            brakes.value(1)
        else:
            brakes.value(0)
            
        time.sleep(0.1)

if __name__ == "__main__":
    main()
