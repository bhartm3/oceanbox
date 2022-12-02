import pygame

mixer.init() # Initialize the mixer, this will allow the next command to work
print(sdl2.audio.get_audio_device_names(False)) # Returns playback devices, Boolean value determines whether they are Input or Output devices.
mixer.quit() # Quit the mixer as it's initialized on your main playback device