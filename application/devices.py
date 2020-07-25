from gpiozero import Button
from application.config import log, pin


def get_entrance_door():
    try:
        button = Button(pin["doorSwitch"])
        status = button.is_pressed
    except Exception as e:
        log.error(e)
        status = "error"
    return {"name": "Entrance door", "status": status}


def get_temp_sensor():
    data = "Error"
    try:
        import Adafruit_DHT
        sensor = Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin['corridorDHT'])

        if humidity is not None and temperature is not None:
            t = ("%.1f" % temperature)
            h = ("%.1f" % humidity)
            data = f"Temperature {t}, Humidity {h}"

    except Exception as e:
        log.error(e)

    return {"name": "Entrance temperature", "status": data}
