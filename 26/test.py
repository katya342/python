import unittest
from task import BusSchedule, Bus, Vehicle, Rail

class TestBus(unittest.TestCase):
    def setUp(self):
        self.bus = Bus("101")
        self.bus2 = Bus("202")
        self.bus3 = Bus("303")
        self.BusSchedule = BusSchedule(self.bus)
        self.rail = Rail("23")

    def test_bus(self):
        self.assertEqual(self.bus.get_number(), "101")
        self.assertEqual(type(self.bus.get_number()), str)
        self.assertIsNotNone(self.bus.get_number())
        self.assertTrue(self.bus)

    def test_is_bus(self):
        self.BusSchedule.add_bus(None, "8:00")
        self.BusSchedule.add_bus(self.bus2, "8:00")
        self.BusSchedule.add_bus(self.bus3, "8:00")
        self.BusSchedule.add_bus(self.rail, "08:00")

        self.assertTrue(self.BusSchedule.is_bus(self.bus3))
        self.assertTrue(self.BusSchedule.is_bus(self.bus2))
        self.assertFalse(self.BusSchedule.is_bus(self.rail))

    # def test_bus_schedule(self):
    #     self.BusSchedule.add_bus(self.bus.get_number(), "08:00")
    #     self.BusSchedule.add_bus(self.bus2)




if __name__ == "__main__":
    unittest.main()