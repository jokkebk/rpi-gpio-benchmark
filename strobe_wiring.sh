#!/bin/sh

# wiringPi provides a "gpio" command, let's use that

gpio -g mode 4 out

gpio -g pwm 4 512 # 50 % duty cycle
# while true
# do
	# gpio -g write 4 1
	# gpio -g write 4 0
# done
