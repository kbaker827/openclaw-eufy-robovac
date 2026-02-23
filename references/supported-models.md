# Supported Eufy RoboVac Models

This skill uses the `aioeufyclean` library for local network control of Eufy robot vacuums.

## Confirmed Working Models

| Model | Series | Notes |
|-------|--------|-------|
| X8 | Clean X | Full support |
| X8 Pro | Clean X | Full support |
| G30 | Clean G | Full support |
| G30 Edge | Clean G | Full support |
| G30 Hybrid | Clean G | Full support |

## Likely Compatible Models

These models use similar communication protocols and should work:

- RoboVac 11S
- RoboVac 15C
- RoboVac 25C
- RoboVac 30
- RoboVac 30C
- RoboVac 35C
- RoboVac 11S MAX
- RoboVac 15C MAX
- RoboVac 30C MAX
- RoboVac G10 Hybrid
- RoboVac G20
- RoboVac G20 Hybrid
- RoboVac G30
- RoboVac G30 Verge
- RoboVac G30 Hybrid
- RoboVac X8
- RoboVac X8 Hybrid

## Requirements

- Vacuum must have WiFi capability
- Must be connected to local network
- Device must not be in pairing mode

## Not Supported

- Bluetooth-only models
- Models without local API (cloud-only)
- Very old RoboVac models (pre-2018)

## Testing New Models

If you test a model not listed here:

1. Run the discovery script: `python scripts/discover.py`
2. Try basic commands: start, stop, dock, status
3. Report results to the project

## Model Codes Reference

| Code | Model Name |
|------|------------|
| T2118 | RoboVac 11S |
| T2120 | RoboVac 30 |
| T2123 | RoboVac 15C |
| T2128 | RoboVac 35C |
| T2150 | RoboVac G30 |
| T2250 | RoboVac X8 |
