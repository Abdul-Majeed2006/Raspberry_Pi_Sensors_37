# User Guide: The Omni-Sentry

## 🔌 Wiring Guide (The "Spider Web")
This project uses **12 wires** connected to the Pico. Use a breadboard rail for 3.3V and GND!

### 1. The Controller (Left Side)
*   **Rotary Encoder (KY-040)**
    *   `CLK` -> **GP2**
    *   `DT`  -> **GP3**
    *   `SW`  -> **GP4**
    *   `+`   -> 3.3V
    *   `GND` -> GND

### 2. The Feedback (Left Side)
*   **RGB LED (KY-016)** - *Common Cathode assumed*
    *   `R`   -> **GP13**
    *   `G`   -> **GP14**
    *   `B`   -> **GP15**
    *   `GND` -> GND

*   **Buzzer (KY-006)**
    *   `S`   -> **GP12**
    *   `-`   -> GND

### 3. The Sensors (Right Side)
*   **Motion Sensor (KY-032 or KY-002)**
    *   `OUT` -> **GP16** (Digital)
*   **Thermistor (KY-013)**
    *   `S`   -> **GP26** (Analog 0)
*   **Photoresistor (KY-018)**
    *   `S`   -> **GP27** (Analog 1)

---

## 🕹️ Operation Manual

### System Start
When you plyg in the Pico, you will hear a **Two-Tone Chime** and the LED will breathe **Green**. This is **IDLE MODE**.

### Changing Modes
1.  **Press the Rotary Encoder Switch** to cycle through modes:
    *   **GREEN (Idle)**: System is sleeping. Safe.
    *   **BLUE (Agitated)**: **ARMED MODE**. The Sentry is watching.
    *   **RED (Flashing)**: **ALARM MODE**. Intruder detected! Siren will sound.

### The "Rules"
*   **ALARM**: If *Motion* is detected while in **ARMED** mode, the specific goes instantly to **ALARM**.
    *   *To Reset*: Press the button again to return to IDLE.
*   **FLASHLIGHT**: In **ARMED** mode, if the room gets *Dark*, the LED will turn **White**. This is the "Night Vision" feature.
