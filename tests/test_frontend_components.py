```python
import unittest
from unittest.mock import patch
from frontend.src.components import Interface, CustomQueries, EducationalContent, Visualization, ExoplanetDetails, Subscription, Login, Register, Profile, Footer, Header

class TestFrontendComponents(unittest.TestCase):

    def setUp(self):
        self.interface = Interface()
        self.customQueries = CustomQueries()
        self.educationalContent = EducationalContent()
        self.visualization = Visualization()
        self.exoplanetDetails = ExoplanetDetails()
        self.subscription = Subscription()
        self.login = Login()
        self.register = Register()
        self.profile = Profile()
        self.footer = Footer()
        self.header = Header()

    def test_interface(self):
        self.assertEqual(self.interface.render(), "Interface Rendered")

    def test_customQueries(self):
        self.assertEqual(self.customQueries.render(), "Custom Queries Rendered")

    def test_educationalContent(self):
        self.assertEqual(self.educationalContent.render(), "Educational Content Rendered")

    def test_visualization(self):
        self.assertEqual(self.visualization.render(), "Visualization Rendered")

    def test_exoplanetDetails(self):
        self.assertEqual(self.exoplanetDetails.render(), "Exoplanet Details Rendered")

    def test_subscription(self):
        self.assertEqual(self.subscription.render(), "Subscription Rendered")

    def test_login(self):
        self.assertEqual(self.login.render(), "Login Rendered")

    def test_register(self):
        self.assertEqual(self.register.render(), "Register Rendered")

    def test_profile(self):
        self.assertEqual(self.profile.render(), "Profile Rendered")

    def test_footer(self):
        self.assertEqual(self.footer.render(), "Footer Rendered")

    def test_header(self):
        self.assertEqual(self.header.render(), "Header Rendered")

if __name__ == '__main__':
    unittest.main()
```