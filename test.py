from typing import Tuple

import pygame
import pygame._sdl2.audio
pygame.mixer.init()  # Initialize the mixer, this will allow the next command to work

# init_subsystem(INIT_AUDIO)
names = get_audio_device_names()
print(names)

pygame.mixer.quit()  # Quit the mixer as it's initialized on your main playback device
