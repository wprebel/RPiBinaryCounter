#!/usr/bin/python

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#ControlPin = [26,19,13,6,5]
ControlPin = [5,6,13,19,26]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


seq =   [   [0,0,0,0,1],
            [0,0,0,1,0],
            [0,0,0,1,1],
            [0,0,1,0,0],
            [0,0,1,0,1],
            [0,0,1,1,0],
            [0,0,1,1,1],
            [0,1,0,0,0],
            [0,1,0,0,1],
            [0,1,0,1,0],
            [0,1,0,1,1],
            [0,1,1,0,0],
            [0,1,1,0,1],
            [0,1,1,1,0],
            [0,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,1],
            [1,0,0,1,0],
            [1,0,0,1,1],
            [1,0,1,0,0],
            [1,0,1,0,1],
            [1,0,1,1,0],
            [1,0,1,1,1],
            [1,1,0,0,0],
            [1,1,0,0,1],
            [1,1,0,1,0],
            [1,1,0,1,1],
            [1,1,1,0,0],
            [1,1,1,0,1],
            [1,1,1,1,0],
            [1,1,1,1,1]]

count = 0


try:
    while True:

        for i in range(31):
            for step in range(31):
		print step + 1, seq[step]
                for pin in range(5):
		
			GPIO.output(ControlPin[pin], seq[step][pin])
		time.sleep(1)


except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    #print "\n", counter # print value of counter

    #except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
        #print "Other error or exception occurred!"

#finally:
        GPIO.cleanup()
