#include <wiringPi.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main() {
  if (wiringPiSetupGpio () == -1)
    exit (1) ;

  pinMode(4, OUTPUT);

  while(1) {
    digitalWrite(4, 0);
    digitalWrite(4, 1);
  }

  return 0 ;
}
