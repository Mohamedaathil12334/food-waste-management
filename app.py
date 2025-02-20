from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to the JSON file storing food waste data
DATA_FILE = os.path.join('data', 'waste_data.json')

# Load existing data or initialize an empty list
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        food_waste_data = json.load(file)
else:
    food_waste_data = []

@app.route('/')
def index():
    return render_template('index.html', data=food_waste_data)

@app.route('/add', methods=['POST'])
def add_waste():
    # Get data from the form
    food_item = request.form.get('food_item')
    quantity = request.form.get('quantity')
    date = request.form.get('date')

    # Add new entry to the data
    new_entry = {
        'food_item': food_item,
        'quantity': quantity,
        'date': date
    }
    food_waste_data.append(new_entry)

    # Save updated data to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(food_waste_data, file, indent=4)

    return redirect(url_for('index'))

@app.route('/data')
def get_data():
    return jsonify(food_waste_data)

if __name__ == '__main__':
    app.run(debug=True)