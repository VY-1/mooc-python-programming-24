# Write your solution here
def read_file(file_input) ->list:
    with open(file_input) as new_file:
        word_list = []
        for line in new_file:
            line = line.replace("\n", "")
            word_list.append(line)
        return word_list

def recipes(file_input) -> list:
    file_list = read_file(file_input)
    recipes_list = []
    recipe = []

    #create recipe list
    for item in file_list:
        if item == "":
            recipes_list.append(recipe)     #add recipe to recipes_list, then reset recipe
            recipe = []
            continue

        recipe.append(item) #add item to recipe
    recipes_list.append(recipe) #append the final recipe to the recipes_list
    return recipes_list



def search_by_name(filename: str, word: str):
    found_list = []
    recipe_list = recipes(filename)
    for recipe in recipe_list:
        if word.lower() in recipe[0].lower():
            found_list.append(recipe[0])

    return found_list

def search_by_time(filename: str, prep_time: int):
    found_list = []
    recipe_list = recipes(filename)
    for recipe in recipe_list:
        if prep_time >= int(recipe[1]):
            found_list.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found_list

def search_by_ingredient(filename: str, ingredient: str):
    found_list = []
    recipe_list = recipes(filename)
    for recipe in recipe_list:
        #check if the ingredient in recipe at index starting 2 to end
        if ingredient in recipe[2:]:
            found_list.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found_list

if __name__ == "__main__":
    found_recipes = search_by_name("src/recipes1.txt","cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("src/recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)
        
    found_recipes = search_by_ingredient("src/recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)