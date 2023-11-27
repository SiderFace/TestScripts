class Recipe:

   def __init__(self, name, ingredients, cooking_time):
      self.name = name
      self.ingredients = ingredients
      self.cooking_time = cooking_time
      self.difficulty = None

   def get_name(self):
      return self.name

   def set_name(self, name):
      self.name = name

   def get_cooking_time(self):
      return self.cooking_time

   def set_cooking_time(self, cooking_time):
      self.cooking_time = cooking_time

   def add_ingredients(self, *ingredients):
      self.ingredients.extend(ingredients)
      self.update_all_ingredients()

   def get_ingredients(self):
      return self.ingredients

   def calculate_difficulty(self):
      if self.cooking_time < 10 and len(self.ingredients) < 4:
         self.difficulty = 'Easy'
      elif self.cooking_time < 10 and len(self.ingredients) >= 4:
         self.difficulty = 'Medium'
      elif self.cooking_time >= 10 and len(self.ingredients) < 4:
         self.difficulty = 'Intermediate'
      elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
         self.difficulty = 'Hard'

   def get_difficulty(self):
      if self.difficulty is None:
         self.calculate_difficulty()
      return self.difficulty

   def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

   def update_all_ingredients(self):
      Recipe.all_ingredients.update(self.ingredients)
       
   def __str__(self):
      return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.get_difficulty()}"

   def recipe_search(data, search_term):
      for recipe in data:
         if recipe.search_ingredient(search_term):
            print(f"Recipe found: {recipe.get_name()}")


# Recipes for 'recipes_list' :
tea = Recipe(
   name="Tea", 
   ingredients = ["Tea Leaves", "Sugar", "Water"], 
   cooking_time = 5
)

coffee = Recipe(
   name="Coffee", 
   ingredients = ["Coffee Powder", "Sugar", "Water"], 
   cooking_time = 5
)

cake = Recipe(
   name="Cake", 
   ingredients = ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 
   cooking_time = 50,
)

banana_smoothie = Recipe(
   name="Banana Smoothie", 
   ingredients = ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 
   cooking_time = 5,
)

# Add recipes to list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Print recipe list
for recipe in recipes_list:
   print(recipe)
   print("---")


# Search for recipes that contain specific ingredients:
ingredients_to_search = ['Water', 'Sugar', 'Bananas']

for ingredient in ingredients_to_search:
    print(f"\nSearching for recipes containing '{ingredient}':")
    Recipe.recipe_search(recipes_list, ingredient)

print("_______________________________________________________\n")


Recipe.all_ingredients = set()