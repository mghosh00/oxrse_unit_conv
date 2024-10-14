import unittest
from oxrse_unit_conv.units import day, second


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(day.si_unit.matches(second))

    def test_basic_conversion(self):
        self.assertEqual(day.to_si(1), 86400)
        self.assertEqual(day.to_unit(10, day), 10)


if __name__ == '__main__':
    unittest.main()
