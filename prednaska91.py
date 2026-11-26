import unittest
import random
from unittest.mock import MagicMock


class API:
    def fetch_data(self):
        # slozita logika pripojeni nekam na api
        return {"data": random.choice(["nahoda1", "nahoda2", "nahoda3"]), "number": random.randint(1, 10)}


class Processor:
    def __init__(self):
        self.api = API()
    
    def get_data(self):
        return self.api.fetch_data()["data"]
    
    def get_incremented_number(self):
        return self.api.fetch_data()["number"] + 1


class DownloadTest(unittest.TestCase):
    def test_download(self):
        api = API()
        api.fetch_data = MagicMock(return_value={"data": "test", "number": 1})
        data = api.fetch_data()
        self.assertEqual(data["data"], "test")
        self.assertEqual(data["number"], 1)

    def test_processor(self):
        processor = Processor()
        processor.api.fetch_data = MagicMock(return_value={"data": "test", "number": 1})
        self.assertEqual(processor.get_data(), "test")
        self.assertEqual(processor.get_incremented_number(), 2)

if __name__ == "__main__":
    unittest.main()
