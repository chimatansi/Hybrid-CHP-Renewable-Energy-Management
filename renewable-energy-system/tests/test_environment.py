def test_energy_environment():
    import pytest
    from src.environment.energy_environment import EnergyEnvironment

    @pytest.fixture
    def env():
        return EnergyEnvironment(weather_data_path="data/weather_datasets.csv")

    def test_reset(env):
        state, _ = env.reset()
        assert state is not None

    def test_step(env):
        action = [0, 0, 0]  # Example action
        state, reward, done, _, _ = env.step(action)
        assert state is not None
        assert isinstance(reward, float)
        assert isinstance(done, bool)

    def test_render(env):
        env.render()  # Ensure no errors occur during rendering

    def test_close(env):
        env.close()  # Ensure no errors occur during closing the environment