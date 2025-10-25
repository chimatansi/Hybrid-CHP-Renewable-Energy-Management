class Wind:
    def __init__(self, max_capacity: float, efficiency: float, reliability: dict, rotor_diameter: float):
        self.max_capacity = max_capacity  # Maximum capacity in kW
        self.efficiency = efficiency  # Efficiency as a decimal
        self.reliability = reliability  # Reliability metrics
        self.rotor_diameter = rotor_diameter  # Rotor diameter in meters

    def calculate_energy_generation(self, wind_speed: float) -> float:
        """
        Calculate energy generation based on wind speed using the power curve.
        :param wind_speed: Wind speed in m/s
        :return: Energy generated in kWh
        """
        if wind_speed < 3:  # Cut-in speed
            return 0
        elif wind_speed > 25:  # Cut-out speed
            return 0
        else:
            # Power formula: P = 0.5 * ρ * A * v^3
            # where ρ is air density (approx. 1.225 kg/m^3), A is the swept area, and v is wind speed
            air_density = 1.225  # kg/m^3
            swept_area = 3.14 * (self.rotor_diameter / 2) ** 2  # m²
            power = 0.5 * air_density * swept_area * (wind_speed ** 3) * self.efficiency  # in Watts
            return min(power / 1000, self.max_capacity)  # Convert to kW and limit to max capacity

    def check_reliability(self) -> dict:
        """
        Check the reliability of the wind turbine.
        :return: Reliability metrics
        """
        return self.reliability