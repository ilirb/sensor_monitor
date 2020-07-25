# sensor_monitor

Simple Flask app to run on Raspberry and display different sensors

## Hardware

- Raspberry Pi
- [Microswitch](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200725121427&SearchText=microswitch)
- [DHT22 Temperature and Humidity sensor](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200725121509&SearchText=dht22)


## Setup

```
sudo apt-get update
sudo apt-get install -y git supervisor authbind python3 python3-pip python3-venv
git clone https://github.com/ilirb/sensor_monitor
cd sensor_monitor
pip3 install -r requirements.txt
```

### gunicorn

This is required to allow listening on port 80 without sudo

```
sudo touch /etc/authbind/byport/80
sudo chmod 500 /etc/authbind/byport/80
sudo chown pi /etc/authbind/byport/80
```

### Supervisor

```
sudo ln -s $PWD/sensor_monitor.conf /etc/supervisor/conf.d/sensor_monitor.conf
sudo supervisorctl reread
sudo service supervisor restart
```

### Run manually without supervisor

```
authbind gunicorn --bind 0.0.0.0:80 run:app
```

## TODO

- Docker images/stacks
- Notifications
- InfluxDB
- Web authentication
- Web configuration (Sensors, notifications, etc)
