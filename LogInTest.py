import unittest
import requests

class TestSmartParkingSystem(unittest.TestCase):

    def test_homepage_loads(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200, "Homepage did not load successfully.")

    def test_api_endpoint(self):
        response = requests.get('http://localhost:8000/api/available-spots')
        self.assertEqual(response.status_code, 200, "API endpoint not reachable.")
        self.assertIn('spots', response.json(), "Response does not contain expected data.")

    def test_404_page(self):
        response = requests.get('http://localhost:8000/nonexistent')
        self.assertEqual(response.status_code, 404, "Nonexistent page did not return 404.")

if __name__ == '__main__':
    unittest.main()
