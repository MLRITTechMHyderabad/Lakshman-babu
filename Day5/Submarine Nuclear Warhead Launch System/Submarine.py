import json
import logging
from authorization import LaunchAuthorizationSystem

# Configure the logging system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Warhead:
    def __init__(self, warhead_id, type, yield_kt):
        self.id = warhead_id
        self.type = type
        self.yield_kt = yield_kt

    def description(self):
        return f"Warhead {self.id}: Type {self.type}, Yield {self.yield_kt} kt"


class NuclearSubmarine:
    def __init__(self, name, warhead_inventory):
        self.name = name
        self.warheads = [Warhead(**item) for item in warhead_inventory]
        self.invalid_attempts = 0

    def request_launch_authorization(self, code):
        logging.info(f"{self.name} requesting missile launch authorization...")

        if LaunchAuthorizationSystem.validate_code(code):
            logging.info(f"Authorization granted for {self.name}. Launching missile...")

            if self.warheads:
                warhead = self.warheads[0]
                logging.info(f"Missile deployed with payload: {warhead.description()}")
            else:
                logging.warning("Launch aborted: No warheads loaded.")
            
            self.invalid_attempts = 0
        else:
            self.invalid_attempts += 1
            logging.error("Authorization failed: Invalid code provided.")

            if self.invalid_attempts >= 3:
                logging.critical("SECURITY ALERT! Maximum failed attempts reached. Activating countermeasures...")


# Simulated JSON input for available warheads
warhead_inventory_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''

# Parse JSON to Python list
warhead_inventory = json.loads(warhead_inventory_json)

# Initialize submarine with warhead data
sub = NuclearSubmarine("USS Trident", warhead_inventory)

# Simulate failed authorization attempts
sub.request_launch_authorization("INVALID-123")
sub.request_launch_authorization("WRONG-CODE-999")
sub.request_launch_authorization("FAIL-CODE-000")

# Simulate a successful launch authorization
sub.request_launch_authorization("AUTH-XYZ123-4567-SECURE")
