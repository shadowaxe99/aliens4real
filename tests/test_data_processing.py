```python
import unittest
from backend.data_processing import processCosmologicalData

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.cosmologicalData = {
            "star_system": "Kepler-22",
            "distance": 638,
            "star_type": "G-type",
            "planets": [
                {
                    "name": "Kepler-22b",
                    "radius": 2.4,
                    "orbital_period": 290,
                    "temperature": 262
                }
            ]
        }

    def test_processCosmologicalData(self):
        processed_data = processCosmologicalData(self.cosmologicalData)
        self.assertIsInstance(processed_data, dict)
        self.assertIn('star_system', processed_data)
        self.assertIn('distance', processed_data)
        self.assertIn('star_type', processed_data)
        self.assertIn('planets', processed_data)
        self.assertIsInstance(processed_data['planets'], list)
        self.assertGreater(len(processed_data['planets']), 0)

if __name__ == '__main__':
    unittest.main()
```