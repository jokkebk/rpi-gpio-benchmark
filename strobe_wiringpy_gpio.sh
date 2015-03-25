#!/bin/sh

gpio mode 7 out

while true
do
	gpio write 7 1
	gpio write 7 0
done
