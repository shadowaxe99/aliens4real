```python
import unittest
from backend.exoplanet_detection import detectExoplanets

class TestExoplanetDetection(unittest.TestCase):

    def setUp(self):
        self.cosmologicalData = {
            "star1": {"distance": 100, "size": 1000, "atmospheric_composition": "H2, He"},
            "star2": {"distance": 200, "size": 2000, "atmospheric_composition": "H2, He, O2"},
            "star3": {"distance": 300, "size": 3000, "atmospheric_composition": "H2, He, O2, N2"}
        }

    def test_detectExoplanets(self):
        exoplanetData = detectExoplanets(self.cosmologicalData)
        self.assertIsInstance(exoplanetData, dict)
        self.assertEqual(len(exoplanetData), 3)
        for star, data in exoplanetData.items():
            self.assertIn(star, self.cosmologicalData)
            self.assertIn("is_exoplanet", data)
            self.assertIn("category", data)

if __name__ == "__main__":
    unittest.main()
```