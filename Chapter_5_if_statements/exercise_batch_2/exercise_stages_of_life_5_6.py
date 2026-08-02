age = 34

if age <= 2:
    status = "baby"
elif age <= 4:
    status = "todlet"
elif age <= 13:
    status = "kid"
elif age <= 20:
    status = "teen"
elif age <= 65:
    status = "adult"
elif age <= 100:
    status = "elderly"
else:
    age <= 150
    status = "dead"    
    
print(f"\nYour Status is: {status}\n")