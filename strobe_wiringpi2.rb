require 'wiringpi2'

io = WiringPi::GPIO.new

while true do
	io.digital_write(7,0)
	io.digital_write(7,1)
end
