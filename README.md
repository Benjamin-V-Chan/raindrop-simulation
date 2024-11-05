# Raindrop Simulation

## Overview

The *Raindrop Simulation* project aims to answer the classic question: **Will you get less wet if you walk or run in the rain?** This project uses simulations to analyze and compare the amount of rain exposure under different movement speeds and rain conditions.

## Project Goal

The objective of this simulation is to provide a data-driven answer to the common debate of whether moving faster or slower in the rain results in less overall wetness. By simulating various scenarios, such as different rainfall intensities, rain angles, and player speeds, the project demonstrates how movement speed and rain conditions affect exposure.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Benjamin-V-Chan/raindrop-simulation.git
   cd raindrop-simulation
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulation:**
   ```bash
   python simulator.py
   ```

## Results and Analysis

- Simulation results are stored in the `results/` directory, with each run saved as a uniquely named CSV file.
- You can analyze specific results files by running `analyze.py`, which generates visualizations and insights into how rain exposure varies under different scenarios.

## Configuration

### `config.json` Structure

#### **rain_settings**
- **`release_rate`**: Release rate of raindrop in releases per second.
- **`spacing`**: The spacing of raindrops in centimeters.
- **`drop_height`**: The height of each raindrop in centimeters.
- **`drop_width`**: The width of each raindrop in centimeters.
- **`rain_angle`**: The angle of the rain in degrees. 
  - `0` represents rain falling vertically.
  - Positive values (e.g., `10`) represent rain angled forward (e.g., due to wind).
  - Negative values (e.g., `-10`) represent rain angled backward.

#### **player**
- **`movement_speed`**: The speed of the player in meters per second.
- **`player_height`**: The height of the player in centimeters (or other chosen unit).
- **`player_width`**: The width of the player in centimeters (or other chosen unit).

#### **simulation_settings**
- **`duration`**: The duration of the simulation in seconds.

#### **output**
- **`results_folder`**: The folder path where simulation results are saved.
- **`csv_prefix`**: A prefix added to each result CSV filename.

## Future Improvements

Planned enhancements include:
- Adding more complex rain patterns and player movement paths.
- Integrating a user-friendly interface for easier configuration.
- Providing more detailed visualizations and customizable plots.