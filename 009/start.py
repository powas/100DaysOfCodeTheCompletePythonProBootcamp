# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting Dictionary on a Dictionary
travel_log = {
    "France": {"cities_vistied": ["Paris", "Lillie", "Dijon"],
               "total_visits": 12,
    },
    "Spain": {"cities_visited": ["Madrid", "Barcelona"],
              "total_visits": 18,
    },
}

# Nesting Dictionary on a List
travel_log = [
    {
        "country": "France",
        "cities_vistied": ["Paris", "Lillie", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Spain",
        "cities_visited": ["Madrid", "Barcelona"],
        "total_visits": 18,
    },
]
