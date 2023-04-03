import json

class ReadInMeals:
    """A class for reading in meals from a JSON file."""

    def __init__(self, filepath):
        """Initialize the ReadInMeals class.

        Args:
            filepath (str): The path to the input JSON file.
        """
        self.filepath = filepath
        
    def get_meals(self):
        """Read in the meals from the JSON file and return them.

        Returns:
            list: A list of dictionaries representing the meals.
        """
        with open(self.filepath, encoding='utf-8') as f:
            meals = json.load(f)
        return meals


class ExportIngredients:
    """A class for extracting and exporting unique ingredients."""

    def __init__(self, filepath):
        """Initialize the ExportIngredients class.

        Args:
            filepath (str): The path to the output JSON file.
        """
        self.filepath = filepath
        
    def export(self, meals):
        """Extract the unique ingredients from the meals and export them to a JSON file.

        Args:
            meals (list): A list of dictionaries representing the meals.
        """
        unique_ingredients = {}
        for meal in meals:
            for ingredient in meal['ingredients']:
                if ingredient not in unique_ingredients:
                    unique_id = len(unique_ingredients) + 1
                    unique_ingredients[ingredient] = unique_id
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(unique_ingredients, f, ensure_ascii=False)


class ReplaceIngredients:
    """A class for replacing ingredients in a list of meals with their unique ID numbers."""

    def __init__(self, meals, unique_ingredients):
        """Initialize the ReplaceIngredients class.

        Args:
            meals (list): A list of dictionaries representing the meals.
            unique_ingredients (dict): A dictionary of unique ingredients and their ID numbers.
        """
        self.meals = meals
        self.unique_ingredients = unique_ingredients
        
    def replace(self):
        """Replace the ingredients in the meals list with their unique ID numbers.

        Returns:
            list: A new list of dictionaries representing the meals, with ingredients replaced by ID numbers.
        """
        new_meals = []
        for meal in self.meals:
            new_meal = meal.copy()
            new_ingredients = []
            for ingredient in meal['ingredients']:
                unique_id = self.unique_ingredients[ingredient]
                new_ingredients.append(unique_id)
            new_meal['ingredients'] = new_ingredients
            new_meals.append(new_meal)
        return new_meals


def process_meal_json(input_file, output_file, ingredients):
    """Read in meals from a JSON file, extract unique ingredients, replace ingredients with unique IDs, and export to a new JSON file.

    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output JSON file.
		ingredients (str): The path to the output ingredient JSON file.
    """
    meals_reader = ReadInMeals(input_file)
    meals = meals_reader.get_meals()

    ingredients_exporter = ExportIngredients(ingredients)
    ingredients_exporter.export(meals)

    with open(ingredients, encoding='utf-8') as f:
        unique_ingredients = json.load(f)

    replacer = ReplaceIngredients(meals, unique_ingredients)
    new_meals = replacer.replace()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_meals, f, ensure_ascii=False)


if __name__ == '__main__':
	list_of_meals = 'meals_v1.json'
	list_of_ingredients = 'ingredients.json'
	list_of_meals_with_numbered_ingredients = 'meals_numbered_ingredients.json'

	process_meal_json(list_of_meals, list_of_meals_with_numbered_ingredients, list_of_ingredients)
