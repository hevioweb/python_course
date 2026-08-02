guest_list = ["John Kiriakou", "Boris Churnij", "Random Kid"]

# for removing something from a list we have 3 methdos: del, remove and pop. In our case we will use pop because we want to reuse the item in our print call

guest_cant_come = guest_list.pop(1)

message_not_to_come = f"Hey {guest_cant_come}, im sorry you cant come"
message_to_come_01 = f"Hey {guest_list[0]}, you are invited to my dinner"
message_to_come_03 = f"Hey {guest_list[1]}, you are invited to my dinner" #now here we need to use lower index because index 2 was popped from the list


guest_list.insert(0, "Trump")
guest_list.insert(2, "Biden")
guest_list.append("Zelya")

message_to_come_04 = f"Hey {guest_list[2]}, you are invited to my dinner"
message_to_come_05 = f"Hey {guest_list[3]}, you are invited to my dinner" 
message_to_come_06 = f"Hey {guest_list[4]}, you are invited to my dinner" 


print(message_to_come_01)
print(message_to_come_03)

print(message_not_to_come)

print("Hey i found  bigger table guys")

print(message_to_come_04)
print(message_to_come_05)
print(message_to_come_06)