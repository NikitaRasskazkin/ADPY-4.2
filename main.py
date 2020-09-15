import unittest
import requests
import json


class Yandex_Api_Test(unittest.TestCase):

    def test_creation_folder(self):
        with open('fixture.json', encoding='utf-8') as f:
            tests = json.load(f)
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {"Authorization": ""}
        for path, status_code in tests:
            with self.subTest():
                params = {"path": path}
                response = requests.put(url, params=params, headers=headers).status_code
                self.assertEqual(response, status_code)
                if response / 100 == 2:
                    response = requests.get(url, params=params, headers=headers).status_code
                    if status_code / 100 == 2:
                        code = 200
                    else:
                        code = 404
                    self.assertEqual(response, code)


if __name__ == '__main__':
    unittest.main()
