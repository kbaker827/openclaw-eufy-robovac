#!/usr/bin/env python3
"""
Control Eufy RoboVac from command line.
"""

import argparse
import asyncio
import json
import sys
import os

try:
    from aioeufyclean import Device
except ImportError:
    print("Error: aioeufyclean not installed. Run: pip install aioeufyclean")
    sys.exit(1)


class VacuumController:
    """CLI controller for Eufy RoboVac."""
    
    def __init__(self, ip_address, device_id, local_key):
        self.device = Device(
            ip_address=ip_address,
            device_id=device_id,
            local_key=local_key
        )
    
    async def connect(self):
        """Connect to the device."""
        await self.device.connect()
    
    async def disconnect(self):
        """Disconnect from the device."""
        await self.device.disconnect()
    
    async def get_status(self):
        """Get device status."""
        status = await self.device.get_status()
        return {
            "battery": getattr(status, "battery", "unknown"),
            "state": getattr(status, "state", "unknown"),
            "cleaning_mode": getattr(status, "cleaning_mode", "unknown"),
            "error_code": getattr(status, "error_code", None),
        }
    
    async def start(self):
        """Start cleaning."""
        await self.device.start()
        return "Cleaning started"
    
    async def stop(self):
        """Stop/pause cleaning."""
        await self.device.stop()
        return "Cleaning stopped"
    
    async def return_to_dock(self):
        """Return to dock."""
        await self.device.return_to_dock()
        return "Returning to dock"
    
    async def locate(self):
        """Play locate sound."""
        await self.device.locate()
        return "Playing locate sound"


def load_config():
    """Load configuration from environment or config file."""
    config = {}
    
    # Try environment variables first
    config["ip"] = os.environ.get("EUFY_IP")
    config["device_id"] = os.environ.get("EUFY_DEVICE_ID")
    config["local_key"] = os.environ.get("EUFY_LOCAL_KEY")
    
    # Try config file
    config_paths = [
        os.path.expanduser("~/.config/eufy-robovac/config.json"),
        os.path.expanduser("~/.eufy-robovac.json"),
        "./eufy-robovac.json",
    ]
    
    for path in config_paths:
        if os.path.exists(path):
            try:
                with open(path) as f:
                    file_config = json.load(f)
                    config["ip"] = config["ip"] or file_config.get("ip")
                    config["device_id"] = config["device_id"] or file_config.get("device_id")
                    config["local_key"] = config["local_key"] or file_config.get("local_key")
            except (json.JSONDecodeError, IOError):
                pass
    
    return config


async def main():
    parser = argparse.ArgumentParser(description="Control Eufy RoboVac")
    parser.add_argument("--ip", help="Device IP address")
    parser.add_argument("--device-id", help="Device ID")
    parser.add_argument("--local-key", help="Local key")
    parser.add_argument("command", choices=["start", "stop", "dock", "status", "locate"],
                       help="Command to execute")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    # Load config
    config = load_config()
    
    ip = args.ip or config.get("ip")
    device_id = args.device_id or config.get("device_id")
    local_key = args.local_key or config.get("local_key")
    
    if not all([ip, device_id, local_key]):
        print("Error: Missing required credentials.")
        print("\nProvide via:")
        print("  --ip, --device-id, --local-key arguments")
        print("  EUFY_IP, EUFY_DEVICE_ID, EUFY_LOCAL_KEY environment variables")
        print("  ~/.config/eufy-robovac/config.json or ~/.eufy-robovac.json")
        print("\nConfig file format:")
        print(json.dumps({"ip": "192.168.1.100", "device_id": "...", "local_key": "..."}, indent=2))
        sys.exit(1)
    
    controller = VacuumController(ip, device_id, local_key)
    
    try:
        await controller.connect()
        
        if args.command == "status":
            result = await controller.get_status()
        elif args.command == "start":
            result = await controller.start()
        elif args.command == "stop":
            result = await controller.stop()
        elif args.command == "dock":
            result = await controller.return_to_dock()
        elif args.command == "locate":
            result = await controller.locate()
        
        if args.json:
            print(json.dumps(result if isinstance(result, dict) else {"message": result}))
        else:
            if isinstance(result, dict):
                for key, value in result.items():
                    print(f"{key}: {value}")
            else:
                print(result)
                
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        await controller.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
