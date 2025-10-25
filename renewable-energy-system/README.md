# Renewable Energy System

This project is designed to model and analyze a renewable energy system that integrates various energy sources, including solar, wind, and combined heat and power (CHP) systems. The system aims to optimize energy generation, storage, and consumption while analyzing reliability and operational costs.

## Project Structure

- **src/**: Contains the main source code for the project.
  - **components/**: Includes classes for different energy components such as batteries, photovoltaic panels, and wind turbines.
  - **models/**: Contains the implementation of the Proximal Policy Optimization (PPO) agent and its neural network architecture.
  - **analysis/**: Includes modules for analyzing system reliability, operational costs, and running case studies.
  - **utils/**: Contains utility functions for weather data processing, system configuration, and metrics calculation.
  - **environment/**: Defines the simulation environment for the renewable energy system.

- **data/**: Contains historical weather data used for simulations and analysis.

- **tests/**: Includes unit tests for components, environment, and analysis modules to ensure code reliability.

- **notebooks/**: Contains Jupyter notebooks for analysis results and visualizations.

- **requirements.txt**: Lists the Python package dependencies required for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd renewable-energy-system
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- To run the renewable energy system simulations, execute the main script located in the `src` directory.
- Use the provided Jupyter notebooks in the `notebooks` directory for analysis and visualization of results.
- Modify the configuration settings in `src/utils/system_config.py` to adjust system parameters as needed.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.