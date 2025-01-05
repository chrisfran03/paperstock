import pytest
from unittest.mock import patch, MagicMock  # For simulating external dependencies
from app.fetch_stocks.fetch_stocks import (
    filter_by_price,
)

# Mock Sample test data for consistency declared as global variables
MOCK_JSON_DATA = {
    "data": {
        "table": {
            "rows": [
                {"symbol": "AAPL", "lastsale": "$150"},  
                {"symbol": "GOOG", "lastsale": "$100"},  
                {"symbol": "TSLA", "lastsale": "$10"} 
            ]
        }
    }
}


# using pytest fixtures for reusable test data
@pytest.fixture
def mock_json_response():
    return MOCK_JSON_DATA



def test_filter_by_price(mock_json_response):
    """
    Test: Ensure `filter_by_price` filters out stocks below $15.
    """

    # Arrange: Use the provided mock data
    json_data = mock_json_response

    # Act: Call the function to filter stocks
    result = filter_by_price(json_data)

    # Assert: Verify only AAPL and GOOG are returned
    assert result == ["AAPL", "GOOG"], "Stocks below $15 should be excluded."
