import board
import busio
import time

uart = busio.UART(board.GP0, board.GP1, baudrate=9600) # Initialize UART with TX pin GP0 and RX pin GP1

while True:
    if uart.in_waiting > 0:
        data = uart.readline().decode('utf-8').strip() # Read data from UART
        print("Received:", data)
    time.sleep(1) # Wait for 1 second
