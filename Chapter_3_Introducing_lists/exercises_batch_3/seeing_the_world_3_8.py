
locations = ["italy", "seatle", "san-francisco", "taiwhan", "california"]

print("\nThis is original list")
print(locations)

print("\nThis is a list using the sorted() function") #sorted alphabeticly with a function instead of arguments
print(sorted(locations))

print("\nThis is a list with reverse argument")
print(sorted(locations, reverse=True)) #this is how the argument is written

print("\nThis is a list using the reverse() methode") 
locations.reverse()
print(locations)

print("\nThis is a list using the reverse() methode") #reversed back
locations.reverse()
print(locations)

print("\nThis is a list using the sort() methode") #sort alphabeticly
locations.sort()
print(locations)

print("\nThis is a list using the sort() methode with the reverse argument") #sort alphabeticly but backwards
locations.sort(reverse=True)
print(locations)