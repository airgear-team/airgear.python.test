import unittest
from traceback import print_tb

import requests


class TestAdminUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\nТестування почато\n")

    # Базове посилання
    BASE_URL = 'http://localhost:8082'
    ADMIN_TOKEN = 'token_here'  # Вставте правильний токен тут

    def test_return_goods_count(self):
        print(f"\ntest_return_goods_count почато")
        URL = f'{self.BASE_URL}/admin/goods/count'

        headers = {
            'Authorization': f'Bearer {self.ADMIN_TOKEN}'
        }

        response = requests.get(URL, headers=headers)

        # Перевіряємо статус-код відповіді
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code,
                         f'Очікуваний статус-код 200, отримано {response.status_code}')

        self.assertTrue(response.headers['Content-type'].startswith('application/json'),
                        'Файл не відповідає розширенню JSON')

        response_data = response.json()
        for count in response_data:
            self.assertIn('count', count, "Бракує \'count\' у JSON файлі")

        # Перевіряємо, що відповідь містить очікувану структуру
        if len(response_data) == 0:
            print("Файл пустий")
        else:
            print(f"Вміст файлу: {response_data} \n")

    def test_return_goods_count_top(self):
        print("\ntefst_return_goods_count_top почато")
        URL = f'{self.BASE_URL}/admin/goods/count/top'

        headers = {
            'Authorization': f'Bearer {self.ADMIN_TOKEN}'
        }

        response = requests.get(URL, headers=headers)

        # Перевіряємо статус-код відповіді
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code,
                         f'Очікуваний статус-код 200, отримано {response.status_code}')

        self.assertTrue(response.headers['Content-type'].startswith('application/json'),
                        'Файл не відповідає розширенню JSON')

        response_data = response.json()
        for count in response_data:
            self.assertIn('count', count, "Бракує \'count\' у JSON файлі")

        # Перевіряємо, що відповідь містить очікувану структуру
        if len(response_data) == 0:
            print("Файл пустий")
        else:
            print(f"Вміст файлу: {response_data} \n")

    def test_return_count_new_date(self):
        print("\ntest_return_count_new_date почато")
        URL = f'{self.BASE_URL}/admin/goods/count/new?fromDate=2023-09-01T00:00:00Z&toDate=2024-09-10T23:59:59Z'  # Вставте власний формат дати
        headers = {
            'Authorization': f'Bearer {self.ADMIN_TOKEN}'
        }

        response = requests.get(URL, headers=headers)

        # Перевіряємо статус-код відповіді
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code,
                         f'Очікуваний статус-код 200, отримано {response.status_code}')

        self.assertTrue(response.headers['Content-type'].startswith('application/json'),
                        'Файл не відповідає розширенню JSON')

        response_data = response.json()
        for count in response_data:
            self.assertIn('count', count, "Бракує \'count\' у JSON файлі")

        # Перевіряємо, що відповідь містить очікувану структуру
        if len(response_data) == 0:
            print("Файл пустий")
        else:
            print(f"Вміст файлу: {response_data} \n")

    def test_return_count_deleted_date(self):
        print("\ntest_return_count_deleted_date почато")
        URL = f'{self.BASE_URL}/admin/goods/count/deleted?fromDate=2023-09-01T00:00:00Z&toDate=2024-09-10T23:59:59Z'  # Вставте власний формат дати
        headers = {
            'Authorization': f'Bearer {self.ADMIN_TOKEN}'
        }

        response = requests.get(URL, headers=headers)

        # Перевіряємо статус-код відповіді
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code,
                         f'Очікуваний статус-код 200, отримано {response.status_code}')

        self.assertTrue(response.headers['Content-type'].startswith('application/json'),
                        'Файл не відповідає розширенню JSON')

        response_data = response.json()

        self.assertIn('count', response_data, "Бракує \'count\' у JSON файлі")
        self.assertIn('name', response_data, "Бракує \'count\' у JSON файлі")

        # Перевіряємо, що відповідь містить очікувану структуру
        if len(response_data) == 0:
            print("Файл пустий")
        else:
            print(f"Вміст файлу: {response_data} \n")

    def test_return_count_category(self):
        print("\ntest_return_count_category почато")

        URL = f'{self.BASE_URL}/admin/goods/count/category'  # Вставте власний формат дати
        headers = {
            'Authorization': f'Bearer {self.ADMIN_TOKEN}'
        }

        response = requests.get(URL, headers=headers)

        # Перевіряємо статус-код відповіді
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code,
                         f'Очікуваний статус-код 200, отримано {response.status_code}')

        self.assertTrue(response.headers['Content-type'].startswith('application/json'),
                        'Файл не відповідає розширенню JSON')

        # Перевіряємо, що відповідь містить очікувану структуру
        response_data = response.json()

        self.assertIn('content', response_data, "Бракує \'content\' у JSON файлі")
        self.assertIsInstance(response_data['content'], list, "\'content\' має бути типу list")

        self.assertGreater(len(response_data['content']), 0, "\'Content\' не має бути порожнім")

        first_category = response_data['content'][0]
        self.assertIn('name', first_category, "\'name\' поле не знайдено в категоріях")
        self.assertIn('count', first_category, "\'count\' поле не знайдено в категоріях")

        self.assertIsInstance(first_category['name'], str, "\'name\' має бути string")
        self.assertIsInstance(first_category['count'], int, "\'count\' має бути integer")

    @classmethod
    def tearDownClass(cls):
        print(f"\nТестування завершено")


if __name__ == "__main__":
    unittest.main()
