#include <avr_sound.h>
#include "welcome.h"

void setup() {
  avr_sound_init();
}

// the loop routine runs over and over again forever:
void loop() {
 play_welcome();
 delay(500); 
}
