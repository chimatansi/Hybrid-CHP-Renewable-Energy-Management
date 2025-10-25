class CostAnalyzer:
    def __init__(self):
        self.cost_data = []

    def add_cost(self, cost: float):
        self.cost_data.append(cost)

    def aggregate_costs(self):
        return sum(self.cost_data)

    def generate_summary(self):
        total_cost = self.aggregate_costs()
        return {
            "total_cost": total_cost,
            "average_cost": total_cost / len(self.cost_data) if self.cost_data else 0
        }