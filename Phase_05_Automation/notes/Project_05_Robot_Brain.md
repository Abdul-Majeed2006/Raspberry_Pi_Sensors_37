# Project 05: The Robot Brain

**Phase 5 Capstone Challenge**

You have mastered Automation:
*   **Relays** (Switching)
*   **Tripwires** (Security)
*   **Robot Vision** (Obstacle Avoidance)

Now, you must build the brain for a **Sentry Robot**.

## 🎯 The Mission

Your robot is guarding a hallway. It has three states:
1.  **Patrol (Green Light):** Driving forward, safe.
2.  **Obstacle (Yellow Light):** Wall detected, stopping.
3.  **Attack (Red Light):** Intruder detected (Tripwire broken)!

### Requirements:

1.  **The Inputs:**
    *   **Obstacle Sensor:** Front facing.
    *   **IR Tripwire:** Side facing (The "check point").

2.  **The Outputs:**
    *   **RGB LED:** Status Indicator.
    *   **Relay:** Imagine this is the "Motor Power".

3.  **The Logic Loop:**
    *   **IF Tripwire Broken:**
        *   **Red Alert!** Flash Red LED fast.
        *   Cut Relay Power (Stop motors to capture intruder).
        *   Print "INTRUDER ALERT!".
    *   **ELSE IF Obstacle Detected:**
        *   **Caution.** Turn LED Yellow.
        *   Cut Relay Power (Stop to avoid crash).
        *   Print "Wall Ahead. Stopping.".
    *   **ELSE (All Clear):**
        *   **Patrol.** Turn LED Green.
        *   Enable Relay Power (Motors ON).
        *   Print "Patrolling...".

## 🚀 Deliverable

Create `project_05_solution.py`.
This code is actually very close to how real industrial robots work (Safety Curtains).

Good luck, Commander. \ud83e\udee1
