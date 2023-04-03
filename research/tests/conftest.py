import sys
import os


# Add the parent folder of the tests folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
from main import ReadInMeals, ExportIngredients, ReplaceIngredients




@pytest.fixture
def meals_data():
    """Return the data from the meals JSON file."""
    filepath = os.path.join(os.path.dirname(__file__), 'data/meals.json')
    reader = ReadInMeals(filepath)
    return reader.get_meals()

@pytest.fixture
def expected_ingredients():
    """Return the expected ingredients from the meals JSON file."""
    filepath = os.path.join(os.path.dirname(__file__), 'data/expected_ingredients.json')
    with open(filepath, encoding='utf-8') as f:
        ingredients = json.load(f)
    return ingredients

@pytest.fixture
def unique_ingredients(tmp_path):
    """Return the path to a unique ingredients JSON file in a temporary directory."""
    filepath = tmp_path / 'unique_ingredients.json'
    exporter = ExportIngredients(str(filepath))
    yield filepath
    os.remove(filepath)

@pytest.fixture
def meals_with_numbered_ingredients(meals_data, unique_ingredients):
    """Return the meals data with ingredients replaced by their unique IDs."""
    exporter = ExportIngredients(str(unique_ingredients))
    exporter.export(meals_data)
    with open(unique_ingredients, encoding='utf-8') as f:
        unique_ingredients_data = json.load(f)
    replacer = ReplaceIngredients(meals_data, unique_ingredients_data)
    new_meals_data = replacer.replace()
    return new_meals_data

