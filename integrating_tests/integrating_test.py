import unittest
import requests
from parameterized import parameterized
import json


class TestLocationService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            cls.BASE_URL = config['base_url']

    @parameterized.expand([
        (prefix,) for prefix in json.load(open('config.json', 'r', encoding='utf-8'))['prefixes']
    ])
    def test_location_with_prefix(self, prefix):
        response = requests.get(f"{self.BASE_URL}/locations", params={"prefix": prefix})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        for location in data:
            self.assertTrue(location['settlement'].startswith(prefix))

    @parameterized.expand([
        (location_id,) for location_id in json.load(open('config.json', 'r', encoding='utf-8'))['location_ids']
    ])
    def test_get_location_by_id(self, location_id):
        response = requests.get(f"{self.BASE_URL}/{location_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['uniqueSettlementID'], location_id)


if __name__ == "__main__":
    unittest.main()
