# 🏆 Capstone Project: The Omni-Sentry

**"One Device. Infinite Awareness."**

This project is the final exam of the **37-in-1 Sensor Masterclass**. It combines inputs, outputs, environmental sensing, and automation into a single, multi-threaded security device.

## 🎯 The Mission

Build a **Multi-Mode Security System** that protects a room using 5 active modules simultaneously.

### The Modes:

1.  **Mode 1: Sentry (Motion)**
    *   **Sensor:** IR Obstacle (KY-032) or Vibration (KY-002).
    *   **Action:** If motion is detected -> **RED ALERT**.
2.  **Mode 2: Climate (Environment)**
    *   **Sensor:** Thermistor (KY-013) or DHT11.
    *   **Action:** If Temp > 30°C -> **YELLOW WARNING**.
3.  **Mode 3: Shadow (Light)**
    *   **Sensor:** Photoresistor (KY-018).
    *   **Action:** If Light < Threshold (Dark) -> **WHITE FLASHLIGHT**.

## 🛠️ Hardware Requirements

*   **Pico**: The Brain.
*   **Rotary Encoder (KY-040)**: The Mode Selector (Scroll to change mode, Click to Reset).
*   **RGB LED (KY-016)**: The Status Indicator.
*   **Buzzer (KY-006)**: The Alarm Siren.
*   **Various Sensors**: As listed above.

## 🧠 Engineering Concepts Learned

*   **State Machines**: How to switch logic without restarting the code.
*   **Non-Blocking Loops**: Managing 5 sensors without `time.sleep()`.
*   **Hardware Abstraction**: Using our `HardwareConfig` class to keep code clean.
