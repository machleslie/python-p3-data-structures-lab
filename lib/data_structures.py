spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list = [name["name"] for name in spicy_foods]
    return list

def get_spiciest_foods(spicy_foods):
    list = [food for food in spicy_foods if food["heat_level"]>5]
    return list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"] * "🌶"
        if food["heat_level"]>5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")



def get_average_heat_level(spicy_foods):
    for food in spicy_foods:
        average = [food["heat_level"]]
    
    sum_element = sum(average)
    length = len(average)
    integer = sum_element / length    
    return integer


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
    