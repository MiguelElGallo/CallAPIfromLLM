import unittest
from weather_cli import ask_gpt

class TestWeatherCLI(unittest.TestCase):
    def test_ask_gpt(self):
        question = "What is the weather like at latitude 52.52 and longitude 13.41?"
        response = ask_gpt(question)
        self.assertIn("temperature_2m", response)

if __name__ == "__main__":
    unittest.main()
