# apache/stream_data.py

"""
This mock script simulates streaming sensor or event data into a Kafka topic.
Replace print statements with actual Kafka producer logic for real usage.
"""

import time
import random
import json

# Simulated schema
def generate_event():
    return {
        "vehicle_id": random.randint(1000, 9999),
        "speed": round(random.uniform(30, 90), 2),
        "weather": random.choice(["clear", "rain", "fog", "snow"]),
        "road_condition": random.choice(["dry", "wet", "icy"]),
        "brake_applied": random.choice([0, 1])
    }

# Simulate stream
if __name__ == "__main__":
    while True:
        event = generate_event()
        print("Sending event:", json.dumps(event))  # Replace with Kafka producer.send()
        time.sleep(2)
