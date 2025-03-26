from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_power(hydrogen_mass):
    if hydrogen_mass < 0:
        raise ValueError("Hydrogen mass cannot be negative.")
    return round(hydrogen_mass / 30, 2)  # Convert grams to kW

@app.route('/calculate_power', methods=['POST'])
def calculate_power_route():
    data = request.get_json()
    hydrogen_mass = data.get('hydrogen')
    power = calculate_power(hydrogen_mass)
    return jsonify({'power': power})

if __name__ == '__main__':
    app.run(debug=True)
