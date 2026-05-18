from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "moisture": None,
    "alert": "No data yet",
    "pump": "OFF"
}

@app.route('/update')
def update():
    value = request.args.get('value')

    if value is None:
        return "Missing value", 400

    value = float(value)

    data["moisture"] = value

    if value < 20:
        data["alert"] = "Water your plant!"
        data["pump"] = "ON"
    else:
        data["alert"] = "Soil is healthy"
        data["pump"] = "OFF"

    return "OK"

@app.route('/status')
def status():
    return jsonify(data)

@app.route('/')
def home():
    return f"""
    <html meta http-equiv="refresh" content="5">
        </head>
        <body>
    <h1>Plant Dashboard</h1>
    <p>Moisture: {data['moisture']}</p>
    <p>Alert: {data['alert']}</p>
    <p>Pump Status: {data['pump']}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)