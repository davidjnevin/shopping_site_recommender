import json

def test_read_in_meals(meals_data):
    assert len(meals_data) == 6
    assert isinstance(meals_data[0], dict)
    assert 'name' in meals_data[0]

def test_export_ingredients(expected_ingredients, unique_ingredients):
    with open(unique_ingredients, encoding='utf-8') as f:
        ingredients = json.load(f)
    assert ingredients == expected_ingredients

def test_replace_ingredients(meals_data, meals_with_numbered_ingredients):
    assert len(meals_data) == len(meals_with_numbered_ingredients)
    assert meals_data[0]['ingredients'] != meals_with_numbered_ingredients[0]['ingredients']

