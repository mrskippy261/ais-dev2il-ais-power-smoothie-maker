import tempfile
from pathlib import Path
from main import get_ingredients

def test_get_ingredients():
    """get_ingredients successfully returns ingredients from the file"""
    # Given: a recipe file with some ingredients
    content = "Apple\nBanana\nOrange\n"
    with tempfile.TemporaryDirectory() as tmp_path:
        recipe_file = Path(tmp_path) / "recipe.txt"
        recipe_file.write_text(content)
        expected = ["Apple", "Banana", "Orange"]
        # When: we call get_ingredients
        result = get_ingredients(recipe_file)
        # Then: we get the expected list of ingredients
        assert result == expected