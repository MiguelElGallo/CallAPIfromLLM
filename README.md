# CallAPIfromLLM
Call and API from an LLM

## Command Line Utility for Weather Data

This repository contains a command line utility that uses the Azure OpenAI GPT-4 model to call the Open-Meteo API for weather data.

### Prerequisites

- Python 3.6 or higher
- Install the required libraries:
  ```sh
  pip install openmeteo-requests requests-cache retry-requests numpy pandas
  ```

### Environment Variables

Set the following environment variables for the OpenAI API key and URL:
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_API_URL`: The URL for the OpenAI API

### Usage

To use the command line utility, run the following command:
```sh
python weather_cli.py <latitude> <longitude>
```

Replace `<latitude>` and `<longitude>` with the coordinates of the location you want to get the weather data for.

### Example

```sh
python weather_cli.py 52.52 13.41
```

This will fetch and display the weather data for the specified location.

### Virtual Environment Setup

To create a virtual environment, run the following command:
```sh
python -m venv .venv
```

To activate the virtual environment, use the following command:
```sh
source .venv/bin/activate
```

To install the required libraries, run:
```sh
pip install -r requirements.txt
```
