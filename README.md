# sensor_monitor

Simple Flask app to run on Raspberry and display different sensors

- [sensor_monitor](#sensor_monitor)
  - [Hardware](#hardware)
  - [Using Docker](#using-docker)
    - [Prepare](#prepare)
    - [Run sensor_monitor](#run-sensor_monitor)
    - [Run without docker-compose](#run-without-docker-compose)
  - [Running without docker](#running-without-docker)
    - [Prepare environment](#prepare-environment)
    - [Setup gunicorn](#setup-gunicorn)
    - [Supervisor](#supervisor)
    - [Run manually without supervisor](#run-manually-without-supervisor)
  - [Configuration](#configuration)
  - [TODO](#todo)

## Hardware

- Raspberry Pi
- [Microswitch](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200725121427&SearchText=microswitch)
- [DHT22 Temperature and Humidity sensor](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200725121509&SearchText=dht22)


## Using Docker

### Prepare

``` bash
sudo apt-get update && sudo apt-get upgrade -y

# Required for docker-compose and git
sudo apt-get install -y git python3-pip

# Install docker
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi

# Install docker-compose
sudo pip3 install docker-compose
```

### Run sensor_monitor

``` bash
git clone https://github.com/ilirb/sensor_monitor.git
cd sensor_monitor

docker-compose up

# to run in background and start on boot
docker-compose up -d

# to update
docker-compose pull && docker-compose up -d

# to stop and remove
docker-compose stop
docker-compose down
```

### Run without docker-compose

``` bash
docker run -p 5000:5000 --privileged ilirb/sensor-monitor:latest
```

## Running without docker

### Prepare environment

``` bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y git supervisor authbind python3 python3-pip python3-venv
git clone https://github.com/ilirb/sensor_monitor
cd sensor_monitor

# On non Rasbperry Pi machine (dev)
pip3 install -r requirements.txt

# On Raspberry Pi
pip3 install -r requirements.txt -r requirements-RPi.txt
```

### Setup gunicorn

This is required to allow listening on port 80 without sudo

``` bash
sudo touch /etc/authbind/byport/80
sudo chmod 500 /etc/authbind/byport/80
sudo chown pi /etc/authbind/byport/80
```

### Supervisor

This makes sensor_monitor run as a service and on boot

``` bash
sudo ln -s $PWD/sensor_monitor.conf /etc/supervisor/conf.d/sensor_monitor.conf
sudo supervisorctl reread
sudo service supervisor restart
```

### Run manually without supervisor

``` bash
authbind gunicorn --bind 0.0.0.0:80 run:app
```

## Configuration

Edit `application/config.py` and adjust pins to sensors/devices connected to Raspberry Pi GPIO

Sensor logic resides in `application/devices.py`

## TODO

- Add multiplatform docker builds (armv7,armv8,arm64)
- Notifications
- Alerts (IFTTT like)
- InfluxDB
- Web authentication
- Web configuration (Sensors, notifications, etc)
