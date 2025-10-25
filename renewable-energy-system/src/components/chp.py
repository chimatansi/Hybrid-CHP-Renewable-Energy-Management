class CHP:
    def __init__(self, electrical_power: float, thermal_efficiency: float):
        self.electrical_power = electrical_power  # kW
        self.thermal_efficiency = thermal_efficiency  # fraction (0 to 1)

    def calculate_heat_output(self) -> float:
        """Calculate the heat output based on electrical power and thermal efficiency."""
        return self.electrical_power * self.thermal_efficiency  # kW

    def calculate_efficiency(self) -> float:
        """Calculate the overall efficiency of the CHP system."""
        return self.thermal_efficiency  # Return thermal efficiency as a percentage

    def __str__(self):
        return f"CHP System: {self.electrical_power} kW, Efficiency: {self.calculate_efficiency() * 100:.2f}%"