def test_reliability_analyzer():
    from src.analysis.reliability_analyzer import ReliabilityAnalyzer

    # Create an instance of ReliabilityAnalyzer
    analyzer = ReliabilityAnalyzer()

    # Test reliability calculation
    result = analyzer.calculate_reliability()
    assert isinstance(result, dict), "Reliability calculation should return a dictionary."
    assert "overall_reliability" in result, "Result should contain overall_reliability."
    assert "lolp" in result, "Result should contain loss of load probability (LOLP)."

def test_cost_analyzer():
    from src.analysis.cost_analyzer import CostAnalyzer

    # Create an instance of CostAnalyzer
    analyzer = CostAnalyzer()

    # Test cost aggregation
    cost_data = analyzer.aggregate_costs()
    assert isinstance(cost_data, pd.DataFrame), "Cost aggregation should return a DataFrame."
    assert not cost_data.empty, "Cost data should not be empty."

def test_case_studies():
    from src.analysis.case_studies import CaseStudies

    # Create an instance of CaseStudies
    studies = CaseStudies()

    # Test running a case study
    results = studies.run_case_study()
    assert isinstance(results, dict), "Case study should return a dictionary of results."
    assert "summary" in results, "Results should contain a summary."