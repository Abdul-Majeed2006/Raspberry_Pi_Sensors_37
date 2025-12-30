# -----------------------------------------------------------------------------
# Capstone Project: The Omni-Sentry
# -----------------------------------------------------------------------------
# A multi-threaded security and environment monitoring system.
#
# WIRING MAP:
# [UI INPUT]  Rotary Encoder
# - CLK -> GP2
# - DT  -> GP3
# - SW  -> GP4
# - +   -> 3.3V
# - G   -> GND
#
# [UI OUTPUT] RGB LED (Common Cathode)
# - R   -> GP13
# - G   -> GP14
# - B   -> GP15
# - -   -> GND
#
# [AUDIO] Buzzer
# - S   -> GP12
# - -   -> GND
#
# [SENSORS]
# - Motion (IR/Vibration) -> GP16 (Digital)
# - Thermistor            -> GP26 (Analog 0)
# - Photoresistor         -> GP27 (Analog 1)
# -----------------------------------------------------------------------------

import machine
import time
import math

# --- HARDWARE CONFIGURATION ---
class HardwareConfig:
    # 1. UI Elements
    PIN_ENC_CLK = 2
    PIN_ENC_DT  = 3
    PIN_ENC_SW  = 4
    
    PIN_RGB_R   = 13
    PIN_RGB_G   = 14
    PIN_RGB_B   = 15
    
    PIN_BUZZER  = 12
    
    # 2. Sensors
    PIN_MOTION  = 16 # Active Low (0 = Trigger) usually
    PIN_TEMP    = 26
    PIN_LIGHT   = 27
    
    # 3. Tuning
    TEMP_BETA   = 3950
    LIGHT_THRESHOLD = 30000 # Below this is "Dark"

# --- SUBSYSTEM: I/O MANAGER ---
class IOManager:
    def __init__(self):
        # RGB LED
        self.r = machine.PWM(machine.Pin(HardwareConfig.PIN_RGB_R))
        self.g = machine.PWM(machine.Pin(HardwareConfig.PIN_RGB_G))
        self.b = machine.PWM(machine.Pin(HardwareConfig.PIN_RGB_B))
        self.r.freq(1000); self.g.freq(1000); self.b.freq(1000)
        
        # Buzzer
        self.buzzer = machine.PWM(machine.Pin(HardwareConfig.PIN_BUZZER))
        self.buzzer.duty_u16(0) # Silence
        
    def set_color(self, r_val, g_val, b_val):
        self.r.duty_u16(r_val)
        self.g.duty_u16(g_val)
        self.b.duty_u16(b_val)
        
    def beep(self, freq, duration):
        if freq > 0:
            self.buzzer.freq(freq)
            self.buzzer.duty_u16(32768)
        time.sleep(duration)
        self.buzzer.duty_u16(0)

# --- SUBSYSTEM: SENSOR ARRAY ---
class SensorArray:
    def __init__(self):
        self.motion = machine.Pin(HardwareConfig.PIN_MOTION, machine.Pin.IN)
        self.temp_adc = machine.ADC(HardwareConfig.PIN_TEMP)
        self.light_adc = machine.ADC(HardwareConfig.PIN_LIGHT)
        
    def check_motion(self):
        # Returns True if motion detected (Active Low assumed for KY-032/002)
        return self.motion.value() == 0 
        
    def get_temp_c(self):
        raw = self.temp_adc.read_u16()
        if raw == 0 or raw == 65535: return 0
        
        # Steinhart-Hart Equation
        voltage = (raw / 65535) * 3.3
        try:
            r_therm = (10000 * voltage) / (3.3 - voltage)
            inv_t = (1/298.15) + (1/HardwareConfig.TEMP_BETA) * math.log(r_therm/10000)
            return (1/inv_t) - 273.15
        except:
            return 0
            
    def get_light_level(self):
        return self.light_adc.read_u16()

# --- MAIN CONTROLLER (STATE MACHINE) ---
class SystemController:
    STATE_IDLE  = 0
    STATE_ARMED = 1
    STATE_ALARM = 2
    
    def __init__(self):
        self.io = IOManager()
        self.sensors = SensorArray()
        self.state = self.STATE_IDLE
        
        # Rotary Encoder Logic needs Interrupts (Simplified here for readability)
        self.enc_sa = machine.Pin(HardwareConfig.PIN_ENC_CLK, machine.Pin.IN)
        self.enc_sb = machine.Pin(HardwareConfig.PIN_ENC_DT, machine.Pin.IN)
        self.enc_sw = machine.Pin(HardwareConfig.PIN_ENC_SW, machine.Pin.IN, machine.Pin.PULL_UP)
        self.btn_prev = 1
        
        print("--- OMNI-SENTRY ONLINE ---")
        self.io.beep(2000, 0.1) # Startup Chime
        self.io.beep(3000, 0.1)
        
    def update(self):
        # 1. Check User Input (Mode Switch)
        btn_now = self.enc_sw.value()
        if btn_now == 0 and self.btn_prev == 1:
            # Button Pressed -> Cycle State
            self.cycle_state()
            time.sleep(0.2) # Debounce
        self.btn_prev = btn_now
        
        # 2. Run State Logic
        if self.state == self.STATE_IDLE:
            self.run_idle()
        elif self.state == self.STATE_ARMED:
            self.run_sentry()
        elif self.state == self.STATE_ALARM:
            self.run_alarm()
            
        time.sleep(0.05) # Loop pacing
        
    def cycle_state(self):
        if self.state == self.STATE_ALARM:
            print(">>> ALARM RESET <<<")
            self.state = self.STATE_IDLE
        elif self.state == self.STATE_IDLE:
            print(">>> SYSTEM ARMED <<<")
            self.io.beep(1000, 0.1)
            self.state = self.STATE_ARMED
        elif self.state == self.STATE_ARMED:
            print(">>> SYSTEM STANDBY <<<")
            self.state = self.STATE_IDLE
            
    # --- STATE HANDLERS ---
    def run_idle(self):
        # Green Pulse (Breathing Effect)
        # Using a simple math.sin wave based on time
        now = time.ticks_ms() / 1000 
        brightness = int(32000 + 30000 * math.sin(now * 2))
        self.io.set_color(0, brightness, 0) # Green
        
        # Monitor Environment passively
        temp = self.sensors.get_temp_c()
        # print(f"Idle.. Temp: {temp:.1f}C") # Optional debug
        
    def run_sentry(self):
        # Blue Steady Light
        self.io.set_color(0, 0, 60000)
        
        # 1. Check Motion
        if self.sensors.check_motion():
            print("!!! MOTION DETECTED !!!")
            self.state = self.STATE_ALARM
            return
            
        # 2. Check Dark/Light
        light = self.sensors.get_light_level()
        if light < HardwareConfig.LIGHT_THRESHOLD:
            # Too Dark? Turn on "Flashlight" (White LED mix)
            # We override the Blue sentry light temporarily
            self.io.set_color(20000, 20000, 20000)
            
    def run_alarm(self):
        # Red Strobe & Siren
        now = int(time.ticks_ms() / 200) # Fast toggle
        if now % 2 == 0:
            self.io.set_color(65535, 0, 0) # Red
            self.io.buzzer.freq(3000)
            self.io.buzzer.duty_u16(32768)
        else:
            self.io.set_color(0, 0, 0) # Off
            self.io.buzzer.freq(1000)
            self.io.buzzer.duty_u16(32768)

# --- ENTRY POINT ---
def main():
    sys = SystemController()
    
    while True:
        try:
            sys.update()
        except KeyboardInterrupt:
            # Safe Shutdown
            sys.io.set_color(0,0,0)
            sys.io.buzzer.duty_u16(0)
            print("\nOmni-Sentry Offline.")
            break

if __name__ == "__main__":
    main()
