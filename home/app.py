import json

from flask import Flask, Response, render_template, stream_with_context

import devices.devices as devices

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/api/entrance')
def entrance_door():
    def generate():
        json_data = json.dumps(devices.get_entrance_door(), default=str)
        yield f"retry: 2000\ndata:{json_data}\n\n"
    return Response(stream_with_context(generate()), mimetype='text/event-stream')


@app.route('/api/entrancetemp')
def entrance_temp():
    def generate():
        json_data = json.dumps(devices.get_temp_sensor(), default=str)
        yield f"retry: 10000\ndata:{json_data}\n\n"
    return Response(stream_with_context(generate()), mimetype='text/event-stream')
