import pygame
import RPi.GPIO as GPIO
import time

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

SOUND_FILE = "/home/pi/waves.mp3"
pygame.mixer.music.load(SOUND_FILE)

INACTIVITY_SECONDS_STOP_SOUND = 60

print("Starting oceanbox (CTRL+C to exit)")
time.sleep(2)
print("Ready")

last_motion = time.time() - 1000
hot = 0


def motion_detected() -> bool:
    return GPIO.input(PIR_PIN)


def play_sound():
    print("playing music")
    pygame.mixer.music.play()


def stop_sound():
    print("stop music")
    pygame.mixer.music.stop()


while True:
    if int(time.time()) - last_motion > INACTIVITY_SECONDS_STOP_SOUND and pygame.mixer.music.get_busy():
        stop_sound()

    if motion_detected():
        print("Motion Detected at time: {}".format(int(time.time())))
        prev_motion = last_motion
        last_motion = time.time()
        if prev_motion - last_motion < 12:
            if not pygame.mixer.music.get_busy():
                last_motion = int(time.time())
                hot = 0
                play_sound()

    time.sleep(1)
