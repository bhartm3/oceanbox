from typing import Tuple

import pygame
from pygame._sdl2 import get_audio_device_names
pygame.mixer.init()  # Initialize the mixer, this will allow the next command to work

# init_subsystem(INIT_AUDIO)
names = get_audio_device_names(True)
print(names)

pygame.mixer.quit()  # Quit the mixer as it's initialized on your main playback device
