import os
import sys
import logging

# Constants
PUSHBULLET_URI="https://api.pushbullet.com/v2"


# Basic logger
log = logging.getLogger('sensor_monitor')
log.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
log.addHandler(ch)

# GPIO Devices
pin = {
    "doorSwitch": 2,
    "corridorDHT": 4
}
