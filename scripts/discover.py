#!/usr/bin/env python3
"""
Discover Eufy RoboVac devices on the local network.
"""

import asyncio
import sys

try:
    from aioeufyclean import Discovery
except ImportError:
    print("Error: aioeufyclean not installed. Run: pip install aioeufyclean")
    sys.exit(1)


async def discover_devices():
    """Discover Eufy devices on the network."""
    print("Scanning for Eufy RoboVac devices...")
    print("(This may take up to 30 seconds)")
    print()
    
    devices = await Discovery.discover()
    
    if not devices:
        print("No devices found.")
        print("\nTroubleshooting:")
        print("- Ensure vacuum is powered on and connected to WiFi")
        print("- Ensure this computer is on the same network as the vacuum")
        print("- Try power cycling the vacuum")
        return
    
    print(f"Found {len(devices)} device(s):\n")
    
    for i, device in enumerate(devices, 1):
        print(f"Device {i}:")
        print(f"  IP Address: {device.ip_address}")
        print(f"  Device ID: {device.device_id}")
        print(f"  Model: {device.model}")
        print(f"  Name: {device.name or 'Unknown'}")
        print()


if __name__ == "__main__":
    asyncio.run(discover_devices())
