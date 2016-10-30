#!/usr/bin/python

"""Clock Example

   This example creates a digital clock that displays the current time
   on the 4 char, 7 segment display.
"""
from datetime import datetime
from time import sleep

from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
display.begin()

# Output 'exit' instruction to console
print("Press CTRL+Z to exit the example.")

# Update continually the time on a 4 char, 7-segment display
while True:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    display.clear()
    # Set hours
    display.set_digit(0, int(hour / 10))     # Tens
    display.set_digit(1, hour % 10)          # Ones
    # Set minutes
    display.set_digit(2, int(minute / 10))   # Tens
    display.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    display.set_colon(second % 2)            # Toggle colon at 1Hz

    # Write the display buffer to the actual hardware display LEDs.
    display.write_display()

    # Wait a quarter second (use less than 1 second to prevent colon blinking)
    sleep(0.25)

