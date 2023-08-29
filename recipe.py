import sqlite3

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeBook:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ingredients TEXT,
            instructions TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_recipe(self, recipe):
        query = "INSERT INTO recipes (name, ingredients, instructions) VALUES (?, ?, ?);"
        ingredients_str = ", ".join(recipe.ingredients)
        instructions_str = "\n".join(recipe.instructions)
        self.conn.execute(query, (recipe.name, ingredients_str, instructions_str))
        self.conn.commit()

    def search_recipe(self, keyword):
        query = "SELECT * FROM recipes WHERE lower(name) LIKE ?;"
        keyword = f"%{keyword.lower()}%"
        cursor = self.conn.execute(query, (keyword,))
        recipes = []
        for row in cursor:
            name = row[1]
            ingredients = row[2].split(", ")
            instructions = row[3].split("\n")
            recipes.append(Recipe(name, ingredients, instructions))
        return recipes

    def view_recipe(self, recipe):
        print(f"Recipe: {recipe.name}")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print("- " + ingredient)
        print("Instructions:")
        for idx, instruction in enumerate(recipe.instructions, start=1):
            print(f"{idx}. {instruction}")

    def close_connection(self):
        self.conn.close()

def main():
    db_name = "recipe_book.db"
    recipe_book = RecipeBook(db_name)

    while True:
        print("\nRecipe Book Menu:")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter instructions (one per line, enter 'done' to finish):\n")
            instructions_list = []
            while instructions.lower() != "done":
                instructions_list.append(instructions)
                instructions = input()
            new_recipe = Recipe(name, ingredients, instructions_list)
            recipe_book.add_recipe(new_recipe)
            print("Recipe added successfully!")

        elif choice == "2":
            keyword = input("Enter a keyword to search for recipes: ")
            matching_recipes = recipe_book.search_recipe(keyword)
            if matching_recipes:
                print("\nMatching Recipes:")
                for idx, recipe in enumerate(matching_recipes, start=1):
                    print(f"{idx}. {recipe.name}")
                selection = int(input("Enter the number of the recipe to view (or 0 to cancel): "))
                if 0 < selection <= len(matching_recipes):
                    recipe_book.view_recipe(matching_recipes[selection - 1])
                else:
                    print("Invalid selection.")
            else:
                print("No recipes found.")

        elif choice == "3":
            print("Exiting Recipe Book.")
            recipe_book.close_connection()
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
