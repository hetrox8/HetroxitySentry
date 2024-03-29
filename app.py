from flask import Flask, jsonify
from BasicBehaviorMonitor import BehaviorMonitor as BasicBehaviorMonitor
from MLBehaviorMonitor import MLBehaviorMonitor

app = Flask(__name__)

@app.route('/basic_behavior')
def basic_behavior_route():
    # Instantiate BasicBehaviorMonitor
    behavior_monitor = BasicBehaviorMonitor()
    # Implement logic to monitor basic behavior
    return jsonify({"message": "Basic behavior monitoring activated."})

@app.route('/ml_behavior')
def ml_behavior_route():
    # Instantiate MLBehaviorMonitor
    ml_behavior_monitor = MLBehaviorMonitor()
    # Implement logic to monitor behavior with machine learning anomaly detection
    return jsonify({"message": "Behavior monitoring with machine learning activated."})

if __name__ == '__main__':
    app.run(debug=True)
