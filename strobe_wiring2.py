import wiringpi2

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(7,io.OUTPUT)

while True:
	io.digitalWrite(7,io.HIGH)
	io.digitalWrite(7,io.LOW)
