# sensor_monitor

## Setup Raspberry Pi

```
sudo apt-get update
sudo apt-get install -y supervisor authbind python3 python3-pip python3-venv
```

### gunicorn

```
sudo touch /etc/authbind/byport/80
sudo chmod 500 /etc/authbind/byport/80
sudo chown USER /etc/authbind/byport/80
```

Run manually

```
authbind gunicorn --bind 0.0.0.0:80 run:app
```

### Supervisor

```
sudo ln -s /home/pi/sensor_monitor/sensor_monitor.conf /etc/supervisor/conf.d/sensor_monitor.conf
sudo supervisorctl reread
sudo service supervisor restart
```
