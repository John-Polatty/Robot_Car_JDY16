import asyncio
from bleak import BleakScanner, BleakClient

# The JDY-16 Serial Characteristic UUID
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def main():
    print("Searching for JDY-16...")
    devices = await BleakScanner.discover()
    target_address = None

    for d in devices:
        if d.name and "JDY-16" in d.name:
            print(f"Found {d.name} at {d.address}")
            target_address = d.address
            break

    if not target_address:
        print("JDY-16 not found. Make sure it's blinking!")
        return

    async with BleakClient(target_address) as client:
        print(f"Connected to {target_address}")

        # Callback function to handle incoming data from the Arduino
        def notification_handler(sender, data):
            print(f"From Arduino: {data.decode('utf-8', errors='ignore')}")

        # Start listening for data
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        print("You can now type messages to send. Type 'exit' to quit.")

        while True:
            # Get user input to send to the Arduino
            msg = await asyncio.to_thread(input, "To Arduino: ")
            if msg.lower() == 'exit':
                break
            
            # Send the message as bytes
            await client.write_gatt_char(CHARACTERISTIC_UUID, msg.encode('utf-8'))

if __name__ == "__main__":
    asyncio.run(main())