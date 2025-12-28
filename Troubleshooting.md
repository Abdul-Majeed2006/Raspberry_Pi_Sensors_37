# 🔧 Troubleshooting Guide

**Don't Panic.**

Engineering is 10% building and 90% debugging. If something isn't working, you are likely just one step away from fixing it.

---

## 🔌 1. Connection Issues

### "My Computer doesn't see the Pico"

*   **The Cable:** 95% of the time, it's the USB cable. Many cables are "Charge Only". You need a **Data Cable**. Try a different cable.
*   **The Port:** Try a different USB port on your computer.
*   **The Button:** Did you hold `BOOTSEL` while plugging it in *only* when installing firmware? For normal use, just plug it in *without* holding the button.

### "Pymakr says 'Disconnected'"

*   **Click Lightning:** Hover over the device in the Pymakr sidebar and click the ⚡ (Connect) icon.
*   **Restart VS Code:** Sometimes the extension just needs a nap. Close and re-open VS Code.
*   **Check Other Apps:** Is Cura, Thonny, or Arduino IDE open? They might be "hogging" the USB port. Close them.

---

## 🐍 2. Code Errors

### "IndentationError: unexpected indent"

Python is very strict about spaces.

*   Ensure all code inside a `while` loop or `if` statement is indented by **4 spaces** (or 1 tab).
*   Do not mix tabs and spaces.

### "NameError: name 'Pin' is not defined"

*   Did you import the library?
*   Top of file: `from machine import Pin`

### "OSError: [Errno 5] EIO"

*   This usually means Pymakr lost connection. Unplug the Pico, plug it back in, and click Connect ⚡.

---

## 💡 3. Hardware Gremlins

### "The LED won't turn on"

*   **Polarity:** LEDs have a positive (+) and negative (-) leg. The **Long Leg** is Positive.
*   **Wiring:** Check your breadboard rails. Is the Red Rail actually connected to 3.3V? Is the Blue Rail connected to GND?

### "The Sensor is getting hot!"

*   **UNPLUG IMMEDIATELY.**
*   You probably created a Short Circuit (Power touching Ground). Check your wiring carefully.

---

## 👻 4. Dead Pins (The Ghost in the Machine)

Sometimes, a specific pin on your Pico stops working due to a static shock or a previous short circuit.

### "I moved the wire, but nothing happens!"
If you follow the code and wiring perfectly, but one pin stays silent while others work:
1.  **Test the Pin:** Use the **`Tools/debug_pins.py`** script in this repository.
2.  **Confirm the Death:** If the debug script fails to light up that specific pin, it is likely "Dead."
3.  **The Fix:** Simply move your wire to a DIFFERENT GP hole (e.g., move from 13 to 16) and update the pin number in your Python code: `led = Pin(16)`.

## 🆘 Still Stuck?

1.  Take a deep breath.
2.  Read the error message in the terminal. It usually tells you exactly which line number is broken.
3.  Check the wiring diagram in the Lesson Note again.
