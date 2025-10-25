def calculate_system_efficiency(generation: float, demand: float) -> float:
    """Calculate the overall system efficiency."""
    if demand == 0:
        return 0
    return (generation / demand) * 100

def calculate_reliability(metrics: dict) -> float:
    """Calculate the reliability of the system based on provided metrics."""
    return metrics.get('uptime', 0) / (metrics.get('uptime', 0) + metrics.get('downtime', 1)) * 100

def report_metrics(metrics: dict) -> None:
    """Print a report of the system metrics."""
    print("System Metrics Report:")
    print(f"Total Generation: {metrics.get('total_generation', 0)} kWh")
    print(f"Total Demand: {metrics.get('total_demand', 0)} kWh")
    print(f"System Efficiency: {calculate_system_efficiency(metrics.get('total_generation', 0), metrics.get('total_demand', 0)):.2f}%")
    print(f"System Reliability: {calculate_reliability(metrics):.2f}%")