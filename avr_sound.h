#ifndef AVR_SOUND_H
#define AVR_SOUND_H

#include <avr/pgmspace.h>
#include <stdlib.h>

#define AVR_SOUND_BUFFER_LEN 256

void avr_sound_init();
void avr_sound_play(unsigned char const*flash_ptr, size_t n);
void avr_sound_play_buffer(size_t n);
inline void avr_sound_out(unsigned char v);

#endif
