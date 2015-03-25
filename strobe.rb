require 'wiringpi'

io = WiringPi::GPIO.new

while true do
	io.write(7,0)
	io.write(7,1)
end
