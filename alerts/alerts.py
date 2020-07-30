from time import sleep
from gpiozero import Button
from pushbullet import Pushbullet
from config import log

CHECK_INTERVAL=1 # Check sensors interval

pb = Pushbullet()

def alert_door_open():
    try:
        button = Button(2)
        if button.is_held(5):
            pb.push_note("SM Door", "Open")
    except Exception as e:
        log.error(e)
        pb.push_note("SM Door Error", "Cannot get status")

while True:
    alert_door_open()

    sleep(CHECK_INTERVAL)
