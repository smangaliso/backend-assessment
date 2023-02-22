"""This is a Python script that defines a Fruit class and several subclasses for different types of fruits. Each
subclass initializes a new instance of the Fruit class and sets its own properties, such as whether the fruit is
citrus, the amount of vitamin C it contains, and its flavor strength.

The script also defines a fruit_factory function that takes a fruit name and weight as input and returns a new fruit
instance of the given type with the specified weight. Additionally, it defines a recipe function that takes a list of
fruit types and weights as input and calculates the total weight, citrus content, vitamin C content, and top flavors
of the fruit list.

The Fruit class has a get_properties method that returns a dictionary of the fruit's properties, including whether it
is citrus, the amount of vitamin C it contains, and its flavor strength.

Overall, this script provides a useful framework for working with different types of fruits and calculating their
properties for use in recipes or other applications.

"""

import argparse
import sys


class Fruit:
    def __init__(self, weight):
        # Initializes a new Fruit instance with the given weight
        self.weight = weight
        self.citrus = False
        self.vitamin_c = 0.0
        self.flavour_strength = 0.0

    def get_properties(self):
        # Returns a dictionary of the fruit's properties
        return {
            'citrus': self.citrus,
            'vitamin_c': self.vitamin_c,
            'flavour_strength': self.flavour_strength
        }


# Defines subclasses for different types of fruits, each with their own properties
class Apple(Fruit):
    # Initializes a new Apple instance with the given weight
    def __init__(self, weight):
        super().__init__(weight)
        self.citrus = False
        self.vitamin_c = 75.0
        self.flavour_strength = 50.0


class Banana(Fruit):
    # Initializes a new Banana instance with the given weight
    def __init__(self, weight):
        super().__init__(weight)
        self.citrus = False
        self.vitamin_c = 85.0
        self.flavour_strength = 40.0


class Orange(Fruit):
    # Initializes a new Orange instance with the given weight
    def __init__(self, weight):
        super().__init__(weight)
        self.citrus = True
        self.vitamin_c = 150.0
        self.flavour_strength = 70.0


class Strawberry(Fruit):
    # Initializes a new Strawberry instance with the given weight
    def __init__(self, weight):
        super().__init__(weight)
        self.citrus = False
        self.vitamin_c = 90.0
        self.flavour_strength = 50


class Lemon(Fruit):
    # Initializes a new Lemon instance with the given weight
    def __init__(self, weight):
        super().__init__(weight)
        self.citrus = True
        self.vitamin_c = 130.0
        self.flavour_strength = 90


def fruit_factory(fruit_name, grams):
    # Returns a new fruit instance of the given type with the specified weigh
    if fruit_name == 'apple':
        return Apple(grams)
    elif fruit_name == 'banana':
        return Banana(grams)
    elif fruit_name == 'orange':
        return Orange(grams)
    elif fruit_name == 'strawberry':
        return Strawberry(grams)
    elif fruit_name == 'lemon':
        return Lemon(grams)
    else:
        # Raises a ValueError if an unsupported fruit type is given
        raise ValueError(f'Unsupported fruit type: {fruit_name}')


def get_flavour_strength(item):
    return item[1]


def recipe(fruit_list):
    # Calculates the total weight, citrus content, vitamin C content, and top flavours of a list of fruits
    total_weight = 0
    total_citrus = 0
    total_vitamin_c = 0
    flavours = {}

    for fruit, weight in fruit_list:
        # Creates a new fruit instance of the given type with the specified weight
        try:
            weight = float(weight)
        except ValueError:
            print(f'Error: weight "{weight}" is not a number.')
            return None

        try:
            fruit_instance = fruit_factory(fruit, weight)
        except ValueError as e:
            print(str(e))
            return None

        # Gets the fruit's properties and adds them to the total values
        fruit_props = fruit_instance.get_properties()
        total_weight += weight
        total_citrus += int(fruit_props['citrus']) * weight
        total_vitamin_c += fruit_props['vitamin_c'] * weight

        # Check if the fruit has already been added to the dictionary
        if fruit in flavours:
            # If it has, add the weight to the existing entry
            flavours[fruit] += fruit_props['flavour_strength'] * weight
        else:
            # Otherwise, create a new entry for the fruit
            flavours[fruit] = fruit_props['flavour_strength'] * weight

    sorted_flavours = sorted(flavours.items(), key=get_flavour_strength, reverse=True)
    top_flavours = [x[0] for x in sorted_flavours[:2]]

    return {
        'fruits': set([x[0] for x in fruit_list]),
        'total_weight': total_weight,
        'total_citrus': total_citrus / total_weight * 100,
        'total_vitamin_c': total_vitamin_c,
        'top_flavours': top_flavours
    }


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Create a smoothie recipe')

    # Add arguments for the smoothie name and the fruits to include
    parser.add_argument('--name', type=str, help='the name of the smoothie')
    parser.add_argument('--fruit', nargs=2, action='append', metavar=('type', 'weight'),
                        help='the type and weight of a fruit to include in the smoothie')

    # Parse the command line arguments
    args = parser.parse_args()

    # Check if the arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Extract the smoothie name and fruit list from the arguments
    smoothie_name = args.name
    fruit_list = []
    for fruit_name, weight in args.fruit:
        try:
            fruit_list.append((fruit_name.lower(), weight))
        except ValueError as e:
            print(e)
            return

    # Create the smoothie recipe
    smoothie_recipe = recipe(fruit_list)

    if smoothie_recipe:
        print(f'Smoothie Name: {smoothie_name}')
        print(f'Fruits: {smoothie_recipe["fruits"]}')
        print(f'Total Weight: {smoothie_recipe["total_weight"]}')
        print(f'Total Citrus Content: {smoothie_recipe["total_citrus"]:.2f}%')
        print(f'Total Vitamin C: {smoothie_recipe["total_vitamin_c"]:.2f} mg')
        print(f'Top Flavours: {smoothie_recipe["top_flavours"]}')


if __name__ == '__main__':
    main()
