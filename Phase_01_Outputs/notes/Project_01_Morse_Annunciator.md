# Project 01: The Morse Code Annunciator

**Phase 1 Capstone Challenge**

You have learned how to use:
*   **RGB LEDs** (Lesson 01)
*   **Passive Buzzers** (Lesson 03)
*   **Laser Transmitters** (Lesson 04)

Now, your mission is to combine them into a single, synchronized communication device. 

## 🎯 The Mission

Build a device that can transmit a secret message (e.g., "HELLO") using **light, sound, and laser** simultaneously.

### Requirements:

1.  **The Input:** define a variable `message = "HELLO WORLD"`.
2.  **The Logic:** Create a loop that goes through each letter.
3.  **The Output (Synchronized):**
    *   **Blue Light:** Flash the RGB LED **Blue** when a DOT is sent.
    *   **Red Light:** Flash the RGB LED **Red** when a DASH is sent.
    *   **Sound:** Play a high note (e.g., 1000Hz) for a DOT and a low note (e.g., 500Hz) for a DASH.
    *   **Laser:** Fire the laser for both Dots and Dashes (so the receiver can see it).

### 📝 Hints

*   You will need a dictionary for Morse Code (steal it from Lesson 04!).
*   You will need to import `machine` and `time`.
*   Remember to turn **OFF** all components (LED, Laser, Buzzer) during the "gaps" between signals.

## 🚀 Deliverable

Create a new file called `project_01_solution.py`.
Write the code from scratch. **No copying and pasting entire blocks!** Type it out to build muscle memory.

Good luck, Agent. \ud83d\udd75\ufe0f\u200d\u2642\ufe0f
