import logging
import sys

# Basic logger
log = logging.getLogger('sensor_monitor')
log.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
log.addHandler(ch)


pin = {
    "doorSwitch": 2,
    "corridorDHT": 4
}
