```python
import unittest
import requests

class TestAPI(unittest.TestCase):

    BASE_URL = "http://localhost:5000/api"

    def test_cosmological_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/cosmologicalData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_exoplanet_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/exoplanetData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_habitability_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/habitabilityData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_life_signature_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/lifeSignatureData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_statistical_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/statisticalData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_user_data_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/userData")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_custom_query_endpoint(self):
        query = {"starSystem": "Alpha Centauri"}
        response = requests.post(f"{self.BASE_URL}/customQuery", json=query)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), dict))

if __name__ == "__main__":
    unittest.main()
```