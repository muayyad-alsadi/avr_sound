#include <avr_sound.h>
#include "emad.h"

void setup() {
  avr_sound_init();
}

// the loop routine runs over and over again forever:
void loop() {
 play_emad();
 delay(500); 
}
