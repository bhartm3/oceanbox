import pygame
import RPi.GPIO as GPIO
import time

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

SOUND_FILE = "/home/pi/sound.wav"
pygame.mixer.music.load(SOUND_FILE)

INACTIVITY_SECONDS_STOP_SOUND = 20

print("Starting oceanbox (CTRL+C to exit)")
time.sleep(2)
print("Ready")

last_motion = time.time()


def motion_detected() -> bool:
    return GPIO.input(PIR_PIN)


def play_sound():
    print("playing music")
    pygame.mixer.music.play()


def stop_sound():
    print("stop music")
    pygame.mixer.music.fadeout()


while True:
    if int(time.time()) - last_motion > INACTIVITY_SECONDS_STOP_SOUND:
        stop_sound()

    if motion_detected():
        print("Motion Detected at time: {}".format(int(time.time())))
        if not pygame.mixer.music.get_busy():
            play_sound()
            last_motion = int(time.time())
    time.sleep(1)
