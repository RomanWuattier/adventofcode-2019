import sys
from math import ceil


RECIPES = {}


def split_name_from_amount(item):
    i_amount, i_name = item.split()
    return i_name, int(i_amount)


def fill_recipes(puzzle_input):
    for l in puzzle_input:
        i, o = l.strip().split('=>')
        o_name, o_amount = split_name_from_amount(o)
        RECIPES[o_name] = {
            'amount': o_amount,
            'ingredients': [[ingredient for ingredient in split_name_from_amount(ing)] for ing in i.split(', ')]
        }


def produce(fuel_recipe, fuel_produced = 1):
    queue = []

    queue.append(('FUEL', fuel_produced))

    ore = 0
    leftover = {}

    while queue:
        needed_ingredient, needed_amount = queue.pop(0)

        if needed_ingredient not in RECIPES:
            ore += needed_amount
            continue

        recipe = RECIPES[needed_ingredient]
        produced = recipe['amount']
        ingredients = recipe['ingredients']

        if needed_ingredient in leftover:
            remaining = min(leftover[needed_ingredient], needed_amount)
            needed_amount -= remaining
            leftover[needed_ingredient] -= remaining

        times = ceil(needed_amount / produced)

        if needed_ingredient in leftover:
            leftover[needed_ingredient] += produced * times - needed_amount
        else: 
            leftover[needed_ingredient] = produced * times - needed_amount

        for ingredient, amount in ingredients:
            queue.append((ingredient, amount * times))

    return ore


def binary_search(left, right, goal):
    middle = 0

    while left < right - 1:
        middle = (left + right) // 2
        ore = produce(RECIPES['FUEL'], middle)
        if ore == goal:
            return middle
        elif ore < goal:
            left = middle
        else:
            right = middle

    return middle


if __name__ == '__main__':
    with open(sys.argv[1]) as puzzle_input:
        puzzle_input = [l.strip() for l in puzzle_input.readlines()]
        fill_recipes(puzzle_input)

        # Part 1
        ore = produce(RECIPES['FUEL'])
        print(ore)

        # Part 2
        left = int(1000000000000 / ore)
        right = 1000000000000
        print(binary_search(left, right, 1000000000000))
