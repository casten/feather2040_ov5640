# SPDX-FileCopyrightText: Copyright (c) 2023 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
This demo is designed for the Raspberry Pi Pico and Camera PiCowbell

It take an image when the shutter button is pressed and saves it to
the microSD card.
"""

import os
import time
import busio
import board
import digitalio
import adafruit_ov5640
import keypad
import sdcardio
import storage

sd_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
sd_cs = board.A1
sdcard = sdcardio.SDCard(sd_spi, sd_cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

print("construct bus")
i2c = busio.I2C(board.SCL, board.SDA)

print("setup reset pin")
#reset = digitalio.DigitalInOut(board.D24)

print("construct camera")
try:
    cam = adafruit_ov5640.OV5640(
        i2c,
        data_pins=(
            board.D4,
            board.D5,
            board.D6,
            board.D9,
            board.D10,
            board.D11,
            board.D12,
            board.D13,
        ),
        vsync=board.TX,
        href=board.RX,
#        reset=reset,
        clock=board.A2,
        shutdown=None,
        mclk=None,
        size=adafruit_ov5640.OV5640_SIZE_VGA,
    )
except Exception as e:
    print(f"exception {e}")

print("print chip id")
print(cam.chip_id)

# keys = keypad.Keys((board.GP4), value_when_pressed=False, pull=True)
keys = keypad.Keys((board.BUTTON,), value_when_pressed=False, pull=True)

def exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError as _:
        return False

_image_counter = 0

def open_next_image():
    global _image_counter  # pylint: disable=global-statement
    while True:
        filename = f"/sd/img{_image_counter:04d}.jpg"
        _image_counter += 1
        if exists(filename):
            continue
        print("# writing to", filename)
        return open(filename, "wb")

cam.colorspace = adafruit_ov5640.OV5640_COLOR_JPEG
cam.quality = 5
b = bytearray(cam.capture_buffer_size)
jpeg = cam.capture(b)
if jpeg == None:
    print("capture failed :(")

while True:
    shutter = keys.events.get()
    # event will be None if nothing has happened.
    if shutter:
        if shutter.pressed:
            time.sleep(0.01)
            jpeg = cam.capture(b)
            print(f"Captured {len(jpeg)} bytes of jpeg data")
            print(f" (had allocated {cam.capture_buffer_size} bytes")
            print(f"Resolution {cam.width}x{cam.height}")
            try:
                with open_next_image() as f:
                    f.write(jpeg)
                print("# Wrote image")
            except OSError as e:
                print(e)

