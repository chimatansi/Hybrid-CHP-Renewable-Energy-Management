class ReliabilityAnalyzer:
    def __init__(self, component_specs):
        self.component_specs = component_specs
        self.history = []

    def calculate_component_reliability(self, component_name: str, operation_hours: int) -> dict:
        # Placeholder for reliability calculation logic
        reliability = {
            'component_name': component_name,
            'reliability_score': 0.95,  # Example score
            'operation_hours': operation_hours
        }
        return reliability

    def update_history(self, demand: float, generation: float, shortfall: float) -> None:
        self.history.append({
            'demand': demand,
            'generation': generation,
            'shortfall': shortfall
        })

    def calculate_system_metrics(self) -> dict:
        # Placeholder for system metrics calculation logic
        total_demand = sum(entry['demand'] for entry in self.history)
        total_generation = sum(entry['generation'] for entry in self.history)
        total_shortfall = sum(entry['shortfall'] for entry in self.history)

        metrics = {
            'total_demand': total_demand,
            'total_generation': total_generation,
            'total_shortfall': total_shortfall,
            'reliability': (total_generation / total_demand) * 100 if total_demand > 0 else 0
        }
        return metrics

    def generate_metrics_report(self) -> str:
        metrics = self.calculate_system_metrics()
        report = f"Total Demand: {metrics['total_demand']}\n"
        report += f"Total Generation: {metrics['total_generation']}\n"
        report += f"Total Shortfall: {metrics['total_shortfall']}\n"
        report += f"System Reliability: {metrics['reliability']:.2f}%\n"
        return report

    def print_reliability_metrics(self) -> None:
        report = self.generate_metrics_report()
        print(report)

    def print_all_metrics(self) -> None:
        self.print_reliability_metrics()