# Provides helper functions to support simulation operations

# utils.py
import json

def load_config(): # Loads and returns the settings from the config file based on selected presets.

    # Load the config file
    with open("config.json", "r") as file:
        config = json.load(file)

    # Access selected presets
    selected_presets = config["selected_presets"]
    rainfall_preset = config["rainfall_presets"][selected_presets["rainfall"]]
    player_preset = config["player_presets"][selected_presets["player"]]
    simulation_preset = config["simulation_presets"][selected_presets["simulation"]]
    output_preset = config["output_presets"][selected_presets["output"]]

    # Return all settings as a single dictionary
    return {
        "rainfall": rainfall_preset,
        "player": player_preset,
        "simulation": simulation_preset,
        "output": output_preset
    }