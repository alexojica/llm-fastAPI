import unittest
from fastapi.testclient import TestClient
from main import app

class TestButtonClick(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_button_click(self):
        response = self.client.get('/button-click')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Button clicked!"})

if __name__ == "__main__":
    unittest.main()