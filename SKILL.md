---
name: eufy-robovac
description: Control Eufy RoboVac robot vacuum cleaners. Use when the user wants to start cleaning, stop/pause vacuum, return to dock, check status/battery, locate the vacuum, or manage cleaning modes for Eufy robot vacuums. Supports local network control via aioeufyclean library.
---

# Eufy RoboVac Control

Control Eufy robot vacuum cleaners over the local network.

## Quick Start

### Prerequisites

1. Install required Python package:
```bash
pip install aioeufyclean
```

2. Find your vacuum's device ID and local key:
   - Use the Eufy Clean app to find device info, OR
   - Use the device discovery script: `python scripts/discover.py`

### Basic Usage

```python
import asyncio
from aioeufyclean import Device

async def control_vacuum():
    device = Device(
        ip_address="192.168.1.100",
        device_id="your-device-id",
        local_key="your-local-key"
    )
    await device.connect()
    
    # Start cleaning
    await device.start()
    
    # Get status
    status = await device.get_status()
    print(f"Battery: {status.battery}%")
    
    # Return to dock
    await device.return_to_dock()
    
    await device.disconnect()

asyncio.run(control_vacuum())
```

## Available Commands

| Command | Description |
|---------|-------------|
| `start()` | Start cleaning |
| `stop()` | Stop/pause cleaning |
| `return_to_dock()` | Return to charging dock |
| `locate()` | Play sound to find vacuum |
| `get_status()` | Get current status, battery, mode |

## Supported Models

- Eufy Clean X8
- Eufy RoboVac series (T2118, T2123, etc.)
- Most Eufy WiFi-enabled robot vacuums

See [references/supported-models.md](references/supported-models.md) for complete list.

## Device Discovery

To find devices on your network:

```bash
python scripts/discover.py
```

## Finding Credentials

To get device_id and local_key:

1. **Using Eufy App (Easiest):**
   - Open Eufy Clean app → Device Settings → About
   - Note: Some app versions may not show local key

2. **Using Script:**
   ```bash
   python scripts/get_credentials.py --username your@email.com --password yourpassword
   ```

3. **Manual Method:**
   See [references/credentials.md](references/credentials.md) for alternative methods.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection refused | Ensure vacuum is on same network |
| Authentication failed | Verify device_id and local_key |
| Commands not working | Check if vacuum supports the command |
| Device not found | Run discovery script to verify IP |

## API Reference

See [references/api.md](references/api.md) for complete API documentation.
