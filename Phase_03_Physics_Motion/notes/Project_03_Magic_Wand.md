# Project 03: The Magic Wand

**Phase 3 Capstone Challenge**

You have mastered the physics of the real world:
*   **Movement** (Shake/Tilt)
*   **Magnetism** (Hall Effect)
*   **Sound** (Microphone)

Now, you will build an interactive **Magic Wand**.

## 🎯 The Mission

Create a device that reacts to gestures and physical forces.

### Requirements:

1.  **The Charge (Shake):**
    *   Use the **Vibration Switch**.
    *   Every time you shake the wand, increase a `mana` variable.
    *   Print "Mana: [Value]" to the console.
    *   *(Bonus: Make the LED brighter as Mana increases!)*

2.  **The Spell (Cast):**
    *   Use the **Tilt Switch** OR **Sound Sensor**.
    *   When triggered (Tilted down or Loud Noise), check if `mana > 10`.
    *   If Yes: **CAST SPELL!** Flash the LED rapidly and play a sound on the Buzzer. Reset Mana to 0.
    *   If No: **FIZZLE...** Blink the LED once slowly.

3.  **The Curse (Magnet):**
    *   Use the **Hall Effect Sensor**.
    *   If a magnet gets close, the wand is **CURSED**.
    *   Drain all `mana` to 0 immediately and play a sad tone.

## 🚀 Deliverable

Create `project_03_solution.py`.
This project requires managing variables (`mana`) and checking multiple sensors in a single loop.

*Tip: Use `time.ticks_ms()` for cooldowns so that one shake doesn't count as 50 shakes!*

Good luck, Wizard. \ud83e\uddd9\u200d\u2642\ufe0f\u2728
