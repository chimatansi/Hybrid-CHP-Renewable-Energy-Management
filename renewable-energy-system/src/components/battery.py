class Battery:
    def __init__(self, max_capacity: float, min_soc: float):
        self.max_capacity = max_capacity  # Maximum capacity in kWh
        self.min_soc = min_soc  # Minimum state of charge as a fraction (0 to 1)
        self.current_soc = max_capacity  # Current state of charge in kWh

    def charge(self, amount: float):
        """Charge the battery by a certain amount."""
        if amount < 0:
            raise ValueError("Charge amount must be positive.")
        self.current_soc = min(self.max_capacity, self.current_soc + amount)

    def discharge(self, amount: float):
        """Discharge the battery by a certain amount."""
        if amount < 0:
            raise ValueError("Discharge amount must be positive.")
        if self.current_soc - amount < self.max_capacity * self.min_soc:
            raise ValueError("Cannot discharge below minimum state of charge.")
        self.current_soc -= amount

    def get_state_of_charge(self) -> float:
        """Return the current state of charge as a fraction of maximum capacity."""
        return self.current_soc / self.max_capacity

    def is_empty(self) -> bool:
        """Check if the battery is empty."""
        return self.current_soc <= 0

    def is_full(self) -> bool:
        """Check if the battery is full."""
        return self.current_soc >= self.max_capacity