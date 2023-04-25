import json


def json_to_list_dict(filepath: str) -> list[dict]:
    """JSON to list of dictionaries.

    :param filepath:
    :type filepath: str
    :rtype: list[dict]
    """
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_unique_ingredients(output_file: str, meals: list[dict]) -> None:
    """Write JSON of unique ingredients.

    :param output_file:
    :type output_file: str
    :param meals:
    :type meals: List[dict]
    """
    unique_ingredients = {}

    for meal in meals:
        for ingredient in meal["ingredients"]:
            if ingredient not in unique_ingredients:
                unique_id = len(unique_ingredients) + 1
                unique_ingredients[ingredient] = unique_id

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(unique_ingredients, file, ensure_ascii=False)


def replace_ingreds_with_numbers(meals, unique_ingredients):
    """Replace ingredients in a list of meals with
    their unique ID numbers.

    Args:
        meals (list): A list of dictionaries representing the meals.
        unique_ingredients (dict): A dictionary of unique ingredients
                    and their ID numbers.

    Returns:
        list: A new list of dictionaries representing the meals,
                    with ingredients replaced by ID numbers.
    """
    new_meals = []
    for meal in meals:
        new_meal = meal.copy()
        new_ingredients = []
        for ingredient in meal["ingredients"]:
            unique_id = unique_ingredients[ingredient]
            new_ingredients.append(unique_id)
        new_meal["ingredients"] = new_ingredients
        new_meals.append(new_meal)
    return new_meals


def process_meal_json(input_file, output_file, ingredients):
    """Read in meals from a JSON file, extract unique ingredients, replace
        ingredients with unique IDs, and export to a new JSON file.

    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output JSON file.
                ingredients (str): The path to the output ingredient JSON file.
    """
    meals_reader = ReadInMeals(input_file)
    meals = meals_reader.get_meals()

    ingredients_exporter = ExportIngredients(ingredients)
    ingredients_exporter.export_meals(meals)

    with open(ingredients, encoding="utf-8") as file:
        unique_ingredients = json.load(file)

    replacer = ReplaceIngredients(meals, unique_ingredients)
    new_meals = replacer.replace()

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(new_meals, file, ensure_ascii=False)


if __name__ == "__main__":
    LIST_OF_MEALS = "meals_v1.json"
    LIST_OF_INGREDIENTS = "ingredients.json"
    MEALS_NUM_INGREDIENTS = "meals_numbered_ingredients.json"

    process_meal_json(LIST_OF_MEALS, MEALS_NUM_INGREDIENTS, LIST_OF_INGREDIENTS)
