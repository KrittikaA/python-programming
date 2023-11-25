lucky_numbers= [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
#print (friends[-1])    #lists can be accessed from the back of the list
#print (friends[1:])    #the entire list starting from position 1
#print (friends[1:3])   # prints positions 1 and 2 but not 3
friends.extend(lucky_numbers)  #append a list to another list
print(friends)
