import json
import os
import sys

import pytest

# Add the parent folder of the tests folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def meals_filepalth():
    """Return the data from the meals JSON file."""
    return os.path.join(os.path.dirname(__file__), "data/meals.json")


@pytest.fixture
def expected_ingredients():
    """Return the expected ingredients from the meals JSON file."""
    filepath = os.path.join(os.path.dirname(__file__), "data/expected_ingredients.json")
    with open(filepath, encoding="utf-8") as f:
        ingredients = json.load(f)
    return ingredients
