import asyncio
import keyboard
from bleak import BleakClient

# --- CONFIGURATION ---
# Replace with your JDY-16 address (e.g., "00:0E:0B:XX:XX:XX")
ROBOT_ADDRESS = "YOUR_DEVICE"

# The standard JDY-16 / MLT-BT05 UUID for serial data
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

class RobotPilot:
    def __init__(self):
        self.last_sent = None

    async def send(self, client, cmd):
        """Only sends the command if it's different from the last one to avoid lag."""
        if self.last_sent != cmd:
            await client.write_gatt_char(CHARACTERISTIC_UUID, cmd.encode())
            self.last_sent = cmd
            print(f"Robot State: {cmd}")

async def main():
    pilot = RobotPilot()
    print(f"Connecting to Victo-Bot ({ROBOT_ADDRESS})...")
    
    try:
        async with BleakClient(ROBOT_ADDRESS) as client:
            if not client.is_connected:
                print("Failed to connect.")
                return

            print("\n" + "="*30)
            print("  CONNECTION SUCCESSFUL")
            print("="*30)
            print("  W -> Forward (F)")
            print("  S -> Backward (B)")
            print("  A -> Turn Left (L)")
            print("  D -> Turn Right (R)")
            print("  No Key -> Stop (S)")
            print("  ESC -> Exit")
            print("="*30 + "\n")

            while True:
                if keyboard.is_pressed('w'):
                    await pilot.send(client, 'F')
                elif keyboard.is_pressed('s'):
                    await pilot.send(client, 'B')
                elif keyboard.is_pressed('a'):
                    await pilot.send(client, 'L')
                elif keyboard.is_pressed('d'):
                    await pilot.send(client, 'R')
                else:
                    # If no keys are held, tell the robot to stop
                    await pilot.send(client, 'S')

                if keyboard.is_pressed('esc'):
                    await pilot.send(client, 'S')
                    print("Exiting...")
                    break

                # High-frequency check (50ms) for smooth driving
                await asyncio.sleep(0.05)

    except Exception as e:
        print(f"Bluetooth Error: {e}")

if __name__ == "__main__":
    # Ensure address is filled in
    if "YOUR_DEVICE" in ROBOT_ADDRESS:
        print("STOP: Please enter your robot's MAC address in the script!")
    else:
        asyncio.run(main())
