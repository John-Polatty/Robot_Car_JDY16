# Libraries for LAFVIN 4WD Robot Car with JDY-16 BLE Control

This directory is intended for project-specific Arduino libraries. Currently, this project uses built-in Arduino libraries and does not require external Arduino libraries.

---

## Arduino Libraries (Built-in)

### Core Libraries
- **Serial** - Built-in UART communication
  - Used for: JDY-16 Bluetooth module communication on both Arduino Uno and Mega
  - No installation needed

- **analogWrite()** - PWM output (built-in function)
  - Used for: Motor speed control via PWM on pins 5 and 6

---

## Python Libraries (PC-side)

Install these Python packages on your Windows PC:

### 1. bleak
**Purpose**: Bluetooth Low Energy (BLE) communication  
**Installation**: `pip install bleak`  
**Documentation**: https://bleak.readthedocs.io/

### 2. keyboard
**Purpose**: Real-time keyboard input capture  
**Installation**: `pip install keyboard`  
**Documentation**: https://github.com/boppreh/keyboard

### 3. asyncio (Built-in)
**Purpose**: Asynchronous I/O for non-blocking Bluetooth and keyboard operations  
**Installation**: Built-in to Python 3.7+  
**Documentation**: https://docs.python.org/3/library/asyncio.html

---

## Adding Arduino Libraries (if needed in the future)

If you need to add external Arduino libraries, place them in separate subdirectories:

```
lib/
├── LibraryName1/
│   ├── src/
│   │   ├── LibraryName1.cpp
│   │   └── LibraryName1.h
│   ├── library.json
│   └── README.md
│
└── LibraryName2/
    ├── src/
    └── library.json
```

Then add to `platformio.ini`:
```ini
lib_deps = 
    path/to/LibraryName1
    path/to/LibraryName2
```

---

## Useful PlatformIO Library Links

- **PlatformIO Library Manager**: https://platformio.org/lib
- **Search for Arduino Libraries**: https://platformio.org/lib?query=search
- **Library Documentation**: https://docs.platformio.org/page/librarymanager/index.html
- **How to Add Dependencies**: https://docs.platformio.org/page/projectconf/sections/env/options/library/lib_deps.html

---

## Current Project Dependencies Summary

| Component | Type | Status |
|-----------|------|--------|
| Serial (UART) | Arduino Built-in | ✓ Included |
| analogWrite (PWM) | Arduino Built-in | ✓ Included |
| asyncio | Python Built-in | ✓ Included |
| bleak | Python Package | Install with: `pip install bleak` |
| keyboard | Python Package | Install with: `pip install keyboard` |

---

## Notes

- The JDY-16 module communicates via standard UART/Serial, so no special Bluetooth library is needed on the Arduino side
- All motor control uses basic PWM, no motor library dependency
- Python libraries are installed separately on your PC, not compiled with the Arduino code
