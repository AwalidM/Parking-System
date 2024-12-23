import unittest
import requests
import os

class TestSmartParkingSystem(unittest.TestCase):

    def test_homepage_loads(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)

    def test_api_endpoint(self):
        response = requests.get('http://localhost:8000/api/available-spots')
        self.assertEqual(response.status_code, 200)
        self.assertIn('spots', response.json())

    def test_404_page(self):
        response = requests.get('http://localhost:8000/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
