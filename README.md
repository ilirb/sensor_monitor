# sensor_monitor

## Setup Raspberry Pi

```
sudo apt-get update
sudo apt-get install -y supervisor authbind python3 python3-pip python3-venv
```

## gunicorn

```
sudo touch /etc/authbind/byport/80
sudo chmod 500 /etc/authbind/byport/80
sudo chown USER /etc/authbind/byport/80
```

```
authbind gunicorn --bind 0.0.0.0:80 run:app
```
