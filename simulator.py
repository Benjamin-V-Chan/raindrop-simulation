# Runs core simulation to determine impact of movement speed on rain exposure based on configurable settings

# simulator.py
from utils import load_config

# Load all settings from config.json
config = load_config()

# Access variables directly from the loaded config dictionary
rainfall = config["rainfall"]
player = config["player"]
simulation = config["simulation"]
output = config["output"]