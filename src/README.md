# Robot Car JDY-16 - Setup & Library Requirements

## Overview
This project controls a **LAFVIN 4WD Robot Car Kit** via Bluetooth Low Energy (BLE) using a JDY-16 wireless module and keyboard input from a PC. The main Arduino code handles motor direction and speed control, while Python scripts on the PC send driving commands wirelessly.

**Note**: LAFVIN kits are typically designed for Android phone control. This project extends compatibility to Windows PCs via BLE, allowing keyboard-based control without requiring an Android device.

## Hardware Requirements
- Arduino Uno
- JDY-16 BLE Module
- Connection: JDY TX → Pin 0 (RX), JDY RX → Pin 1 (TX)
- Ardiuno MEGA

---

## Arduino/C++ Requirements

### Built-in Libraries (No Installation Needed)
- **Serial** - For BLE communication with JDY-16 module
- **analogWrite()** - PWM control for motor speeds

### Main Code Files
- **Keyboardcontrolarduino.ino** - Main robot control code (receives BLE commands, drives motors)
- **forceconfig.ino** - One-time JDY-16 module configuration to Slave mode

### Upload Instructions
Upload the main code to your Arduino Uno:
```bash
platformio run --target upload -e uno
```

The robot will be ready to receive commands once this is uploaded and the JDY-16 module is configured.

---

## Python Requirements

### Required Python Libraries

#### 1. **bleak** (BLE Communication)
- **Purpose**: Handles Bluetooth Low Energy communication with the JDY-16 module
- **Installation**:
  ```bash
  pip install bleak
  ```
- **Supported Platforms**: Windows, macOS, Linux

#### 2. **keyboard** (Keyboard Input Capture)
- **Purpose**: Captures real-time keyboard input for robot control
- **Installation**:
  ```bash
  pip install keyboard
  ```
- **Note**: Requires admin/root privileges to run scripts using this library

### Built-in Libraries (No Installation Needed)
- **asyncio** - For asynchronous operations
- **encodings** - For UTF-8 encoding/decoding

---

## Installation Instructions

### Step 1: Install Python 3.7+
Download from [python.org](https://www.python.org)

### Step 2: Install Required Packages
Run the following command in your terminal/PowerShell:

```bash
pip install bleak keyboard
```

Or install individually:
```bash
pip install bleak
pip install keyboard
```

### Step 3: Verify Installation
Test if libraries are installed correctly:
```bash
python -c "import bleak; import keyboard; print('All libraries installed successfully!')"
```

---

## Usage

### Phase 1: Upload Main Arduino Code
1. Upload `Keyboardcontrolarduino.ino` to Arduino Uno
   ```bash
   platformio run --target upload -e uno
   ```
2. This code handles motor control based on BLE commands

### Phase 2: Configure JDY-16 Module (One-time Setup)
1. Upload `forceconfig.ino` to your Arduino Mega
   ```bash
   platformio run --target upload -e megaatmega2560
   ```
2. Open Serial Monitor (9600 baud)
3. Should see: `+OK` and `Configuration complete`
4. **Note**: This only needs to be done once per JDY-16 module

### Phase 3: Discover Robot MAC Address
1. **Ensure JDY-16 is powered** - The Bluetooth module must be connected to power and blinking
2. Run `Bluetoothgrabber.py` to find your JDY-16 device:
   ```bash
   python Bluetoothgrabber.py
   ```
3. Note the MAC address (format: `XX:XX:XX:XX:XX:XX`)

### Phase 4: Control the Robot
1. Update `ROBOT_ADDRESS` in `Keyboardcontrol.py` with your robot's MAC address
2. Ensure `Keyboardcontrolarduino.ino` is still uploaded to the Arduino
3. Run with admin/root privileges:
   ```bash
   python Keyboardcontrol.py
   ```
   (On Windows, right-click PowerShell → Run as Administrator)

### Controls
- **W** - Forward (F)
- **S** - Backward (B)
- **A** - Turn Left (L)
- **D** - Turn Right (R)
- **No Key** - Stop (S)
- **ESC** - Exit

---

## Troubleshooting

### "Module not found" Error
- Ensure pip install completed successfully
- Try: `pip install --upgrade bleak keyboard`

### "Permission denied" on keyboard library
- Windows: Run PowerShell as Administrator
- Linux/macOS: Use `sudo python Keyboardcontrol.py`

### Cannot find JDY-16 device
- Ensure JDY-16 is powered and blinking
- Check Bluetooth is enabled on PC
- Verify Arduino is running and has uploaded JDY-16 config

### Connection drops during control
- Check JDY-16 power supply
- Reduce BLE interference (move away from Wi-Fi routers)
- Try reconnecting: restart `Keyboardcontrol.py`

---

## File Structure
```
Robot_Car_JDY16/
├── src/
│   ├── Keyboardcontrolarduino.ino   # Main robot motor control code (upload this)
│   ├── forceconfig.ino              # JDY-16 configuration (one-time setup)
│   ├── Bluetoothgrabber.py          # Discover JDY-16 device MAC address
│   └── Keyboardcontrol.py           # Keyboard-controlled robot driver (PC side)
├── lib/                             # Arduino libraries (if added)
├── platformio.ini                   # Project configuration
└── README.md                        # This file
```

---

## Motor Pin Configuration

The robot uses the following Arduino Uno pins for motor control:

| Function | Arduino Uno Pin | Type |
|----------|---------|------|
| Left Motor Direction | 2 | Digital Output |
| Left Motor Speed | 5 | PWM Output |
| Right Motor Direction | 4 | Digital Output |
| Right Motor Speed | 6 | PWM Output |

### Speed Settings
- **Drive Speed**: 230 (PWM value, 0-255)
- **Turn Speed**: 150 (PWM value, 0-255)

These can be adjusted in `Keyboardcontrolarduino.ino` by modifying:
```cpp
int driveSpeed = 230;  // Adjust for faster/slower forward movement
int turnSpeed  = 150;  // Adjust for tighter/wider turns
```

---

## Version Info
- Python: 3.7 or higher
- Arduino Board: Uno, Mega(for forceconfig)
- JDY-16 Firmware: Standard (configured to Slave/Role 0)
