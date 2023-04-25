import os

from research.main import json_to_list_dict


def test_json_to_list_dict():
    """test_fields_in_meals_json.

    :param meals_data:
    :type meals_data: str
    """
    """test_fields_in_meals_json.

    :param Dict:
    :type Dict: meals_data
    """
    """Ensure correct fields in json."""
    filepath = os.path.join(os.path.dirname(__file__), "data/meals.json")

    meals_data = json_to_list_dict(filepath)

    assert len(meals_data) == 2
    assert isinstance(meals_data[0], dict)
    assert "ID" in meals_data[0]
    assert "name" in meals_data[0]
    assert "meal_type" in meals_data[0]
    assert "ingredients" in meals_data[0]


#    def test_export_ingredients(expected_ingredients, unique_ingredients):
# #        with open(unique_ingredients, encoding="utf-8") as f:
#            ingredients = json.load(f)
#        assert ingredients == expected_ingredients

#    def test_replace_ingredients(meals_data, meals_with_numbered_ingredients):
#        assert len(meals_data) == len(meals_with_numbered_ingredients)
#        assert (
#            meals_data[0]["ingredients"]
#            != meals_with_numbered_ingredients[0]["ingredients"]
##
