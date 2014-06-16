#include "avr_sound.h"
#include "Arduino.h"

unsigned char *avr_sound_buffer;

void avr_sound_init() {
  DDRB|= (1<<PB0) | (1<<PB1); // init digital pin 8 and digital pin 9 as LSB and HSB
  avr_sound_buffer=(unsigned char *)malloc(AVR_SOUND_BUFFER_LEN);
}

void avr_sound_play(unsigned char const*flash_ptr, size_t n) {
  memcpy_P(avr_sound_buffer, flash_ptr, n);
  avr_sound_play_buffer(n);
}

void avr_sound_play_buffer(size_t n) {
  int i=0;
  unsigned char v;
  for (i=0; i<n; ++i) {
    v=avr_sound_buffer[i];
    avr_sound_out(v&3);
    v>>=2;
    avr_sound_out(v&3);
    v>>=2;
    avr_sound_out(v&3);
    v>>=2;
    avr_sound_out(v&3);
  }
  PORTB&=~3;
}

// to have 8000 Hz we need to play for 125 millis
#define avr_sound_interval 125

inline void avr_sound_out(unsigned char v) {
  PORTB^= (PORTB&3)^v;
  delayMicroseconds(125);
}
