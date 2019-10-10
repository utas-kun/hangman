import module_hangman

import random

colors = ["white",
          "black",
          "red",
          "pink",
          "orange",
          "blue",
          "yellow",
          "green",
          "purple",
          "gray",
          "brown",
          "gold",
          "silver"
          ]

hangman(colors[random.randint(0,len(colors))])