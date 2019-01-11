from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
userChoice = HashMap(len(types))
for type in types:
  if userChoice.retrieve(type[0]) is None:
    ll = LinkedList(type)
    userChoice.assign(type[0],ll)
  else:
    ll = userChoice.retrieve(type[0])
    ll.insert_beginning(type)
    userChoice.assign(type[0],ll)

# Write code to insert restaurant data into a data structure here. The data is in data.py
restaurantChoice = HashMap(len(restaurant_data))
for restaurant in restaurant_data:
  if restaurantChoice.retrieve(restaurant[0]) is None:
    ll = LinkedList(restaurant[1:6])
    restaurantChoice.assign(restaurant[0],ll)
  else:
    ll = restaurantChoice.retrieve(restaurant[0])
    ll.insert_beginning(restaurant[1:6])
    restaurantChoice.assign(restaurant[0],ll)
    
#Write code for user interaction here
while True:
  user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
  
  #Search for user_input in food types data structure here
  if userChoice.retrieve(user_input):
    ll = userChoice.retrieve(user_input)
    current_node = ll.get_head_node()
    current_size = ll.get_size()
    current_value = current_node.get_value()

    print("\nWith those beginning letters, your choices are {}\n".format(ll.pretty_list()))

    if current_size == 1:
      restaurant_type = current_value
    elif current_size > 1:
      user_input = str(input("What type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()

      while current_node:
        current_value = current_node.get_value()

        if user_input == current_value[0:2]:
          restaurant_type = current_value
          user_input = str(input("The only option with those beginning letters is {}.  Do you want to look at {} restaurants? Enter 'y' for yes and 'n' for no\n".format(current_value.title(), current_value.title())).lower())

          if user_input == 'y':
            break
          else:
            next
        current_node = current_node.get_next_node()
      else:
        restaurant_type = 'empty'
        next

    #After finding food type write code for retrieving restaurant data here    
    if restaurant_type != 'empty':
      rc = restaurantChoice.retrieve(restaurant_type)
      
      current_node = rc.get_head_node()
      current_value = current_node.get_value()
      
      print("\n\nThe {} restaurants in Soho are\n".format(restaurant_type.title()))

      while current_node:
        current_value = current_node.get_value()
        if current_node is not None:
          print("\n--------------------------\n\nName: {}\nPrice: {}/5\nRating: {}/5\nAddress: {}\n".format(current_value[0],current_value[1],current_value[2],current_value[3]))
        current_node = current_node.get_next_node()
  
      user_input = str(input("Do you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n".lower()))
      
      if user_input == 'n':
        break