# -----------------------------------------------------------------------------
# Lesson 17: Climate Monitoring (DHT11)
# -----------------------------------------------------------------------------
# Module: KY-015 Temperature & Humidity Sensor (DHT11)
# Goal: Measure both Temperature AND Humidity.
#
# ANATOMY:
# Uses a custom Single-Wire protocol (not I2C, not SPI).
# Requires the built-in 'dht' library.
#
# WIRING:
# - S (Signal) -> GP16
# - (Center)   -> 3.3V
# - (-)        -> GND
# -----------------------------------------------------------------------------

import machine
import dht
import time

class HardwareConfig:
    PIN_DHT = 16
    SAMPLE_RATE_SEC = 2.0 # DHT11 requires > 1.5s between reads

def main():
    # 1. Setup Sensor
    # The 'dht' library handles all the complex timing logic for us.
    try:
        sensor = dht.DHT11(machine.Pin(HardwareConfig.PIN_DHT))
    except Exception as e:
        print(f"Hardware Error: {e}")
        return

    print("--- SYSTEM READY: CLIMATE MONITOR ---")
    print(f"Sampling every {HardwareConfig.SAMPLE_RATE_SEC} seconds...")
    
    while True:
        try:
            # 2. Trigger Measurement
            sensor.measure()
            
            # 3. Read Values
            temp_c = sensor.temperature()
            hum = sensor.humidity()
            
            # Convert C -> F
            temp_f = (temp_c * 9/5) + 32
            
            print(f"Temp: {temp_c}C ({temp_f:.1f}F) | Humidity: {hum}%")
            
        except OSError:
            # Checksum failure or timeout (common with DHT sensors)
            print("Warning: Sensor Read Failed (Retrying...)")
        
        # 4. Wait
        time.sleep(HardwareConfig.SAMPLE_RATE_SEC)

if __name__ == "__main__":
    main()
