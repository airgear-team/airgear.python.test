import unittest
import requests


class TestLocationService(unittest.TestCase):
    BASE_URL = "http://localhost:8083"

    def test_location_with_prefix(self):
        # we can change the prefix below to make more different tests
        # TODO: make prefix changeable outside the code
        prefix = 'Ки'
        response = requests.get(f"{self.BASE_URL}/locations", params={"prefix": prefix})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        for location in data:
            self.assertTrue(location['settlement'].startswith(prefix))

    def test_get_location_by_id(self):
        # we can change the prefix below to make more different tests
        # TODO: make prefix changeable outside the code
        location_id = 8
        response = requests.get(f"{self.BASE_URL}/{location_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['uniqueSettlementID'], location_id)
