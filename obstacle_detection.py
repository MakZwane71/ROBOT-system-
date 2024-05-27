# Write your code here :-)
import math
from machine import Pin, PWM
from time import sleep

# Import library for ultrasonic sensor
from hcsr04 import HCSR04

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

# Initialize ultrasonic sensor
sensor = HCSR04(trigger_pin=16, echo_pin=17)

def get_distance():
    return sensor.distance_cm()

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
    try:
        while True:
            distance = get_distance()
            print("Distance:", distance)
            if distance < 10:  # If obstacle is closer than 10cm
                stop_motors()
                if distance < 5:  # If obstacle is very close, turn sharply
                    turn_left(1) if distance <= 3 else turn_right(1)
                else:  # If obstacle is moderately close, turn gradually
                    turn_left(0.5) if distance <= 7 else turn_right(0.5)
            else:
                move_forward(0.5)
    except KeyboardInterrupt:
        stop_motors()

if __name__ == "__main__":
    main()
