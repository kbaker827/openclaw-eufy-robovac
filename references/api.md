# Eufy RoboVac API Reference

Complete reference for the `aioeufyclean` library API.

## Device Class

```python
from aioeufyclean import Device

device = Device(
    ip_address="192.168.1.100",
    device_id="your-device-id",
    local_key="your-local-key"
)
```

### Connection Methods

| Method | Description |
|--------|-------------|
| `async connect()` | Establish connection to device |
| `async disconnect()` | Close connection |
| `async is_connected()` | Check if connected |

### Control Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `async start()` | Start cleaning | None |
| `async stop()` | Stop/pause cleaning | None |
| `async return_to_dock()` | Return to charging dock | None |
| `async locate()` | Play locate sound | None |
| `async get_status()` | Get device status | Status object |

### Status Object

The `get_status()` method returns a status object with these attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `battery` | int | Battery percentage (0-100) |
| `state` | str | Current state (cleaning, docked, etc.) |
| `cleaning_mode` | str | Active cleaning mode |
| `error_code` | int or None | Error code if error present |

### Example Usage

```python
import asyncio
from aioeufyclean import Device

async def main():
    device = Device(
        ip_address="192.168.1.100",
        device_id="...",
        local_key="..."
    )
    
    await device.connect()
    
    # Get status
    status = await device.get_status()
    print(f"Battery: {status.battery}%")
    print(f"State: {status.state}")
    
    # Control vacuum
    if status.state == "docked":
        await device.start()
    elif status.state == "cleaning":
        await device.return_to_dock()
    
    await device.disconnect()

asyncio.run(main())
```

## Discovery Class

```python
from aioeufyclean import Discovery

# Discover devices on network
devices = await Discovery.discover()

for device in devices:
    print(f"Found: {device.name} at {device.ip_address}")
```

### Discovery Response

The `discover()` method returns a list of device info objects:

| Attribute | Type | Description |
|-----------|------|-------------|
| `ip_address` | str | Device IP address |
| `device_id` | str | Device identifier |
| `model` | str | Model number |
| `name` | str | Device name (if available) |

## Error Handling

Common exceptions:

```python
from aioeufyclean import Device
from aioeufyclean.exceptions import ConnectionError, AuthenticationError

try:
    device = Device(...)
    await device.connect()
except ConnectionError:
    print("Failed to connect - check IP address")
except AuthenticationError:
    print("Authentication failed - check credentials")
```

## States

Possible vacuum states:

| State | Description |
|-------|-------------|
| `docked` | At charging station |
| `cleaning` | Currently cleaning |
| `paused` | Cleaning paused |
| `returning` | Returning to dock |
| `error` | Error state |

## Cleaning Modes

Available cleaning modes (varies by model):

| Mode | Description |
|------|-------------|
| `auto` | Automatic cleaning |
| `spot` | Spot cleaning |
| `edge` | Edge cleaning |
| `single_room` | Single room mode |
