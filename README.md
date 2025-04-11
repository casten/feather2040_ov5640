# feather2040_ov5640
Port of camera picowbell to support rp2040 feather.


# Current Issues

On capture, None is returned

# Connections

## Feather 2040 <-> Picowbell

### Power
___
	USB (+) - VB (VBUS)
	3.3V    - 3V (NOT VS!!!)
	GND     - GND

### MicroSD - SPI
___
	MISO (GPIO20) - MISO (GP16)
	SCK  (GPIO18) - SCK (GP18)
	MOSI (GPIO19) - MO (MOSI/GP19)
	A1   (GPIO27) - CS (GP17)

### Camera - I2C
___
	SDA (SDA/GPIO2) - SDA (GPIO4)
	SCL (SCL/GPIO3) - SCL (GPIO5)

### Camera - Sync, Status, etc.
___
	TX  (GPIO0)  - GP0 (VSYNC)
	A0  (GPIO26) - GP2 (HREF)
	A2  (GPIO28) - GP3 (PCLK)
	A3  (GPIO29) - GP1 (PDWN)
	D24 (GPIO24) - RESET (GP14)

### Camera Data
___
	D4  (GPIO6)    - DATA2 (GP6)
	D5  (GPIO7)    - DATA3 (GP7)
	D6  (GPIO8)    - DATA4 (GP8)
	D9  (GPIO9)    - DATA5 (GP9)
	D10  (GPIO10)  - DATA6 (GP10)
	D11  (GPIO11)  - DATA7 (GP11)
	D12  (GPIO12)  - DATA8 (GP12)
	D13  (GPIO13)  - DATA9 (GP13)

# References
- RP2040 Feather Pinout - https://learn.adafruit.com/adafruit-feather-rp2040-pico/pinouts
- Camera Picowbell Pinout - https://learn.adafruit.com/adafruit-picowbell-camera-breakout?view=all
- RPi Pico Pinout - https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html
- Picowbell Info - https://learn.adafruit.com/adafruit-picowbell-camera-breakout?view=all
- Capture Example - https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/PiCowbell_Camera_Demos/JPEG_Capture/code.py
