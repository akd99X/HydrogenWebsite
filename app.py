from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TASK_DATABASE = {
    "charge car": 50,
    "power home": 30,
    "run factory": 1000,
    "fly drone": 0.5,
    "launch rocket": 50000,
    "brew coffee": 0.1
}

PRODUCTION_DATA = {
    "green": {"cost": 5, "co2": 0},
    "gray": {"cost": 2, "co2": 10},
    "blue": {"cost": 3, "co2": 2}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_power', methods=['POST'])
def calculate_power():
    hydrogen_grams = float(request.json['hydrogen'])
    hydrogen_kg = hydrogen_grams / 1000
    power = hydrogen_kg * 33.3
    return jsonify({"power": round(power, 2)})

@app.route('/calculate_hydrogen', methods=['POST'])
def calculate_hydrogen():
    power = float(request.json['power'])
    hydrogen_kg = power / 33.3
    return jsonify({"hydrogen": round(hydrogen_kg, 2)})

@app.route('/convert_task', methods=['POST'])
def convert_task():
    task = request.json['task'].lower()
    quantity = 1
    words = task.split()
    for word in words:
        if word.isdigit():
            quantity = int(word)
            break
    task_keyword = ' '.join([word for word in words if not word.isdigit()])
    energy_needed = None
    for key in TASK_DATABASE:
        if key in task_keyword:
            energy_needed = TASK_DATABASE[key] * quantity
            break
    if energy_needed:
        hydrogen_needed = energy_needed / 33.3
        return jsonify({"hydrogen": round(hydrogen_needed, 2)})
    else:
        return jsonify({"error": "Task not found!"})

@app.route('/compare_methods', methods=['POST'])
def compare_methods():
    method = request.json['method'].lower()
    if method in PRODUCTION_DATA:
        return jsonify(PRODUCTION_DATA[method])
    else:
        return jsonify({"error": "Invalid method!"})

if __name__ == '__main__':
    app.run(debug=True)