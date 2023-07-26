```python
import unittest
from backend.statistical_analysis import conductStatisticalAnalysis

class TestStatisticalAnalysis(unittest.TestCase):

    def setUp(self):
        self.statisticalData = {
            "region": "Milky Way",
            "exoplanets": 1000,
            "habitable_exoplanets": 10,
            "potential_life_signatures": 2
        }

    def test_conductStatisticalAnalysis(self):
        result = conductStatisticalAnalysis(self.statisticalData)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('probability_of_life', result)

if __name__ == '__main__':
    unittest.main()
```