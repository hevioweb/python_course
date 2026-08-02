rivers = ["missisipi", "amazon", "neva"]
mountains = ["zugspitze", "montblanc", "everest"]
places = ["japan", "hawaii", "usa"]


#original lists
print(f"\norig mountain list {mountains}")
print(f"\norig river list {rivers}")
print(f"\norig places list {places}")


#using sorted() function
print(f"\nFirst i would like to see {sorted(rivers)}")


#using reverse methode 
places.reverse()
print(f"\nThose are my favourite places: {places}")
places.reverse()


#using sort methode
mountains.sort()
print(f"\nThose are my favourite mountains in alphabetical order: {mountains}")


#using sort methode with reverse argument
mountains.sort(reverse=True)
print(f"\nThose are my favourite mountains in reversed alphabetical order: {mountains}")


#using len() function
print(f"\nThere are {len(rivers)} rivers in this list")
