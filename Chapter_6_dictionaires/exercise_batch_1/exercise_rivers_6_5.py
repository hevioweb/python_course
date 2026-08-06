rivers = {"nile": "egypt", 
          "misisipi": "USA", 
          "volga": "russia",
            }

    
for river, country in rivers.items(): #must include the .items() methode for it to work
    print(f"\nThe {river.title()} runs through {country.title()}")
    
for river in rivers.keys(): # prints only the keys
    print(river.title())
    
for country in rivers.values(): # prints only the values
    print(country.title())