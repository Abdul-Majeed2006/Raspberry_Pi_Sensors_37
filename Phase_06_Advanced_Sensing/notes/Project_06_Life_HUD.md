# Project 06: The Life Support HUD

**Phase 6 (Graduation) Challenge**

You have mastered the most sensitive sensor in the kit:
*   **The Heartbeat Sensor** (Bio-Metrics)

Now, you must build a survival suit interface... a **Life Support HUD**.

## 🎯 The Mission

You are an astronaut (or a secret agent). Your suit needs to monitor your vital signs.

### Requirements:

1.  **The Monitor:**
    *   Read the Heartbeat sensor data fast.
    *   Print the peak value to the console to simulate a "Heart Rate" readout.
    
2.  **The Life Alert:**
    *   If no "pulse" (dip in light level) is detected for more than 3 seconds...
    *   **CRITICAL FAILURE!** 
    *   Turn the RGB LED **Solid Red**.
    *   Buzz a continuous flatline tone on the **Buzzer**.
    *   Print "STAT: CARDIAC ARREST - REBOOTING..."
    
3.  **The All Clear:**
    *   If heartbeats are detected regularly...
    *   Blink the RGB LED **Green** once per beat.
    *   Make the Buzzer "Click" (short high pitch).

## 🚀 Deliverable

Create `project_06_solution.py`.

This project requires careful threshold tuning. You'll need to use `time.ticks_ms()` to measure the time between beats, just like we did with the Microphone lesson!

Good luck, Cadet. This is your final exam. 👨‍🚀🚀
