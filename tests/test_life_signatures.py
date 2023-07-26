```python
import unittest
from backend.life_signatures import identifyLifeSignatures

class TestLifeSignatures(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "planet_id": "exoplanet_1",
            "spectral_data": [0.2, 0.3, 0.4, 0.5, 0.6],
            "chemical_composition": {"H2O": 0.1, "CO2": 0.2, "N2": 0.7}
        }

    def test_identify_life_signatures(self):
        result = identifyLifeSignatures(self.sample_data)
        self.assertIsInstance(result, dict)
        self.assertIn('life_signature_probability', result)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            identifyLifeSignatures(None)

        with self.assertRaises(ValueError):
            identifyLifeSignatures({"invalid_key": "invalid_value"})

if __name__ == '__main__':
    unittest.main()
```