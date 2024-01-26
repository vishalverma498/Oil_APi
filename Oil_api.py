import asyncio
import json
import random
from flask import Flask, jsonify
from flask_cors import CORS
import string
from datetime import datetime
import time

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for development purposes

# Initialize arm rotation and direction as global variables

Alarm30_data = []  # Initialize an empty list to store 30 data points

# List of random strings
random_strings = [" HIGH HIGH", " HIGH", "LOW", "LOW LOW", "TRANSMITTER FAULT"]
random_number_priority = ["0", "1", "2", "3", "4", "10"]
random_number_class = ["1", "8", "18", "17", "10", "4", "5", "6", "16"]
random_number_valve = ["Position Feedback Fault","Failed to Close"]

# Counter for cycling through lists
counter = 0

@app.route('/Alarm30', methods=['GET'])
def get_graph30_data():
    global Alarm30_data, counter
    while len(Alarm30_data) < 30:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data_point = {
            "Priority": random_number_priority[counter % len(random_number_priority)],
            "Class": random_number_class[counter % len(random_number_class)],
            "Type": 1,
            "Text3": random_strings[counter % len(random_strings)],
            "Classname": "Alarm",
            "Typename": "Alarm High",
            "ServerID": "0",
            "AlarmTag": round(random.uniform(100, 4000), 0),
            "Timestamp": timestamp,
        }
        time.sleep(0.2)
        Alarm30_data.append(new_data_point)

    data = json.dumps(Alarm30_data)
    Alarm30_data = []  # Clear the list for the next 30 data points
    # Increment counter for the next cycle
    counter += 1
    return data

@app.route('/Alarm_Water_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Fuel_Oil_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Drill_Water_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Dirty_Oil_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Potable_Water_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Fuel_Oil_Day_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Edge_Fuel_Oil_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Non_Contaminated_Drain_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Billre_Holding_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


@app.route('/Contaminated_Drain_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/Raw_Sewage_Tank', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_strings[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

################### Valve API ############################## 

@app.route('/Dump_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/Fill_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/EQ_Solenoid_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/FODT-1_Centrifuge-1_Outlet_Quick_Closing_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/FODT-1_Service_Pump_Outlet_Quick_Closing_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)

@app.route('/FODT-1_Main_ENG_Outlet_Quick_Closing_Valve', methods=['GET'])
def get_graph_data():
    global counter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "Priority": random_number_priority[counter % len(random_number_priority)],
        "Class": random_number_class[counter % len(random_number_class)],
        "Type": 1,
        "Text3": random_number_valve[counter % len(random_strings)],
        "Classname": "Alarm",
        "Typename": "Alarm High",
        "ServerID": "0",
        "AlarmTag": round(random.uniform(100, 4000), 0)
    }
    # Increment counter for the next cycle
    counter += 1
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345, threaded=True)
