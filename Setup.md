# 🛠️ Setup Guide: Zero to Hero

**Welcome to the Lab.**

Before we start wiring up lasers and robots, we need to calibrate our tools. This guide will help you set up your development environment to look and feel like a professional engineering workstation.

---

## 📦 1. Hardware Checklist

Ensure you have the following on your desk:

*   **1x Raspberry Pi Pico** (Pico, Pico W, or Pico 2W).
*   **1x Micro USB Cable** (Ensure it is a *Data* cable, not just a *Charge* cable!).
*   **1x Breadboard** (830 tie-points recommended).
*   **1x 37-in-1 Sensor Kit** (The red PCB modules).
*   **Jumper Wires** (Male-to-Male and Male-to-Female).

---

## 💾 2. Firmware Installation

The "Brain" of the Pico needs an operating system. We use **MicroPython**.

1.  **Download Firmware:**
    *   Go to the [Official MicroPython Website](https://micropython.org/download/rp2-pico/).
    *   Download the latest `.uf2` file (e.g., `v1.23.0`).
2.  **Flash the Pico:**
    *   Hold down the white **BOOTSEL** button on your Pico.
    *   While holding the button, plug the Pico into your computer via USB.
    *   Release the button. A new drive named `RPI-RP2` should appear on your computer.
    *   **Drag and drop** the `.uf2` file into the `RPI-RP2` drive.
    *   The Pico will reboot and disconnect. **Success!** You now have MicroPython installed.

---

## 💻 3. Software Setup (VS Code + Pymakr)

We use **VS Code** because it is the industry standard. We use the **Pymakr** extension to talk to the Pico.

### Step A: Install VS Code
Download and install [Visual Studio Code](https://code.visualstudio.com/) for your OS.

### Step B: Install NodeJS
Pymakr requires NodeJS to run.
*   Download the LTS version from [nodejs.org](https://nodejs.org/).
*   Run the installer and restart your computer if asked.

### Step C: Install the Pymakr Extension
1.  Open VS Code.
2.  Click the **Extensions** icon on the left sidebar (looks like tetris blocks).
3.  Search for `Pymakr`.
4.  Click **Install** (Created by Pycom).
5.  **RESTART VS CODE** after installation.

---

## 🔌 4. Connecting to the Pico

Now we connect the brain to the editor.

1.  **Open this Project:**
    *   In VS Code, go to `File > Open Folder...` and select this repository folder.
2.  **Connect Pymakr:**
    *   Click the **Pymakr** icon in the sidebar (it might look like a plug or chip).
    *   You should seen a device listed under "Devices" (e.g., `COM3` or `/dev/ttyACM0`).
    *   Hover over the device and click the **Connect** (⚡) icon.
    *   A terminal should open at the bottom with `>>>`. This is the **REPL**.

### 🧪 Test It
Type the following into the standard terminal (bottom of screen) inside the `>>>` prompt:

```python
print("Hello World")
```

If it replies `Hello World`, you are ready to code.

---

## ⚡ 5. Breadboard Basics & Safety

**⚠️ IMPORTANT WARNINGS:**
1.  **NEVER** connect 3.3V (Power) directly to GND (Ground). This is a Short Circuit and will kill your Pico.
2.  **ALWAYS** unplug the USB cable before changing wiring.
3.  **LASERS:** Never look into the beam.

### The Power Rails
*   **Red Line (+):** This is for 3.3V Power.
*   **Blue Line (-):** This is for Ground (GND).

Connect the Pico's **3V3(OUT)** pin (Pin 36) to the **Red Rail**.
Connect a Pico **GND** pin (Pin 38) to the **Blue Rail**.
Now the entire rail provides power to your sensors!

---

## 🚀 Ready?

You are setup. Go to **[Phase 1: Outputs](Phase_01_Outputs/)** to start your first mission.
