                                                                                                                                                                            import math
print(math.pi)

from machine import Pin, PWM
from time import sleep

# Define the GPIO pins for motor control
left_motor_forward = PWM(Pin(8))
left_motor_backward = PWM(Pin(9))
right_motor_forward = PWM(Pin(10))
right_motor_backward = PWM(Pin(11))

# Set the PWM frequency
left_motor_forward.freq(1000)
left_motor_backward.freq(1000)
right_motor_forward.freq(1000)
right_motor_backward.freq(1000)

def move_forward(duration):
    print("Moving forward")
    left_motor_forward.duty_u16(32768)  # 50% duty cycle
    right_motor_forward.duty_u16(32768) # 50% duty cycle
    sleep(duration)
    stop_motors()

def move_backward(duration):
    print("Moving backward")
    left_motor_backward.duty_u16(32768)  # 50% duty cycle
    right_motor_backward.duty_u16(32768) # 50% duty cycle
    sleep(duration)
    stop_motors()

def turn_left(duration):
    print("Turning left")
    left_motor_backward.duty_u16(32768)  # 50% duty cycle
    right_motor_forward.duty_u16(32768)  # 50% duty cycle
    sleep(duration)
    stop_motors()

def turn_right(duration):
    print("Turning right")
    left_motor_forward.duty_u16(32768)  # 50% duty cycle
    right_motor_backward.duty_u16(32768) # 50% duty cycle
    sleep(duration)
    stop_motors()

def stop_motors():
    left_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(0)
    right_motor_forward.duty_u16(0)
    right_motor_backward.duty_u16(0)

def main():
    # Example movements
    move_forward(2)
    turn_left(1)
    move_forward(2)
    turn_right(1)
    move_backward(2)

if __name__ == "__main__":
    main()
# Write your code here :-)
