# Project 04: The Weather Station

**Phase 4 Capstone Challenge**

You have mastered Environmental Sensing:
*   **Temperature** (Heat)
*   **Humidity** (Dampness)
*   **Light** (Brightness)
*   **Fire** (Safety)

Now, you must build a comprehensive **Digital Climate Dashboard**.

## 🎯 The Mission

Build a program that constantly monitors the room and reports the status.

### Requirements:

1.  **The Monitor Loop:**
    *   Every 2 seconds, read **Temp**, **Light**, and **Flame** sensors.
    *   Print a clean "Dashboard" to the console:
        ```text
        --- STATUS REPORT ---
        Temp:  24.5 C
        Light: 45000 (Bright)
        Fire:  SAFE
        ---------------------
        ```

2.  **The Alerts:**
    *   **Night Mode:** If Light < 5000, turn on the **White LED** (RGB: 100% Red, 100% Green, 100% Blue).
    *   **Heat Wave:** If Temp > 30 C, turn on the **Red LED**.
    *   **Fire Alarm:** If Fire is detected, override everything! Flash **Red/Blue** and Sound the **Siren**.

## 🚀 Deliverable

Create `project_04_solution.py`.

*Tip: You will need to copy your `steinhart_hart` math logic from Lesson 11 into this new file.*

Good luck, Meteorologist. \u2600\ufe0f\ud83c\udf27\ufe0f
