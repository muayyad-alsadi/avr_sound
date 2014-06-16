#include <avr_sound.h>
#include "hello_ar.h"

void setup() {
  avr_sound_init();
}

// the loop routine runs over and over again forever:
void loop() {
 play_hello_ar();
 delay(500); 
}
