from gpiozero import Button
from config import log, pin


def get_entrance_door():
    try:
        button = Button(pin["doorSwitch"])
        status = button.is_pressed
    except Exception as e:
        log.error(e)
        status = "error"
    return {"name": "Entrance door", "status": status}

def get_temp_sensor():
    try:
        status = "Not Implemented"
    except Exception as e:
        log.error(e)
        status = "error"
    return {"name": "Entrance temperature", "status": status}
