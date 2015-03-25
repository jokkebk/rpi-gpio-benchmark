# rpi-gpio-benchmark
Raspberry Pi GPIO Benchmarks

Installation of libraries
-------------------------

WiringPi (strobe_wiringpy_gpio.sh):

    git clone git://git.drogon.net/wiringPi
    cd wiringPi
    ./build

Python RPi.GPIO (strobe.py):

    sudo apt-get install python-rpi.gpio python3-rpi.gpio

Python wiringpi2 (strobe_wiring2.py):

    sudo apt-get install python-dev python-setuptools
    git clone https://github.com/Gadgetoid/WiringPi2-Python.git
    sudo python setup.py install

Ruby  (strobe_wiringpi2.rb)

    sudo apt-get install ruby-dev
    sudo gem install wiringpi2

C BCM2835 (strobe_bcm.c)

    curl -O -J -L http://www.airspayce.com/mikem/bcm2835/bcm2835-1.42.tar.gz
    tar xzf bcm2835-1.42.tar.gz
    cd bcm2835-1.42
    ./configure
    make
    sudo make install
    cd ..
    gcc strobe_bcm.c -O3 -lbcm2835 -o strobe_bcm

C WiringPi (strobe_wiring*.c)

    (install WiringPi as above)
    gcc strobe_wiring.c -lwiringPi -o strobe_wiring
    (similar commands for other 2 versions)

Perl BCM2835 (strobe.pl)

    wget http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Device-BCM2835-1.9.tar.gz
    cd Device-BCM2835
    perl Makefile.PL
    make
    sudo make install

Benchmarks themselves need to be run with sudo to access GPIO.
