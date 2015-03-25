import wiringpi

# wiringpi.wiringPiSetupGpio
# wiringpi.pinMode(4, wiringpi.OUTPUT) # set pin 7 as output

# while True:
	# wiringpi.digitalWrite(7, 1)
	# wiringpi.digitalWrite(7, 0)

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

io.pinMode(7,io.OUTPUT)

while True:
	io.digitalWrite(7,io.HIGH)
	io.digitalWrite(7,io.LOW)
