```python
import unittest
from backend.habitability_assessment import assessHabitability

class TestHabitabilityAssessment(unittest.TestCase):

    def setUp(self):
        self.exoplanetData = {
            "name": "Kepler-22b",
            "size": 2.4,
            "distance_from_star": 600,
            "atmospheric_composition": {"N2": 78, "O2": 21, "Ar": 0.9, "CO2": 0.04},
            "temperature": 22,
            "water_presence": True
        }

    def test_assessHabitability(self):
        result = assessHabitability(self.exoplanetData)
        self.assertIsInstance(result, dict)
        self.assertIn('habitability_score', result)
        self.assertIn('habitability_status', result)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            assessHabitability({})

if __name__ == '__main__':
    unittest.main()
```