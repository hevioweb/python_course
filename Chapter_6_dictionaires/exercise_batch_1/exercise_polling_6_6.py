favorite_languages = {"jen": "python",
                      "sarah": "c",
                      "edward": "rust",
                      "phil": "python",
                      }
    
names = ["sarah", "ian", "jeff", "phil"]

for name in names:
    if name in favorite_languages:
        # `name == favorite_languages` would compare a string against the whole dictionary, which is never True. 
        # `in` checks whether the name exists as a KEY in the dictionary: True if it's there, False otherwise.
        print(f"{name}, you already took the poll")
    else:
        print(f"{name}, is invited to take the poll")
