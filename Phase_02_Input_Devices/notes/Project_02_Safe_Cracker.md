# Project 02: The Digital Safe Cracker

**Phase 2 Capstone Challenge**

You have mastered Inputs:
*   **Buttons** (Digital)
*   **Joysticks** (Analog)
*   **Encoders** (Counting)

Now, you must build a security system.

## 🎯 The Mission

Build a "Combination Lock" game.
The user must rotate the encoder to the correct numbers and press a button to unlock the safe.

### The Combination: `3 - 7 - 12`

### Requirements:

1.  **Hardware:**
    *   Rotary Encoder (for dialing numbers).
    *   Push Button (built-in to encoder or separate) for "Enter".
    *   RGB LED (for status).

2.  **The Logic:**
    *   Start at `0`.
    *   **Phase 1:** Rotate until the print output says `3`. Press Button.
        *   *If correct:* LED flashes **Green**. Move to Phase 2.
        *   *If incorrect:* LED flashes **Red**. Reset to start!
    *   **Phase 2:** Rotate to `7`. Press Button.
    *   **Phase 3:** Rotate to `12`. Press Button.
    *   **Victory:** If all three are correct, turn the LED **Blue** and keep it on!

### 📝 Hints

*   Reuse your "Volume Knob" code concepts to track the number.
*   You will need a variable like `current_stage` to track if you are looking for the 1st, 2nd, or 3rd number.
*   Use `time.sleep(0.5)` after a button press so you don't accidentally press it twice.

## 🚀 Deliverable

Create `project_02_solution.py`.
This is a complex logic puzzle. Draw a flowchart if you get stuck!

Good luck, Safecracker. \ud83d\udd12\ud83d\udc40
