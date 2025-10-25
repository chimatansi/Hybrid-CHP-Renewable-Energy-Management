class PV:
    def __init__(self, panel_area: float, efficiency: float):
        self.panel_area = panel_area  # in square meters
        self.efficiency = efficiency  # as a decimal (e.g., 0.15 for 15%)

    def calculate_energy_generation(self, solar_irradiance: float, hours: float) -> float:
        """
        Calculate the energy generation from the PV system.

        :param solar_irradiance: Solar irradiance in kW/m²
        :param hours: Number of hours of sunlight
        :return: Energy generated in kWh
        """
        return self.panel_area * self.efficiency * solar_irradiance * hours

    def __str__(self):
        return f"PV Panel: Area = {self.panel_area} m², Efficiency = {self.efficiency * 100}%"