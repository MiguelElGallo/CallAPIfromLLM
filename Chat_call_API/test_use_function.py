import pytest
from use_function import get_current_weather


def test_get_current_weather():
    # Call the function
    response = get_current_weather("59.168187", "20.762857")

    # Print the full response for inspection
    print("\nAPI Response:")
    print(response)

    # Basic assertions to verify response structure
    assert response is not None


if __name__ == "__main__":
    pytest.main([__file__])
