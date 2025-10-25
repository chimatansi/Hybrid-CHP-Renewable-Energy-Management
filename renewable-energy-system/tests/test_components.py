import unittest
from src.components.battery import Battery
from src.components.chp import CHP
from src.components.pv import PV
from src.components.wind import Wind

class TestComponents(unittest.TestCase):

    def setUp(self):
        self.battery = Battery(max_capacity=100, max_charge_rate=10, min_soc=0.2)
        self.chp = CHP(efficiency=0.9)
        self.pv = PV(panel_area=20, efficiency=0.15)
        self.wind = Wind(turbine_capacity=2, efficiency=0.4)

    def test_battery_charge(self):
        self.battery.charge(50)
        self.assertEqual(self.battery.state_of_charge, 50)

    def test_battery_discharging(self):
        self.battery.charge(50)
        self.battery.discharge(20)
        self.assertEqual(self.battery.state_of_charge, 30)

    def test_chp_heat_output(self):
        heat_output = self.chp.calculate_heat_output(electrical_power=100)
        self.assertEqual(heat_output, 90)  # Assuming 90% efficiency

    def test_pv_energy_generation(self):
        energy = self.pv.calculate_energy_generation(solar_irradiance=1000, hours=5)
        self.assertEqual(energy, 15)  # 20 m² * 0.15 efficiency * 5 hours

    def test_wind_energy_generation(self):
        energy = self.wind.calculate_energy_generation(wind_speed=10, hours=5)
        self.assertEqual(energy, 8)  # Assuming some calculation based on wind speed

if __name__ == '__main__':
    unittest.main()