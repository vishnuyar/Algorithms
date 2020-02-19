#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_times = []
  if(recipe.keys()==ingredients.keys()):
    for item in recipe:
      recipe_times.append(ingredients[item]//recipe[item])
    return min(recipe_times)
  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  #recipe_batches(recipe, ingredients)
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))