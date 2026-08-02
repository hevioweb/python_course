guest_list = ["John Kiriakou", "Boris Churnij", "Random Kid"]

# for removing something from a list we have 3 methdos: del, remove and pop. In our case we will use pop because we want to reuse the item in our print call
guest_cant_come = guest_list.pop(1)

#creating messages for those who can come 
print(f"Hey {guest_cant_come}, im sorry you cant come")
print(f"Hey {guest_list[0]}, you are invited to my dinner")
print(f"Hey {guest_list[1]}, you are invited to my dinner") #now here we need to use lower index because index 2 was popped from the list

#table for more people
print("\tHey i found  bigger table guys")

#adding new people
guest_list.insert(0, "Trump")
guest_list.insert(2, "Biden")
guest_list.append("Zelya")

#creating messages for new guests
print(f"Hey {guest_list[0]}, you are invited to my dinner")
print(f"Hey {guest_list[2]}, you are invited to my dinner" )
print(f"Hey {guest_list[4]}, you are invited to my dinner")

#table wont arrive
print("\tOhh shoot the table won't arrive at the right time so there is a place only for 2 guests")

#canceling some guests and leaving 2
guest_uninvited_01 = guest_list.pop()
guest_uninvited_02 = guest_list.pop()
guest_uninvited_03 = guest_list.pop()

#canceling guests
print(f"Hey {guest_uninvited_01}, im sorry you cant come")
print(f"Hey {guest_uninvited_02}, im sorry you cant come")
print(f"Hey {guest_uninvited_03}, im sorry you cant come")


print(f"\t{guest_list[0]} and {guest_list[1]} Yall can come")
