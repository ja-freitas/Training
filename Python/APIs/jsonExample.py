import json

best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

print (type(best_food_chains))
print (best_food_chains)[0]

# Use json.dumps to convert best_food_chains to a string. Cannot index like a list.
best_food_chains_string = json.dumps(best_food_chains)

print (type(best_food_chains_string))
print best_food_chains_string[0]

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))


# Make a dictionary

fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# Dump a dictionary to a string and load it

fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
