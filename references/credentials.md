# Finding Eufy RoboVac Credentials

To control your Eufy RoboVac, you need three pieces of information:
1. **IP Address** - Local network address of the vacuum
2. **Device ID** - Unique identifier for your device
3. **Local Key** - Authentication key for local control

## Method 1: Environment Variables

Set these environment variables:

```bash
export EUFY_IP="192.168.1.100"
export EUFY_DEVICE_ID="your-device-id"
export EUFY_LOCAL_KEY="your-local-key"
```

## Method 2: Config File

Create `~/.eufy-robovac.json`:

```json
{
  "ip": "192.168.1.100",
  "device_id": "your-device-id",
  "local_key": "your-local-key"
}
```

Or use the more formal location:

```bash
mkdir -p ~/.config/eufy-robovac
cat > ~/.config/eufy-robovac/config.json << 'EOF'
{
  "ip": "192.168.1.100",
  "device_id": "your-device-id",
  "local_key": "your-local-key"
}
EOF
```

## Method 3: Finding Device Information

### Finding IP Address

**Router Admin Panel:**
- Log into your router (usually 192.168.1.1 or 192.168.0.1)
- Look for connected devices
- Find device named "Eufy" or "RoboVac"
- Note the IP address

**Command Line:**
```bash
# Scan network for Eufy devices
nmap -p 6668 192.168.1.0/24

# Or use the discovery script
python scripts/discover.py
```

**Mobile App:**
- Eufy Clean app → Device Settings → WiFi Settings
- May show IP address (varies by app version)

### Finding Device ID and Local Key

**Option A: Eufy Clean App (Limited)**
- Some app versions show device info in Settings → About
- Local key may not be visible in newer app versions

**Option B: Network Sniffing (Advanced)**
Capture device pairing process using:
- Wireshark
- tcpdump
- mitmproxy

Look for Tuya protocol traffic on port 6668.

**Option C: Third-Party Tools**

Several community tools can extract credentials:

1. **tuya-convert** (for older firmware)
2. **Tuya CLI**
3. **tinytuya** Python library

Example using tinytuya:
```bash
pip install tinytuya
python -m tinytuya scan
```

## Security Notes

- Local key is sensitive - treat it like a password
- Never commit credentials to version control
- Use environment variables or secure config files
- Local key may change if you re-pair the device

## Troubleshooting Credentials

| Issue | Solution |
|-------|----------|
| "Authentication failed" | Verify device_id and local_key match |
| "Connection refused" | Check IP address, ensure vacuum is online |
| Key stopped working | May need to re-extract after firmware update |
| Can't find local key | Try alternative methods above |
